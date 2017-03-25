import matplotlib.pyplot as plt
from PID import PID

x0 = 20

x = []

u = []

t = []

e = []
delta_t = 0.01

t_max = 100

t_current = 0.0

i = 0

pid = PID(
    proportional=0.1,
    integral=0.1,
    differential=0.01,
    period=delta_t,
    min_value=-100.0,
    max_value=100.0,
    formula='pid'
)

while t_current < t_max:
    t.append(t_current)
    x.append(
        20
        #t_current
    )
    e.append(x0 - x[i])
    u.append(pid.next_value(e[i]))
    i += 1
    t_current += delta_t

plt.plot(t, u)
plt.xlabel('t')
plt.ylabel('u(t)')
plt.show()
