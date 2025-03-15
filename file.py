import water as w
import SONAR as s
import matplotlib.pyplot as plt

water = w.Water(T=2)
[s_left,s_right] = water.gen_echo(r=800, phi=30)

sonar = s.SONAR(T=2)
[r,phi,df] = sonar.detector(s_left, s_right)

print(r,phi,df)

plt.plot(s_left)
plt.plot(s_right)
plt.show()
