# Kinematic-Control-And-Trajectory-Engine
> **An industrial-grade, modular control architecture for Multi-DOF planar robotic systems featuring deterministic geometric inverse kinematics, real-time signal conditioning, and linear trajectory planning.**

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-green.svg)
![Robotics](https://img.shields.io/badge/field-Robotics%20%26%20Automation-orange.svg)
![Math](https://img.shields.io/badge/framework-NumPy-lightblue.svg)

---

## 🛠️ System Architecture

This repository contains a modular Python framework designed to simulate, filter, and plan motions for robotic arms. Real-world robotics application development requires abstracting hardware away from high-level coordinate transformations. This project demonstrates an end-to-end simulation pipeline:

```mermaid
graph TD
    A[Trajectory Planner: Target Coordinates] --> B[Simulated Real-World Noise Layer]
    B --> C[Signal Conditioning: Exponential Moving Average Filter]
    C -->|Clean Coordinates| D[Kinematics Core: Geometric Inverse Kinematics Solver]
    D --> E[Actuator Output: Discrete Joint Angles J1 & J2]


![System Execution Logs](image_f1c2aa.png)
