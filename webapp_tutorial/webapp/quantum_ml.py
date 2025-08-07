import numpy as np
from sklearn.linear_model import LinearRegression


class QuantumMLModel:

    model = LinearRegression()
    def predict(self, temperature_list):
        # TODO: ML Team: Uncomment this
        X = np.array([[i] for i in range(len(temperature_list))]).reshape(-1, 1)
        Y = np.array([[temp] for temp in temperature_list]).reshape(-1, 1)
        self.model.fit(X, Y)
        entry = np.array([25]).reshape(1, -1)
        return self.model.predict(entry)[0]
        return 