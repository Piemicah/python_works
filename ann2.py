import numpy as np
import numpy.random as ran


class Layer:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.01 * ran.randn(n_neurons, n_inputs)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights.T) + self.biases


class Relu:
    def activate(self, inputs):
        self.output = inputs * (inputs > 0)


class Softmax:
    def activate(self, inputs):
        ex_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        self.output = ex_values / np.sum(ex_values, axis=1, keepdims=True)


class Loss:
    def calculate(self, output, y):
        sample_loses = self.forward(output, y)
        data_loss = np.mean(sample_loses)

        return data_loss


class LossCategoricalCrossEntropy(Loss):
    def forward(self, y_predict, y_true):
        # Number of samples
        samples = len(y_predict)
        # Clip data to prevent division by 0
        # Clip both sides to not drag mean towards any value
        y_pred_clipped = np.clip(y_predict, 1e-7, 1 - 1e-7)
        # Probabilities for target values -
        # only if categorical labels

        # check the dimension of the data
        dim = len(y_true.shape)
        if dim == 1:
            correct_confidences = y_pred_clipped[range(samples), y_true]

        # Mask values - only for one-hot encoded labels
        elif dim == 2:
            correct_confidences = np.sum(y_pred_clipped * y_true, axis=1)

        # Losses
        negative_log_likelihoods = -np.log(correct_confidences)
        return negative_log_likelihoods


class OneHot:
    def convert(self, x):
        return 1 * (x == np.max(x, axis=1, keepdims=True))


x = np.array([[3, 1, 4], [6, -2, 1.5], [5, 6, 1], [2.9, -0.86, 2]])

layer1 = Layer(3, 3)

layer1.forward(x)

activation1 = Relu()
activation1.activate(layer1.output)

layer2 = Layer(3, 3)
activation2 = Softmax()
activation2.activate(activation1.output)

print(layer1.output)
print(activation1.output)
print(activation2.output)


class_targets = OneHot().convert(activation2.output)
print("class_target:", class_targets)

loss_function = LossCategoricalCrossEntropy()

loss = loss_function.calculate(activation2.output, class_targets)
print("loss =", loss)
