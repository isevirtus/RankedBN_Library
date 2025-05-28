# scenarios.py
TPN1 = [
    {"AT": "VL", "AC": "VH", "AE": "VL", "AE_expert": [0, 1, 0, 0, 0]},
    {"AT": "VH", "AC": "VL", "AE": "VL", "AE_expert": [0, 1, 0, 0, 0]},
    {"AT": "VL", "AC": "VL", "AE": "VH", "AE_expert": [0, 1, 0, 0, 0]},
    {"AT": "VL", "AC": "VH", "AE": "VH", "AE_expert": [0, 0, 1, 0, 0]},
    {"AT": "VH", "AC": "VL", "AE": "VH", "AE_expert": [0, 1, 0, 0, 0]},
    {"AT": "VH", "AC": "VH", "AE": "VL", "AE_expert": [0, 0, 1, 0, 0]}
]
TPN2 = [
    {"AT": "VL", "AC": "VH", "AE": "VL", "AE_expert": [0, 1, 0, 0, 0]},
    {"AT": "VH", "AC": "VL", "AE": "VL", "AE_expert": [0, 1, 0, 0, 0]},
    {"AT": "VL", "AC": "VL", "AE": "VH", "AE_expert": [0, 1, 0, 0, 0]},
    {"AT": "VL", "AC": "VH", "AE": "VH", "AE_expert": [0, 0, 1, 0, 0]},
    {"AT": "VH", "AC": "VL", "AE": "VH", "AE_expert": [0, 0, 1, 0, 0]},
    {"AT": "VH", "AC": "VH", "AE": "VL", "AE_expert": [0, 0, 1, 0, 0]}
]
TPN3 = [
    {"AT": "VL", "AC": "VH", "AE": "VL", "AE_expert": [0, 1, 0, 0, 0]},
    {"AT": "VH", "AC": "VL", "AE": "VL", "AE_expert": [1, 0, 0, 0, 0]},
    {"AT": "VL", "AC": "VL", "AE": "VH", "AE_expert": [1, 0, 0, 0, 0]},
    {"AT": "VL", "AC": "VH", "AE": "VH", "AE_expert": [0, 1, 0, 0, 0]},
    {"AT": "VH", "AC": "VL", "AE": "VH", "AE_expert": [0, 1, 0, 0, 0]},
    {"AT": "VH", "AC": "VH", "AE": "VL", "AE_expert": [0, 1, 0, 0, 0]}
]
TPN4 = [
    {"AT": "VL", "AC": "VH", "AE_expert": [0, 1, 0, 0, 0]},
    {"AT": "VH", "AC": "VL", "AE_expert": [0, 1, 0, 0, 0]},
    {"AT": "VL", "AC": "M",  "AE_expert": [0, 1, 0, 0, 0]},
    {"AT": "M",  "AC": "VL", "AE_expert": [0, 1, 0, 0, 0]}
]
TPN5 = [
    {"AT": "VL", "AC": "VH", "AE_expert": [0, 0, 0, 1, 0]},
    {"AT": "VH", "AC": "VL", "AE_expert": [0, 1, 0, 0, 0]},
    {"AT": "VL", "AC": "M",  "AE_expert": [0, 1, 0, 0, 0]},
    {"AT": "M",  "AC": "VL", "AE_expert": [0, 1, 0, 0, 0]}
]
AT_AC_AE = [
                               
    {"AT": "VL", "AC": "VH", "AE_expert": [0.274, 0.323, 0.274, 0.081, 0.048]},
    {"AT": "VH", "AC": "VL", "AE_expert": [0.172, 0.259, 0.345, 0.172, 0.052]},
    {"AT": "VL",  "AC": "VL",  "AE_expert": [0.333, 0.333, 0.283, 0.050, 0.0]},
    {"AT": "VH",  "AC": "VH", "AE_expert": [0.0, 0.055, 0.273, 0.309, 0.364]},
    {"AT": "VL",  "AC": "M", "AE_expert": [0.2, 0.3, 0.34, 0.1, 0.06]},
    {"AT": "M",   "AC": "VL", "AE_expert": [0.357, 0.357, 0.179, 0.107, 0.0]},
]