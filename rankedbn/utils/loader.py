# loader.py
import json
import numpy as np

def load_repository(path='repository.json'):
    """
    Load and convert the repository of samples from JSON.
    """
    with open(path, 'r', encoding='utf-8') as f:
        repo = json.load(f)
        for state in repo:
            repo[state]['amostras'] = np.array(repo[state]['samples'])
        return repo