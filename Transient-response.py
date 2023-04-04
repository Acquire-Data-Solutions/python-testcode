import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# tau * dy2/dt2 + 2*zeta*tau*dy/dt + y = Kp*u
Kp = 1.5  # gain
tau = 1.0  # time constant
zeta = 0.09  # damping factor
theta = 0.0  # no time delay
du = 1.0  # change in u
N = 5000

tEnd = 90
time = np.arange(0, tEnd, 0.1)
# (1) Transfer Function
num = [Kp]
den = [tau ** 2, 1.3 * zeta * tau, 1]
sys1 = signal.TransferFunction(num, den)
t1, y1 = signal.step2(sys1, T=time, N=N)

tau1 = 1.0  # time constant
zeta1 = 0.30  # damping factor
theta = 0.0  # no time delay
du1 = 1.0  # change in u

den1 = [tau1 ** 2, 1 * zeta1 * tau1, 1]
sys2 = signal.TransferFunction(num, den1)
t1, y2 = signal.step2(sys2, T=time, N=N)

plt.figure(1)
linewidth = 1.5
plt.plot(time, y1 * du, linewidth=linewidth, label='PID Controller')
plt.plot(time, y2 * du1, linewidth=linewidth, label='ML Controller')
y_ss = Kp * du
plt.plot([0, max(t1)], [y_ss, y_ss], 'k:')
plt.xlabel('Steps/time')
plt.ylabel('Response (y)')
plt.legend(loc='best')
plt.show()
