import numpy as np

scores = np.array([
    [7.5, 8.0, 6.5, 9.0],
    [6.0, 7.0, 7.5, 8.0],
    [8.5, 9.0, 8.0, 9.5],
    [5.5, 6.0, 6.5, 7.0],
    [9.0, 8.5, 9.5, 8.0]
])

print("1. Ma trận điểm:\n", scores)
print("2. Điểm trung bình toàn bộ:", np.mean(scores))
print("3. Điểm trung bình từng sinh viên:", np.mean(scores, axis=1))
print("4. Điểm trung bình từng môn:", np.mean(scores, axis=0))
print("5. Điểm cao nhất:", np.max(scores))
print("6. Điểm thấp nhất:", np.min(scores))
print("7. Độ lệch chuẩn từng môn:", np.std(scores, axis=0))

avg_students = np.mean(scores, axis=1)
best_student = np.argmax(avg_students)
print("Sinh viên có điểm TB cao nhất là vị trí:", best_student)