import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
steps = np.random.choice([-1, 1], size=100)
walk = np.cumsum(steps)

print("10 vị trí đầu tiên:", walk[:10])
print("Vị trí cuối cùng:", walk[-1])
print("Vị trí lớn nhất:", np.max(walk))
print("Vị trí nhỏ nhất:", np.min(walk))

# Vẽ đồ thị
plt.plot(walk)
plt.title("Random Walk 1 chiều")
plt.xlabel("Bước")
plt.ylabel("Vị trí")
plt.grid(True)
plt.show()