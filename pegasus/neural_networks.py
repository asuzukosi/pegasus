from pegasus.engine import Variable
import numpy as np

# Implement A neuron class 
class Neuron:
    def __init__(self, name, num_inputs):
        self.name = name
        self.w = np.array([Variable(np.random.uniform(-1, 1), name=f"N({self.name})W({i})") for i in range(num_inputs)]) # this will be a numpy vector
        self.b = Variable(np.random.uniform(-1, 1), name=f"N({name})B") # this will be a scalar value
        
    # perform computation on a single neuron
    def __call__(self, inputs):
        out = np.dot(self.w, inputs) + self.b
        out = out.tanh()
        return out
    
    # get the parameters of a neuron which include the weights and the biases
    def parameters(self):
        parameters = []
        parameters.extend(self.w)
        parameters.append(self.b)
        return parameters
    
# Implement A layer class
class Layer:
    def __init__(self, name, n_inputs, n_outputs):
        self.n_inputs = n_inputs
        self.n_outputs = n_outputs
        self.name = name
        self.neurons = np.array([Neuron(f"L({name})n{i}", self.n_inputs) for i in range(self.n_outputs)])
    
    # perform inference on a single layer
    def __call__(self, input):
        out = np.array([neuron(input) for neuron in self.neurons])
        return out
    
    # get the parameters of a single layer which include the parameters of the nuerons
    def parameters(self):
        parameters = []
        for neuron in self.neurons:
            parameters.extend(neuron.parameters())
        return parameters
    

# Implement a multilayer perceptronn
class MultiLayerPerceptron:
    def __init__(self, num_inputs):
        self.layers = []
        self.num_inputs = num_inputs
        
    # add layers to MLP
    def add_layer(self, num_outputs):
        layer = Layer(name=str(len(self.layers)), n_inputs=self.num_inputs, n_outputs=num_outputs)
        self.layers.append(layer)
        self.num_inputs = num_outputs
        
    # perform inference on the MLP
    def __call__(self, inputs):
        if len(self.layers) == 0:
            return inputs

        for layer in self.layers:
            inputs = layer(inputs)
        return inputs if len(inputs) > 1 else inputs[0]
    
    # get all parameters on the MLP
    def parameters(self):
        parameters = []
        for layer in self.layers:
            parameters.extend(layer.parameters())
        return parameters
    
    