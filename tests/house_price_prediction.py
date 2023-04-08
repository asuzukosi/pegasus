from sklearn.datasets import fetch_california_housing
import numpy as np
from pegasus.neural_networks import MultiLayerPerceptron
from pegasus.training import Trainer, squared_error_loss, SDG_Optimization
from sklearn.metrics import mean_squared_error

dataset = fetch_california_housing()

# minimize the size of the dataset and convert to numpy array
X = np.array(dataset['data'][:300])
y = np.array(dataset['target'][:300])

# split to training and testing data
X_train = X[:200]
y_train = y[:200]

X_test = X[200:]
y_test = y[200:]

# Create Multilayer perceptron with pegasus
# number of inputs is set to 8 becuase the dataset has 8 features
model = MultiLayerPerceptron(num_inputs=8)
model.add_layer(5)
model.add_layer(5)
model.add_layer(3)
# the last layer should have one output becuase it is 
# the output layer and we are solving a regression 
# problem which has only one output
model.add_layer(1) 

# check performace of the model before training
predictions = []
for test in X_test:
    prediction = model(test)
    predictions.append(prediction)

error = mean_squared_error(predictions, y_test)
print("The error before training is: ", error)

trainer = Trainer(model, squared_error_loss, SDG_Optimization, 0.01)
trainer(15, X_train, y_train)


predictions = []
for test in X_test:
    prediction = model(test)
    predictions.append(prediction)

error = mean_squared_error(predictions, y_test)
print("The error after training is: ", error)

