import numpy as np


class Neural():

    #values from -1 to 1 
    self.snaptic = 2 * np.random.random((3,1)) - 1


def sigmoid(self, x):
    #weighted sum of the inputs and creates a normal between 0 and 1
    return 1 / (1 + np.exp(-x))

def derivative(self, x)
    #derivative of the signmoid
    return x * (1-x)

def train_mind(self, _inputs, _outputs, _iterations)
    for i in range(_iterations)
        #passing network
        output = self.think(_inputs)

        #error calculation 
        error = _ouputs - output
        #transpose - gradiet (derivative)
        adjust = np.dot(_inputs.T, error * self.derivative(output))

        #make adjustments
        self.synaptic += adjust


def think(self, inputs)
    #Actual Thinking
    output = self.sigmoid(np.dot(inputs, self.synaptic))
    return output



if__name__ == "main":





