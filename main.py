import numpy as np
from src.kinematics import RoboticKinematics
from src.signal_filter import IndustrialSignalFilter
from src.path_planner import TrajectoryPlanner

def main():
    print("Initializing Robotic Control Engine...")
    
    # 1. Initialize physical parameters (Link 1 = 10 units, Link 2 = 10 units)
    arm = RoboticKinematics(l1=10, l2=10)
    filter_engine = IndustrialSignalFilter(alpha=0.25)
    
    # 2. Plan a trajectory path from Point A to Point B
    start_pos = [5, 5]
    end_pos = [12, 8]
    planned_path = TrajectoryPlanner.generate_linear_path(start_pos, end_pos, steps=5)
    
    print("\n--- Executing Autonomous Path Execution with Actuator Telemetry ---")
    
    for idx, point in enumerate(planned_path):
        # Simulate high-frequency noise from joint encoders/hardware feedback
        simulated_noise = np.random.normal(0, 0.2, size=2)
        noisy_point = point + simulated_noise
        
        # Run noise filtering
        filtered_x = filter_engine.exponential_moving_average(noisy_point[0])
        filtered_y = filter_engine.exponential_moving_average(noisy_point[1])
        
        # Calculate calculated inverse kinematics for actual motor execution
        try:
            joint_1, joint_2 = arm.inverse_kinematics(filtered_x, filtered_y)
            print(f"Step {idx+1} | Target: {point} | Actuator Joint Angles -> J1: {joint_1:.2f}° , J2: {joint_2:.2f}°")
        except ValueError as e:
            print(f"Step {idx+1} | execution blocked: {e}")

if __name__ == "__main__":
    main()
