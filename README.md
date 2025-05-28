# RNM-GA Calibration Library

Library for Automatic Calibration of Ranked Nodes in Bayesian Networks using Genetic Algorithms

This library provides the full implementation of a method for calibrating Bayesian Networks using the **Ranked Nodes Method (RNM)**. It automates the search for optimal configurations (aggregation function, weights, and variance) using a **Genetic Algorithm (GA)** to minimize the **Brier Score** based on expert-elicited scenarios.

---

## 📦 Installation

Clone the repository and install required dependencies:

```bash
pip install numpy scikit-learn matplotlib pgmpy
📚 Library Structure

rankedbn/
├── functions/                   # Aggregation and transformation functions (WMEAN, WMIN, etc.)
│   ├── __init__.py              # Maps function names to implementations
│   └── mixture.py               # Applies TNormal transformation
├── genetic/
│   └── genetic_algorithm.py     # Genetic Algorithm logic and API
├── evaluation/
│   ├── evaluator.py             # Evaluation and CPT CSV export
│   └── scenarios.py             # Expert scenarios (TPN1–TPN5)
├── utils/
│   └── loader.py                # Loads repository of continuous samples
├── example/
│   └── run_example.py           # Example script that runs full calibration and evaluation
├── repository.json              # Continuous samples for each linguistic state
🚀 Usage
You can use this as a Python library in your own code, or run the example to test everything.

▶️ 1. Import as a Library

from genetic.genetic_algorithm import run_ga_optimization
from functions import functions
from utils.loader import load_repository
from evaluation.scenarios import TPN3

repository = load_repository("repository.json")
melhor_ind = run_ga_optimization(
    expert_data=TPN3,
    repository=repository,
    tam_pop=50,
    max_gen=10,
    taxa_mutacao=0.1
)
▶️ 2. Run the Complete Example
To execute the full pipeline (GA + Evaluation + CSV export):

python -m example.run_example
This will:

Search for the best configuration (function, weights, variance)

Print per-scenario probabilities and Brier Scores

Export results to:

resultados_ag.csv (AG trace)

TPN3_melhor_config.csv (final CPT based on best config)

📊 Expert Scenarios
The evaluation/scenarios.py file includes sample data used for validation:

TPN1 to TPN5 — each list includes parent states + expected distributions.

These are used as targets during optimization.

📌 Repository Input
Ensure the file repository.json is present. It contains pre-generated continuous samples (VL, L, M, H, VH) required by the aggregation functions and the TNormal transformation.

📄 License and Citation
This library is released under the GNU General Public License v3.0.
