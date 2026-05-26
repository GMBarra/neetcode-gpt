import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        sigma_element_value = 1 / (1 + np.exp(-z))
        return np.round(sigma_element_value, 5)
        pass

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        relu_value = np.maximum(0,z)
        return np.round(relu_value,5)
        pass
