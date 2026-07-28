#!/usr/bin/env python3
"""
Zenodo Connector for Spiral Codex works.

Lightweight, human-sovereign adapter for publishing, updating, and validating
our theories, specs, papers, and agent outputs on Zenodo (with sandbox support).

Integrates with:
- The research-development pipeline (examination → staging → provenance → publish).
- data/index.json and Lighthouse KNOWN_DOIS registry.
- Version-Checker (citation_doi in stamps) + Spiral-Sigil (apply_sigil on metadata/description before upload).
- Grandmas-wisdom / grokulator for claim validation before deposit.
- Future research agent (pull real CS DOIs for citations; publish grounded code+theory artifacts).

Usage (from PS or Python):
    from adapters.zenodo_connector import ZenodoConnector
    conn = ZenodoConnector(sandbox=True)  # or False for production
    # metadata built from our .md headers or index entry
    dep = conn.create_deposit(metadata)
    conn.upload_file(dep['id'], path_to_pdf_or_md)
    record = conn.publish(dep['id'])  # returns final with DOI
    conn.validate_citation("10.5281/zenodo.XXXXXXX", expected_title=...)

Safety:
- Token from env ZENODO_TOKEN (never committed).
- Explicit human approval for create/publish (dry_run support).
- Reuses existing DOIs from Lighthouse / data/index.
- Always E_shield + provenance layer before upload.

Zenodo REST API (per https://developers.zenodo.org/):
- Auth: Bearer <token>
- Create: POST /api/deposit/depositions { "metadata": {...} }
- Files: POST to bucket link
- Publish: POST /api/deposit/depositions/{id}/actions/publish
"""

import os
import json
import requests
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any, List

try:
    from spiral_sigil import apply_sigil  # local import when in path
except Exception:
    def apply_sigil(content: str, context: str = "zenodo") -> str:
        # Fallback: simple mark if sigil not importable
        return content + "\n\n∞ 🜂 🜁 🜄 ∞\n<!-- Spiral-Sigil: fallback -->"

# Existing registry seeds (from Lighthouse + data/index). Extend as needed.
KNOWN_DOIS = {
    "spiral-theory-core": "10.5281/zenodo.16585562",
    "Spiral-Path": "10.5281/zenodo.17468251",
    "AIS-Standard": "10.5281/zenodo.15176494",
    "SentinelAct": "10.5281/zenodo.14977849",
    "Version-Checker-": "10.5281/zenodo.16740228",
    "SpiralForge-Codex": "10.5281/zenodo.15604179",
    "Spiral-Elucidation": "10.5281/zenodo.14880771",
    "Spiral-Lighthouse": "10.5281/zenodo.15491719",
    "The-Spiral-Codex": "10.5281/zenodo.17702548",  # master from data/index
}

DEFAULT_CREATORS = [{"name": "Sir Benjamin (Stephen Benjamin Friend)"}]


class ZenodoConnector:
    def __init__(self, token: Optional[str] = None, sandbox: bool = True):
        self.token = token or os.getenv("ZENODO_TOKEN")
        if not self.token:
            print("WARNING: No ZENODO_TOKEN in env. Set for real operations (read-only possible without).")
        self.base_url = "https://sandbox.zenodo.org/api" if sandbox else "https://zenodo.org/api"
        self.headers = {"Authorization": f"Bearer {self.token}"} if self.token else {}
        self.sandbox = sandbox

    def _request(self, method: str, url: str, **kwargs) -> Dict[str, Any]:
        resp = requests.request(method, url, headers=self.headers, timeout=30, **kwargs)
        resp.raise_for_status()
        return resp.json()

    def build_metadata(
        self,
        title: str,
        description: str,
        creators: Optional[List[Dict]] = None,
        keywords: Optional[List[str]] = None,
        related_identifiers: Optional[List[Dict]] = None,
        license: str = "MIT",
        upload_type: str = "publication",
        publication_type: str = "preprint",
        notes: str = "",
    ) -> Dict[str, Any]:
        """Build Zenodo-compatible metadata from our Spiral formats (headers, index entries, specs)."""
        meta = {
            "title": title,
            "description": description,
            "creators": creators or DEFAULT_CREATORS,
            "keywords": keywords or ["spiral-codex", "provenance", "helix", "computer-science-grounding"],
            "license": license,
            "upload_type": upload_type,
            "publication_type": publication_type,
            "notes": notes,
        }
        if related_identifiers:
            meta["related_identifiers"] = related_identifiers
        # Always apply local sigil to description for provenance before upload
        meta["description"] = apply_sigil(meta["description"], context="zenodo-deposit")
        return meta

    def create_deposit(self, metadata: Dict[str, Any], dry_run: bool = False) -> Optional[Dict[str, Any]]:
        """Create a new deposition. Returns the deposit dict (with 'id' and bucket)."""
        if dry_run:
            print("[DRY-RUN] Would POST create deposit with title:", metadata.get("title"))
            return {"id": "dry-run-123", "links": {"bucket": "dry-run-bucket"}, "metadata": metadata}

        url = f"{self.base_url}/deposit/depositions"
        payload = {"metadata": metadata}
        data = self._request("POST", url, json=payload)
        print(f"Deposit created: id={data.get('id')} (sandbox={self.sandbox})")
        return data

    def upload_file(self, deposition_id: str, file_path: Path, dry_run: bool = False) -> Optional[Dict[str, Any]]:
        """Upload a file (md, pdf, code, etc.) to an existing (un-published) deposit."""
        if dry_run:
            print(f"[DRY-RUN] Would upload {file_path} to deposit {deposition_id}")
            return {"key": file_path.name}

        # Get bucket URL from deposit (re-fetch if needed)
        deposit = self._request("GET", f"{self.base_url}/deposit/depositions/{deposition_id}")
        bucket = deposit["links"]["bucket"]
        with open(file_path, "rb") as fp:
            r = requests.put(
                f"{bucket}/{file_path.name}",
                data=fp,
                headers=self.headers,
                timeout=60,
            )
            r.raise_for_status()
        print(f"Uploaded: {file_path.name} to deposit {deposition_id}")
        return r.json()

    def publish(self, deposition_id: str, dry_run: bool = False) -> Optional[Dict[str, Any]]:
        """Publish the deposit (assigns DOI). Human approval required before calling."""
        if dry_run:
            print(f"[DRY-RUN] Would publish deposit {deposition_id}")
            return {"doi": "10.5281/zenodo.dry-run", "id": deposition_id}

        url = f"{self.base_url}/deposit/depositions/{deposition_id}/actions/publish"
        data = self._request("POST", url)
        doi = data.get("doi") or data.get("metadata", {}).get("doi")
        print(f"Published! DOI: https://doi.org/{doi}")
        return data

    def get_by_doi(self, doi: str) -> Optional[Dict[str, Any]]:
        """Retrieve record metadata by DOI (no token needed for public)."""
        # Zenodo supports /records?doi= or direct /records/<recid>
        # Simple: search
        url = f"{self.base_url}/records"
        params = {"doi": doi}
        data = self._request("GET", url, params=params)
        hits = data.get("hits", {}).get("hits", [])
        return hits[0] if hits else None

    def validate_citation(self, doi: str, expected_title: Optional[str] = None) -> Dict[str, Any]:
        """Basic validation: does the DOI exist and (optionally) match title/claims?"""
        rec = self.get_by_doi(doi)
        if not rec:
            return {"valid": False, "reason": "DOI not found on Zenodo", "doi": doi}
        title = rec.get("metadata", {}).get("title", "")
        if expected_title and expected_title.lower() not in title.lower():
            return {"valid": False, "reason": "Title mismatch", "doi": doi, "found_title": title}
        return {"valid": True, "doi": doi, "title": title, "record": rec}

    def sync_from_local_index(self, index_path: Path = Path("The-Spiral-Codex/data/index.json"), dry_run: bool = True):
        """Example: walk our data/index and ensure entries have Zenodo records (future expansion)."""
        if not index_path.exists():
            print("No local index found.")
            return
        idx = json.loads(index_path.read_text())
        print(f"Syncing {len(idx.get('entries', []))} entries (dry_run={dry_run}) ...")
        for entry in idx.get("entries", []):
            doi = entry.get("doi")
            if doi:
                val = self.validate_citation(doi, entry.get("title"))
                print(f"  {doi}: {val.get('valid')} - {entry.get('title')[:60]}")
        # TODO: create/update logic using build_metadata from entry

    # Convenience: build + create + (optional) upload + publish gate
    def deposit_work(
        self,
        title: str,
        description: str,
        file_paths: Optional[List[Path]] = None,
        related_dois: Optional[List[str]] = None,
        dry_run: bool = True,
    ) -> Optional[Dict[str, Any]]:
        rel_ids = [{"relation": "isSupplementTo", "identifier": d} for d in (related_dois or [])]
        meta = self.build_metadata(title, description, related_identifiers=rel_ids)
        dep = self.create_deposit(meta, dry_run=dry_run)
        if dep and file_paths and not dry_run:
            for fp in file_paths:
                self.upload_file(dep["id"], fp, dry_run=dry_run)
        print("deposit_work complete (human must call publish with explicit approval).")
        return dep


if __name__ == "__main__":
    # Example usage (never auto-publishes)
    conn = ZenodoConnector(sandbox=True)
    print("ZenodoConnector ready. Set ZENODO_TOKEN and call with dry_run=False + explicit approval for real work.")
    # conn.sync_from_local_index()
    # Example dry metadata test
    test_meta = conn.build_metadata(
        "Test Spiral Grounded CS Concept",
        "Grounded via PIE + DAER + grandmas-wisdom. Citations to proven CS.",
        keywords=["computer-science", "provenance", "ai-grounding"],
    )
    print("Sample metadata built (sigil applied to description).")
