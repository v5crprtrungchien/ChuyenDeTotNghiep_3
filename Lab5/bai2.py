import numpy as np

scores = np.array([
    [7.5, 8.0, 6.5, 9.0],
    [6.0, 7.0, 7.5, 8.0],
    [8.5, 9.0, 8.0, 9.5],
    [5.5, 6.0, 6.5, 7.0],
    [9.0, 8.5, 9.5, 8.0]
])

mean_col = np.mean(scores, axis=0)
std_col = np.std(scores, axis=0)
z_scores = (scores - mean_col) / std_col
print("Ma trận Z-score (làm tròn 2 chữ số):")
print(np.round(z_scores, 2))
print("TB các cột sau chuẩn hóa:", np.mean(z_scores, axis=0))

min_col = np.min(scores, axis=0)
max_col = np.max(scores, axis=0)
normalized_01 = (scores - min_col) / (max_col - min_col)
print("\nMa trận chuẩn hóa [0,1] (làm tròn 2 chữ số):")
print(np.round(normalized_01, 2))