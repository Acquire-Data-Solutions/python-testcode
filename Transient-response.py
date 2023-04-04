import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# tau * dy2/dt2 + 2*zeta*tau*dy/dt + y = Kp*u
Kp = 1.5  # gain
tau = 1.0  # time constant
zeta = 0.09  # damping factor
theta = 0.0  # no time delay
du = 1.0  # change in u
N = 500
# (1) Transfer Function
num = [Kp]
den = [tau ** 2, 2 * zeta * tau, 1]
sys1 = signal.TransferFunction(num, den)
t1, y1 = signal.step2(sys1, N=N)

print(len(t1))

tau1 = 0.001  # time constant
zeta1 = 0.90  # damping factor
theta = 0.0  # no time delay
du1 = 1.0  # change in u

den1 = [tau1 ** 2, 0.5 * zeta1 * tau1, 1]
sys2 = signal.TransferFunction(num, den1)
t1, y2 = signal.step2(sys2, N=N)

plt.figure(1)
linewidth = 1
plt.plot(t1, y1 * du, linewidth=linewidth, label='PID Controller')
plt.plot(t1, y2 * du1, linewidth=linewidth, label='ML Controller')
y_ss = Kp * du
plt.plot([0, max(t1)], [y_ss, y_ss], 'k:')
plt.xlabel('Time')
plt.ylabel('Response (y)')
plt.legend(loc='best')
plt.show()
#
# from numpy import min, max
# import numpy as np
# from scipy import linspace
# from scipy.signal import lti, step, impulse
#
# # making transfer function
# # example from Ogata Modern Control Engineering
# # 4th edition, International Edition page 307
#
# # num and den, can be list or numpy array type
# num = [6.3223, 18, 12.811]
# den = [1, 6, 11.3223, 18, 12.811]
#
# tf = lti(num, den)
#
# # get t = time, s = unit-step response
# tme, s = step(tf)
#
# # recalculate t and s to get smooth plot
# t, sp = step(tf, T=np.linspace(min(tme), tme[-1], 5000))
# t, i = step(tf, T=np.linspace(min(t), tme[-1], 5000))
#
# # get i = impulse
# # t, i = impulse(tf, T=np.linspace(min(t), tme[-1], 5000))
#
# from matplotlib import pyplot as plt
#
# plt.plot(t, sp, t, i)
# plt.title('Transient-Response Analysis')
# plt.xlabel('Time(sec)')
# plt.ylabel('Amplitude')
# plt.hlines(1, min(t), max(t), colors='r')
# plt.hlines(0, min(t), max(t))
# plt.xlim(xmax=max(t))
# plt.legend(('Unit-Step Response', 'Unit-Impulse Response'), loc=0)
# plt.grid()
# plt.show()
