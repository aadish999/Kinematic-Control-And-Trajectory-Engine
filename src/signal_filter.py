import numpy as np

class IndustrialSignalFilter:
    def __init__(self, alpha=0.2):
        """Alpha controls smoothing: Lower = smoother but introduces slight lag."""
        self.alpha = alpha
        self.previous_estimate = None

    def exponential_moving_average(self, raw_measurement):
        """Filters high-frequency sensor noise using an EMA algorithm."""
        if self.previous_estimate is None:
            self.previous_estimate = raw_measurement
            return raw_measurement

        # Filtering math: S_t = α * Y_t + (1 - α) * S_{t-1}
        filtered_value = (self.alpha * raw_measurement) + ((1 - self.alpha) * self.previous_estimate)
        self.previous_estimate = filtered_value
        return filtered_value

    def batch_filter(self, data_array):
        """Processes an entire telemetry block at once."""
        filtered_data = []
        self.previous_estimate = None
        for data in data_array:
            filtered_data.append(self.exponential_moving_average(data))
        return np.array(filtered_data)
