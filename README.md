## Pegasus deep learning micro library built with only python and numpy v1

![alt text](./images/pegasus.jpg)

## Introduction
With the steady growth in the development of deep learning, there have been several layers of abstraction which have been built to simplify communication of ideas and speed up development. But the cost is that fewer people understand the foundational building blocks of deep learning models : the perceptron. This project is intended to be a *very simple* decomposition of a deep learning library, meant only for pedantic purposes. 

## Structure
The project is divided into the engine and the neural network. The Neural Network section implements the Neuron, Layers and other parts needed to implement a deep neural network. While the Engine section is an implementation of an auto grad engine which uses chain rule to calculate the cascading gradients of variables on the network.

There is also an implmentation to create a computational graph from a node that is exported as a file and viewed. 


## Special Notes
Currently, the only activation function used is tanh and the only loss function used is squared error loss. It also currently uses only stochastic gradient descent for its optimizations. Also please note: pegasus is only for pedantic purposes, i.e if you use it with more than 300 training examples, it WILL definately blow up your system :)