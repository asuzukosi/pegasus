from pegasus.engine import Variable
from typing import List
import numpy as np

# implementation of the Squared error loss
def squared_error_loss(target, predictions):
    out = predictions - target
    out = out**2
    return out.sum()



def SDG_Optimization(lr: float, parameters: List[Variable]):
    # peform gradient descent by subtracting the gradient multiplied by the learing rate from the data
    for parameter in parameters:
        parameter.data -= float(lr) * float(parameter._grad)
        


class Trainer:
    def __init__(self, model, loss_function, optimization, learning_rate):
        self.model = model
        self.loss_function = loss_function
        self.optimization = optimization
        self.learning_rate = learning_rate
        
    def _calculate_predictions(self, inputs):
        predictions = np.array([self.model(input) for input in inputs])
        return predictions
        
    def __call__(self, epochs, inputs, targets):
        for epoch in range(epochs):
            predictions = self._calculate_predictions(inputs)
            loss:Variable = self.loss_function(targets, predictions)
            loss.zero_grad()
            loss.backward()
            self.optimization(self.learning_rate, self.model.parameters())
            print(f"At epoch {epoch} loss = {loss.data}")