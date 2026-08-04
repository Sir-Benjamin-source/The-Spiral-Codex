# λ_A / λ_P — Dual Damping Rates

**Six-Clause Meta-Standard Entry**  
**Version**: 0.1 (Locked 2026-08-04)  
**Status**: Accepted for use in the parallel differential examination form

---

### 1. Name & Symbol
Dual Damping Rates — \( \lambda_A \), \( \lambda_P \)  
Range: \( \lambda_A > 0 \), \( \lambda_P > 0 \), with the constraint \( \lambda_A + \lambda_P = \Lambda \) (a declared positive constant).

### 2. Operational Definition
\( \lambda_A \) and \( \lambda_P \) are coupled positive rates that govern how strongly the system responds to the coherence residual \( (1 - C) \).  
- \( \lambda_A \) scales the braking (or acceleration) applied to the actionable trajectory.  
- \( \lambda_P \) scales the corresponding term on the paradox-containment trajectory.  

Their sum is held constant so that the overall responsiveness of the examination system remains bounded; only the *balance* between constructive advance and residual holding is free to vary.

### 3. Measurement Protocol
These are not measured from text in the same way as \( S, G, E, C \). They are **declared control parameters** of the examination process itself.

1. Choose a global responsiveness constant \( \Lambda > 0 \) (default recommendation: \( \Lambda = 0.30 \)).  
2. Choose a balance parameter \( \gamma \in [0, 1] \) that sets the relative weight:  
   \( \lambda_A = \gamma \cdot \Lambda \),  
   \( \lambda_P = (1 - \gamma) \cdot \Lambda \).  
3. Default starting balance: \( \gamma = 0.5 \) (equal damping).  
4. Record both values and the chosen \( \Lambda \) whenever the parallel differential form is run.  
5. Optional adaptive rule (future): allow \( \gamma \) to shift slowly according to observed \( A - P \) or residual-stability feedback, while still preserving \( \lambda_A + \lambda_P = \Lambda \).

### 4. Reference / Classical Anchor
- Dual or complementary damping / learning-rate schedules in adaptive control and dynamical systems.  
- Regularization balance parameters in classical statistical learning (e.g., the relative weight between different penalty terms).  
- Gain scheduling and complementary filtering in classical control theory.  
- Temperature or exploration–exploitation balance parameters in classical search and optimization.

### 5. Failure Modes & Edge Cases
- \( \Lambda = 0 \) → both trajectories become pure product terms; the coherence residual exerts no influence (system loses its corrective mechanism).  
- One rate set to zero while the other absorbs all of \( \Lambda \) → the system collapses to a single trajectory.  
- Unbounded or independently drifting rates → the examination dynamics can become unstable; the sum constraint is mandatory.  
- Extremely large \( \Lambda \) → the coherence residual dominates and can suppress both \( S \cdot G \cdot E \) and \( S \cdot (1-G) \cdot E \) terms.

### 6. Relation Rules
- \( \lambda_A \) and \( \lambda_P \) appear only in the residual terms of the parallel differential form.  
- They do not alter the definitions of \( S, G, E, \) or \( C \).  
- Changing the balance \( \gamma \) shifts emphasis between actionable claim generation and paradox containment without changing the overall gain of the system.  
- In future embodiment, \( \Lambda \) or \( \gamma \) may be linked to residual-stability targets from qsc-stabilization, but any such link is an empirical control choice, not part of the definitional standard.

---

*Locked under the six-clause meta-standard. Ready for embodiment.*
