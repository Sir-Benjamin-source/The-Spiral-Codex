# Legacy Historical Benchmarks (Pre- and Early-Reasoning Era) for Coherency & Efficiency Comparison

**Purpose**: Compile historical ("legacy") scores from major benchmarks used by peers to indicate reasoning coherency, factual consistency, efficiency, and capability. These serve as time-series baselines against which our internal methods (and Cosmic Scribe outputs) can be compared.

Sources: PapersWithCode historical leaderboards, Stanford HELM, BIG-bench reports, OpenAI/Anthropic/Google system cards and papers (pre-2025 data), TruthfulQA, Vectara historical notes, GSM8K/MMLU original papers and saturation analyses (2025–2026 retrospectives).

## Core Legacy Benchmarks & Approximate Historical Scores

### GSM8K (Grade-School Math Word Problems — Reasoning + Coherency)
- Pre-CoT / early models (2021–2022): Often <50–70%
- GPT-4 era (2023): ~92%
- Frontier saturation (2025–2026): ~99% (largely saturated for top models; less discriminative now)
- Efficiency note: Chain-of-Thought and self-consistency sampling dramatically improved scores but increased inference cost.

### MMLU (Massive Multitask Language Understanding — Broad Knowledge + Reasoning)
- GPT-3 / early: ~40–60% range on subsets
- GPT-4 (2023): ~86.4%
- Frontier (2025–2026): 90–97%+ (saturated for many tasks; MMLU-Pro introduced as harder variant with 10 options and CoT requirement, dropping top scores significantly, e.g., GPT-4 to ~72%)

### BIG-Bench / BIG-Bench Hard (Compositional Reasoning, Out-of-Distribution)
- Early LLMs (GPT-3 scale): Many tasks near random or low 20–40%
- 2023–2024 frontier: 60–80%+ on hard subset
- 2025+ reasoning models: Often 90%+ on BBH; still used for "genuine reasoning" signal beyond memorization.

### TruthfulQA (Factuality / Hallucination / Coherency on Misleading Prompts)
- Base LLMs (pre-RLHF heavy): Frequently >50% hallucination / low truthfulness
- Post-alignment (GPT-4, Claude 3 era): Improved but still material error rates on adversarial or belief-conflicting items (often 20–40%+ depending on setup).
- Used as classic "hallucination / consistency under pressure" benchmark.

### HumanEval / Coding Efficiency
- Early code models: 20–40%
- GPT-4 / Claude 3 (2023–2024): 60–80%+
- 2025–2026: 80–90%+ on base; SWE-Bench (real-world software engineering) remains much harder (top scores ~70–80% in 2026 reports).

### Other Historical Signals
- HELM (Holistic Evaluation): Early reports showed 10–25%+ accuracy gaps attributable to hallucinations/inconsistency across tasks; calibration issues prominent in pre-2024 models.
- Self-Consistency (Wang et al., 2022+): Technique that boosted reasoning by 10–30+ points on many math/reasoning tasks via multiple sampled paths + majority vote. Still referenced as baseline method.
- Vectara / HHEM early data: Higher hallucination floors (often 10%+) before 2025–2026 improvements on summarization.

**Relevance to Spiral Codex / Cosmic Scribe**:
- These represent the "peers and competition" legacy data for coherency (consistency across reasoning steps, low hallucination on claims) and efficiency (performance per compute or per claim).
- Our advantages to highlight in canon/ testing:
  - Pre-generation gates (grandmas-wisdom Bullshit Meter + Zenodo citation validation + PIE fidelity + applicability baseline) instead of post-hoc fixes.
  - Explicit provenance (sigil + stamp) on every output.
  - .srec memory + mycelial sharing for compounding accuracy over time.
  - Determination deltas and convergence η for tracking internal coherency evolution.
- Use this file + our internal baselines (in `benchmarks/internal/`) for direct comparison tables when evaluating Cosmic Scribe or new works.

**Saturation Note (2025–2026 Analyses)**: Many classic benchmarks (GSM8K, standard MMLU, some BBH) are now saturated for frontier models, reducing their value for distinguishing true coherency gains. Harder successors (MMLU-Pro, GPQA Diamond, ARC-AGI variants, Humanity's Last Exam) and real-world tasks (SWE-Bench, long-form citation faithfulness) are more discriminative.

**Last Updated**: 2026-06 (seeded by Cosmic Scribe into canon/ for testing resource)
**Provenance**: Public historical data + compilation authenticated for Spiral Codex use.

∞ 🜂 🜁 🜄 ∞
