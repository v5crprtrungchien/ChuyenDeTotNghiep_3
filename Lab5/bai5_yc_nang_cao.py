import numpy as np

steps_many = np.random.choice([-1, 1], size=(100, 100))
walks_many = np.cumsum(steps_many, axis=1)

final_positions = walks_many[:, -1]
print("Số walk kết thúc dương:", np.sum(final_positions > 0))

hit_10 = np.any(np.abs(walks_many) >= 10, axis=1)
print("Số walk chạm ngưỡng |10|:", np.sum(hit_10))