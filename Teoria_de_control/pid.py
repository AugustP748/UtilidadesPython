import control as ctrl
import matplotlib.pyplot as plt
import numpy as np

# Define the system to control (transfer function)
num = [1]
den = [1, 5, 6]
system = ctrl.TransferFunction(num, den)

# Create a PID controller
Kp = 2.0  # Proportional gain 
Ki = 1.0  # Integral gain
Kd = 0.5  # Derivative gain
controller = ctrl.TransferFunction([Kd, Kp, Ki], [1, 0])

# Create a closed-loop system
closed_loop_system = ctrl.feedback(controller * system, 1)

# Time vector for simulation
time = np.linspace(0, 10, 1000)

# Step input
t, y = ctrl.step_response(closed_loop_system, time)

# Plot the response
plt.figure()
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('PID Controller Response')
plt.grid(True)
plt.show()
