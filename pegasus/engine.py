import math
import numpy as np
import graphviz



class Variable:
    """
    The Variable class is the fundamental data type used in pegasus
    The Variable class is used for *most* arithmetic operations in the library
    The Variable class also implements the auto grad engine
    """
    def __init__(self, data, name, _op=None, _parents=[]):
        self.data = data
        self.name = name
        self._op = _op
        self._grad= 0
        self._parents = _parents
        self._backward = lambda: None
    
    # add function to print the value in the variable
    def __repr__(self) -> str:
        return f"Variable: {self.data}"
    
    
    # override the add function to allow mathematical operations
    def __add__(self, other):
        other = other if isinstance(other, Variable) else Variable(other, name=str(other))
        value = self.data + other.data 
        out = Variable(value, name=f"({self.name}+{other.name})", _op="+", _parents=(self, other))
        def backward():
            self._grad += (1 * out._grad)
            other._grad += (1 * out._grad)
            self._backward()
            other._backward()
            
        out._backward = backward
        return out
    
    # override the multiplication special function to allow mathematical operations
    def __mul__(self, other):
        other = other if isinstance(other, Variable) else Variable(other, name=str(other))
        value = self.data * other.data
        out = Variable(value, name=f"({self.name}*{other.name})", _op="*", _parents=(self, other))
        def backward():
            self._grad += (out._grad * other.data)
            other._grad += (out._grad * self.data)
            self._backward()
            other._backward()
            
        out._backward = backward
        return out
    
    
    # override the subtraction special function to allow mathematical operations
    def __sub__(self, other):
        other = other if isinstance(other, Variable) else Variable(other, str(other))
        return self + (other * -1)
    
    
    # override the power function to allow mathematical operations
    def __pow__(self, other):
        other = other if isinstance(other, Variable) else Variable(other,str(other))
        value = self.data ** other.data
        out = Variable(value, name=f"{self.name}**{other.name}", _op="**", _parents=(self, other))
        def backward():
            # using power rule
            self._grad += out._grad * (other.data*(self.data**(other.data-1)))
            self._backward()

        out._backward = backward
        return out
    
    # override the divide function to allow mathematical operations
    def __truediv__(self, other):
            other = other if isinstance(other, Variable) else Variable(other,str(other))
            return self.data/ other.data
    
    # overrid the floored division to allow mathmatical operations
    def __floordiv__(self, other):
        other = other if isinstance(other, Variable) else Variable(other)
        result = self.data / other.data
        return Variable(result, (self, other), "/")
        
    # this is tanh funciton which is used to add non linearity in or deep learning network from the neuron, it is a form of activation function
    def tanh(self):
        sigmoid = np.tanh(self.data)
        out = Variable(sigmoid, name=f"tanh({self.name})", _op="tanh", _parents=(self,))
        def backward():
            self._grad += ((1 - (sigmoid**2)) * out._grad)
            self._backward()
            
        out._backward = backward
        return out
    
    # perform back progragation through all the nodes using recursion
    def backward(self):
        self._grad = 1
        self._backward()
        
        
    # private function to draw the computational graph using recursion
    def _draw(self, graph):
        for parent in self._parents:
            parentName = f"{parent.name}|{parent.data}|{parent._grad}"
            nodeName = f"{self.name}|{self.data}|{self._grad}"
            graph.edge(parentName, nodeName)
            parent._draw(graph)
    
    # public function to draw the computational graph
    def draw(self):
        g = graphviz.Digraph('G', filename=f'{self.name}.gv')
        self._draw(g)
        g.view()
        
    # set the gradients of all nodes to zero    
    def zero_grad(self):
        self._grad = 0
        for parent in self._parents:
            parent.zero_grad()
        