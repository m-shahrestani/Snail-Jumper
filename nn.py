import numpy as np


class NeuralNetwork:

    def __init__(self, layer_sizes):
        """
        Neural Network initialization.
        Given layer_sizes as an input, you have to design a Fully Connected Neural Network architecture here.
        :param layer_sizes: A list containing neuron numbers in each layers. For example [3, 10, 2] means that there are
        3 neurons in the input layer, 10 neurons in the hidden layer, and 2 neurons in the output layer.
        """
        # TODO (Implement FCNNs architecture here)
        # layer_sizes example: [4, 10, 2]

        self.layer_sizes = layer_sizes

        #  contain the all weights of two layer
        self.weights = []

        #  contain the baiases of two layer
        self.baises = []

        # weight for the first layer
        weight_first_layer = np.random.normal(size=(layer_sizes[1], layer_sizes[0]))
        self.weights.append(weight_first_layer)

        # weight for the second layer
        weight_second_layer = np.random.normal(size=(layer_sizes[2], layer_sizes[1]))
        self.weights.append(weight_second_layer)

        # bias of the first layer
        bais_first_layer = np.zeros((layer_sizes[1], 1))
        # bais_first_layer = np.random.normal(size =(layer_sizes[1], 1))
        self.baises.append(bais_first_layer)

        # bias of the second layer
        bais_second_layer = np.zeros((layer_sizes[2], 1))
        # bais_second_layer = np.random.normal(size= (layer_sizes[2], 1))
        self.baises.append(bais_second_layer)

    def activation(self, x):
        """
        The activation function of our neural network, e.g., Sigmoid, ReLU.
        :param x: Vector of a layer in our network.
        :return: Vector after applying activation function.
        """
        # TODO (Implement activation function here)
        return 1/(1 + np.exp(-x))

    def forward(self, x):
        """
        Receives input vector as a parameter and calculates the output vector based on weights and biases.
        :param x: Input vector which is a numpy array.
        :return: Output vector
        """
        # TODO (Implement forward function here)
        # x example: np.array([[0.1], [0.2], [0.3]])
        hidden_layer = self.activation(self.weights[0] @ x + self.baises[0])

        output_layer = self.activation(self.weights[1] @ hidden_layer + self.baises[1])

        return output_layer
