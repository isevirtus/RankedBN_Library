from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import numpy as np



# ================================
# Class Bayesian Network
# ================================
class BNetwork:
    def __init__(self):
        self.model = BayesianNetwork()
        self.nodes = {}
        self.evidence = {}

    def createNode(self, node_id, name, outcomes):
        self.nodes[node_id] = {"name": name, "outcomes": outcomes}
        self.model.add_node(node_id)

    def addEdge(self, parent_id, child_id):
        self.model.add_edge(parent_id, child_id)

    def setNodeCPD(self, node_id, cpt_values):
        parent_ids = list(self.model.get_parents(node_id))
        parent_cards = [len(self.nodes[p]["outcomes"]) for p in parent_ids]
        var_card = len(self.nodes[node_id]["outcomes"])
        cpt_values = np.array(cpt_values)
        if cpt_values.shape != (var_card, np.prod(parent_cards)):
            raise ValueError(f"Incorrect format for {node_id}. Expected {(var_card, np.prod(parent_cards))}, but received {cpt_values.shape}")
        cpd = TabularCPD(
            variable=node_id,
            variable_card=var_card,
            values=cpt_values.tolist(),
            evidence=parent_ids if parent_ids else None,
            evidence_card=parent_cards if parent_cards else None,
            state_names={node_id: self.nodes[node_id]["outcomes"], **{pid: self.nodes[pid]["outcomes"] for pid in parent_ids}}
        )
        self.model.add_cpds(cpd)

    def updateBeliefs(self):
        self.model.check_model()
        infer = VariableElimination(self.model)
        evidence_dict = self.evidence if self.evidence else {}
        return {
            node_id: infer.query([node_id], evidence=evidence_dict).values.tolist()
            for node_id in self.nodes if node_id not in evidence_dict
        }

    def setEvidence(self, node_id, state_name):
        self.evidence[node_id] = state_name

    def calculateTPN(self, node_id):
        infer = VariableElimination(self.model)
        return infer.query([node_id], evidence=self.evidence).values.tolist()

