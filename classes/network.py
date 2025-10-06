import numpy

class Node:
    def __init__(self, weight, bias):
        self.weight = weight
        self.bias = bias

class Layer:
    def __init__(self, layer_type: str):
        self.nodes = []
        self.layer_type = layer_type

    def get_weighted_sum(self):
        pass

class Network:
    def __init(self, network_type: str):
        self.layers = []
        self.network_type = network_type
    
    def get_result(self):
        pass