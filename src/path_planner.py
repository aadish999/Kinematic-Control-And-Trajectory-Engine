import numpy as np

class TrajectoryPlanner:
    @staticmethod
    def generate_linear_path(start_coord, end_coord, steps=50):
        """Generates a highly discrete point-to-point path matrix for smooth motion profiles."""
        start_coord = np.array(start_coord)
        end_coord = np.array(end_coord)
        
        # Generates linearly spaced steps between coordinates
        path = np.linspace(start_coord, end_coord, num=steps)
        return path
