# shoes.py
# Basic skeleton for Shoes, Harnesses, and Disciplines
# Part of the Spiral Codex operational methodology

from typing import Dict, List, Optional, Callable
from dataclasses import dataclass, field

@dataclass
class Harness:
    """Primary layer - Core operational template"""
    name: str
    description: str
    execute: Callable
    metadata: Dict = field(default_factory=dict)

    def run(self, *args, **kwargs):
        return self.execute(*args, **kwargs)


@dataclass
class Shoe:
    """Secondary layer - Modular overlay that modifies a Harness"""
    name: str
    description: str
    applies_to: List[str]  # Which Harnesses this Shoe is compatible with
    modify: Callable  # Function that modifies behavior or output

    def apply(self, harness: Harness, *args, **kwargs):
        if harness.name not in self.applies_to and "any" not in self.applies_to:
            raise ValueError(f"Shoe '{self.name}' is not compatible with Harness '{harness.name}'")
        return self.modify(harness, *args, **kwargs)


@dataclass
class Discipline:
    """Tertiary layer - Self-contained specialized practice"""
    name: str
    description: str
    harness: Harness
    shoes: List[Shoe] = field(default_factory=list)
    metadata: Dict = field(default_factory=dict)

    def execute(self, *args, **kwargs):
        result = self.harness.run(*args, **kwargs)
        for shoe in self.shoes:
            result = shoe.apply(self.harness, result, *args, **kwargs)
        return result


# Example usage

def base_research_pipeline(topic: str):
    print(f"Running base research on: {topic}")
    return {"topic": topic, "findings": "Raw data collected"}


def world_examination_shoe(harness: Harness, previous_result: dict, *args, **kwargs):
    print("Applying World Examination Shoe...")
    previous_result["examined"] = True
    previous_result["levels"] = ["World", "Region", "National", "Local", "Personal"]
    return previous_result


# Define a Harness
research_harness = Harness(
    name="ResearchPipeline",
    description="Basic multi-source research loop",
    execute=base_research_pipeline
)

# Define a Shoe
world_exam_shoe = Shoe(
    name="WorldExamination",
    description="Examines topics across multiple geographic and personal levels",
    applies_to=["ResearchPipeline", "any"],
    modify=world_examination_shoe
)

# Create a Discipline
world_research_discipline = Discipline(
    name="WorldResearchDiscipline",
    description="Research with structured world examination",
    harness=research_harness,
    shoes=[world_exam_shoe]
)

# Usage
if __name__ == "__main__":
    result = world_research_discipline.execute("Current state of AI agent infrastructure")
    print(result)