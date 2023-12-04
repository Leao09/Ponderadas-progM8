import numpy as np

y_array = [np.array([0,0]),np.array([0,1]),np.array([1,0]),np.array([1,1])]

class Perceptron:
    def __init__(self, threshold=0.5, learning_rate=0.1, iterations=100):
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.bias = 0
        self.weights = None

    def activation(self, value):
        return 1 if value >= self.threshold else 0

    def predict(self, input_data):
        if len(input_data) != len(self.weights):
            raise Exception("Input dimension is invalid")
        value = self.bias + np.dot(input_data, self.weights)
        return self.activation(value)

    def train(self, inputs, results):
        self.weights = np.zeros(len(inputs[0]))

        for _ in range(self.iterations):
            for i in range(len(inputs)):
                prediction = self.predict(inputs[i])
                error = results[i] - prediction
                self.weights += self.learning_rate * error * inputs[i]
                self.bias += self.learning_rate * error


perceptron = Perceptron(threshold=1, learning_rate=0.1, iterations=100)

print("and_gate")
perceptron.train(np.array([[0,0],[0,1],[1,0],[1,1]]), np.array([0,0,0,1]))
for i in y_array:
    resp = perceptron.predict(i)    
    print(resp)

print("or_gate")
perceptron.train(np.array([[0,0],[0,1],[1,0],[1,1]]), np.array([0,1,1,1]))
for i in y_array:
    resp = perceptron.predict(i)    
    print(resp)
    
print("Nand_gate")
perceptron.train(np.array([[0,0],[0,1],[1,0],[1,1]]), np.array([1,1,1,0]))
for i in y_array:
    resp = perceptron.predict(i)    
    print(resp)

print("Xor_gate")
perceptron.train(np.array([[0,0],[0,1],[1,0],[1,1]]), np.array([0,1,1,0]))
for i in y_array:
    resp = perceptron.predict(i)    
    print(resp)
