import numpy as np

class RoboticKinematics:
    def __init__(self, l1, l2):
        """Initializes robot link lengths."""
        self.l1 = l1
        self.l2 = l2

    def forward_kinematics(self, theta1, theta2):
        """Computes End-Effector (X, Y) from joint angles (Radians)."""
        x = self.l1 * np.cos(theta1) + self.l2 * np.cos(theta1 + theta2)
        y = self.l1 * np.sin(theta1) + self.l2 * np.sin(theta1 + theta2)
        return np.array([x, y])

    def inverse_kinematics(self, target_x, target_y):
        """Computes required joint angles to reach a target coordinate."""
        # Law of Cosines to find Theta 2
        cos_theta2 = (target_x**2 + target_y**2 - self.l1**2 - self.l2**2) / (2 * self.l1 * self.l2)
        
        # Out of workspace safety boundary check
        if np.abs(cos_theta2) > 1.0:
            raise ValueError("Target coordinate is outside the robot's physical workspace!")

        theta2 = np.arccos(cos_theta2)
        
        # Calculate Theta 1
        theta1 = np.arctan2(target_y, target_x) - np.arctan2(
            (self.l2 * np.sin(theta2)), (self.l1 + self.l2 * np.cos(theta2))
        )
        
        return np.degrees(theta1), np.degrees(theta2)
