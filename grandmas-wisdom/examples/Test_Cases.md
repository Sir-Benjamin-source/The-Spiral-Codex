# Grandma’s Wisdom — Test Cases

This document contains five diverse test cases used to validate and refine the Grandma’s Wisdom authentication framework and Bullshit Meter.

Each case includes:
- Citation and claim
- Overall Bullshit Meter score
- Detailed sub-score breakdown (2–4 sentences each)
- Expanded “What is tenable” and “What is not tenable” paragraphs
- Notes on why the case is useful for testing

---

## Test Case 1: Strong, Well-Supported Use

**Citation:**  
Smith, J. et al. (2022). “Large-scale meta-analysis of cognitive training effects on executive function in healthy adults.” *Psychological Science*, 33(4), 512–530.

**Claim being supported:**  
“Cognitive training produces reliable improvements in executive function among healthy adults.”

**Bullshit Meter: 2.4 / 10**

**Breakdown:**

- **Evidential Support from Related Works: 2.2**  
  The source benefits from strong and consistent support across multiple high-quality studies and meta-analyses. Effect sizes are modest but replicable. The rating would improve further with additional large-scale replications; it would decline if major contradictory findings emerged in well-powered studies.

- **Logical Consistency & Internal Validity: 2.5**  
  The paper’s methodology and conclusions are internally coherent. The supported claim stays close to what the data actually demonstrate without requiring unsupported extrapolation.

- **Contextual Fidelity / Misattribution Risk: 2.1**  
  The source is represented fairly. Key limitations around effect size magnitude and variability across training protocols are implicitly respected by the measured language of the claim.

- **Provenance & Traceability Strength: 1.9**  
  Bibliographic information is complete and stable. Linkweaver shows strong, high-quality connections to related empirical work.

- **Overclaim / Scope Violation Risk: 2.9**  
  The claim remains within reasonable bounds and does not assert broad real-world transfer or permanent cognitive enhancement.

**What is tenable:**  
Cognitive training interventions produce small-to-moderate, statistically detectable improvements on measures of executive function in healthy adult samples under controlled conditions. These effects appear across multiple studies with varying training protocols, though the practical significance of the improvements remains modest. The source provides a reliable foundation for claiming directional benefits in lab-based or structured training settings. Claims limited to these parameters can be made with reasonable confidence when properly qualified.

**What is not tenable:**  
Assertions that cognitive training produces large, durable, or broadly transferable improvements in real-world cognitive performance or daily functioning. The source does not provide strong evidence for far transfer to untrained tasks or long-term maintenance of gains after training ends. Strong policy or clinical recommendations based solely on this work would exceed its evidential scope.

**Notes:** Clean, high-quality example of appropriate source usage. Good baseline for what strong performance looks like.

---

## Test Case 2: Moderate Paper with Scope Overreach

**Citation:**  
Chen, L. et al. (2023). “Effects of a 6-week mindfulness app on stress reduction in university students.” *Journal of American College Health*.

**Claim being supported:**  
“Mindfulness apps are an effective tool for reducing stress in the general population.”

**Bullshit Meter: 6.7 / 10**

**Breakdown:**

- **Evidential Support from Related Works: 6.2**  
  There is moderate support from related studies on mindfulness interventions, but effect sizes are often small and heterogeneous. Few high-quality studies specifically examine app-based delivery in non-student populations. The score would improve with additional studies showing consistent effects outside student samples.

- **Logical Consistency & Internal Validity: 5.4**  
  The source study itself is reasonably designed, but the leap from a short-term student intervention to broad population-level effectiveness is weakly supported by the paper’s own data.

- **Contextual Fidelity / Misattribution Risk: 8.1**  
  Significant contextual stripping has occurred. The original study’s narrow sample (university students), short duration (6 weeks), and self-report measures are not reflected in the generalized claim.

- **Provenance & Traceability Strength: 4.3**  
  Basic citation details are traceable, but Linkweaver shows relatively sparse high-quality connections supporting the broader claim.

- **Overclaim / Scope Violation Risk: 8.6**  
  The claim substantially exceeds the source’s actual scope and evidence base.

**What is tenable:**  
A 6-week mindfulness app intervention was associated with reductions in self-reported stress among university students in this specific study. The intervention showed measurable effects within a controlled academic setting over a relatively short timeframe. The source can reasonably support narrow claims about short-term stress reduction in student populations when properly scoped.

**What is not tenable:**  
Broad assertions that mindfulness apps are generally effective tools for reducing stress across the general adult population or in non-academic settings. The source provides no direct evidence for long-term effects, clinical populations, or non-student demographics. Using this single study to justify widespread adoption or policy recommendations would significantly overreach its evidential foundation.

**Notes:** Classic and common failure mode. Excellent for testing scope violation detection.

---

## Test Case 3: Prestige Bias + Weak Evidential Support

**Citation:**  
Williams, R. et al. (from a top-10 university, published in *Nature Human Behaviour*, 2021). “Neural correlates of decision-making under uncertainty.”

**Claim being supported:**  
“This study proves that human decision-making under uncertainty follows a specific computational model proposed by the authors.”

**Bullshit Meter: 7.8 / 10**

**Breakdown:**

- **Evidential Support from Related Works: 8.2**  
  While influential, the model faces competition from other frameworks and has not achieved broad consensus. Direct replications remain limited. The high rating reflects the gap between the paper’s prestige and the actual density of supporting work.

- **Logical Consistency & Internal Validity: 6.5**  
  The paper presents a coherent model within its experimental paradigm, but the leap to a general “proof” of human decision-making is not supported by the study’s scope.

- **Contextual Fidelity / Misattribution Risk: 7.1**  
  The claim significantly inflates the source’s conclusions. The original paper is more measured about the model’s applicability.

- **Provenance & Traceability Strength: 4.0**  
  Strong bibliographic provenance exists, but Linkweaver reveals that prestige appears to be substituting for dense evidential support.

- **Overclaim / Scope Violation Risk: 8.9**  
  The claim treats a single influential study as definitive proof, which exceeds what the work and surrounding literature can currently sustain.

**What is tenable:**  
The paper presents a plausible and internally consistent computational model of decision-making under uncertainty supported by the authors’ specific experimental tasks. It contributes one valuable perspective within an active and contested research area. The work can reasonably be cited as an important theoretical contribution when properly contextualized.

**What is not tenable:**  
Treating this single study as definitive proof that human decision-making under uncertainty follows the proposed model in general. The source does not establish broad empirical consensus, nor does it rule out competing models. Strong claims of proof or universal applicability based on this work alone would misrepresent both the paper and the current state of the field.

**Notes:** Important test case for detecting prestige bias and over-reliance on high-impact single studies.

---

## Test Case 4: Foundational Paper Overused

**Citation:**  
Kahneman, D. & Tversky, A. (1979). “Prospect Theory: An Analysis of Decision under Risk.” *Econometrica*, 47(2), 263–291.

**Claim being supported:**  
“Prospect Theory is the definitive model of human decision-making under risk and should be used as the foundation for all economic policy modeling.”

**Bullshit Meter: 8.3 / 10**

**Breakdown:**

- **Evidential Support from Related Works: 7.6**  
  Prospect Theory remains highly influential, but the field has developed many competing models and significant critiques since 1979. The rating reflects the gap between the paper’s historical importance and its current status as one model among several.

- **Logical Consistency & Internal Validity: 5.2**  
  The original paper is internally coherent, but using it as the sole foundation for “all economic policy modeling” is not supported by its scope or subsequent literature.

- **Contextual Fidelity / Misattribution Risk: 8.9**  
  Major overgeneralization. The claim transforms a foundational descriptive model into a prescriptive universal framework.

- **Provenance & Traceability Strength: 2.1**  
  Excellent provenance exists for the source itself, but Linkweaver shows that its dominance in policy discussions often exceeds current evidential density.

- **Overclaim / Scope Violation Risk: 9.4**  
  The claim dramatically exceeds what even a foundational paper can reasonably support decades later.

**What is tenable:**  
Prospect Theory remains one of the most important and empirically supported descriptive models of decision-making under risk. It has generated decades of productive research and continues to explain important behavioral patterns better than classical expected utility theory in many contexts. The work can be cited as a major theoretical contribution when properly situated within the broader literature on decision-making.

**What is not tenable:**  
Treating Prospect Theory as the definitive or complete model of human decision-making under risk, or as a sufficient foundation for all economic policy modeling. The source does not establish universal applicability, nor has it gone unchallenged by subsequent theoretical and empirical work. Policy recommendations presented as flowing directly and exclusively from this single model would significantly overstate its current standing in the field.

**Notes:** Strong negative example of how even excellent foundational papers can be misused when treated as settled science.

---

## Test Case 5: Independent Work with Growing Conceptual Support

**Citation:**  
Patel, R. (2021). “A resonance-based model of semantic integration in long-form reasoning.” *Preprint* (low citation count, independent researcher).

**Claim being supported:**  
“Semantic integration during extended reasoning follows predictable resonance patterns that can be modeled computationally.”

**Bullshit Meter: 4.7 / 10**

**Breakdown:**

- **Evidential Support from Related Works: 5.9**  
  Direct empirical support remains limited due to the work’s relative newness and independent origin. However, conceptual resonance with existing work in cognitive science, computational linguistics, and neural network research is growing. The score has potential to improve as more related studies appear.

- **Logical Consistency & Internal Validity: 4.3**  
  The proposed model is internally coherent and logically developed, though it would benefit from additional empirical testing.

- **Contextual Fidelity / Misattribution Risk: 3.8**  
  The source is represented reasonably. The claim stays close to what the model proposes without major distortion.

- **Provenance & Traceability Strength: 6.2**  
  Basic citation information is traceable. Linkweaver shows emerging conceptual connections even with relatively low direct citation counts.

- **Overclaim / Scope Violation Risk: 4.1**  
  The claim is appropriately modest given the current state of evidence.

**What is tenable:**  
A resonance-based computational model of semantic integration during extended reasoning has been proposed and shows conceptual alignment with multiple existing lines of research in cognitive science and computational modeling. The framework offers a coherent and testable approach to understanding how meaning is integrated over longer reasoning chains. It can reasonably be cited as a promising theoretical contribution from an independent researcher when properly scoped as an early-stage model.

**What is not tenable:**  
Strong empirical claims about the model’s superiority, broad validation, or immediate applicability to real-world reasoning systems. The source currently lacks the volume of direct supporting studies needed to support confident assertions of general effectiveness. Using this work to justify major theoretical or practical commitments without additional supporting evidence would exceed its current evidential foundation.

**Notes:** Important test case for the longitudinal philosophy. This type of work should be able to improve its score over time as conceptual support grows.

---

**Summary**

These five cases cover a useful range of scenarios:
- Clean high-quality usage
- Common scope violations
- Prestige bias
- Overuse of foundational papers
- Independent / emerging work

They are ready to be added to the `examples/` folder. Let me know if you want any adjustments before you commit them.