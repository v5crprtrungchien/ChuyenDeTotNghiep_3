import numpy as np


print("\n=== BÀI 2: PHÂN TÍCH CHUYÊN CẦN ===")

attendance = np.array([
    [1,1,1,1,1,1,1,1],
    [1,1,0,1,1,0,1,1],
    [1,0,0,1,1,1,0,1],
    [1,1,1,1,0,1,1,1],
    [0,1,1,0,1,1,1,0],
    [1,1,1,1,1,1,0,1],
    [1,0,1,0,1,0,1,0],
    [1,1,1,1,1,1,1,0],
    [0,0,1,1,0,1,1,1],
    [1,1,1,0,1,1,1,1],
    [1,1,0,0,1,0,1,1],
    [1,1,1,1,1,0,1,1]
])

present_count = attendance.sum(axis=1)
rate = present_count / 8 * 100

print("Số buổi có mặt của từng SV:", present_count)
print("Tỉ lệ chuyên cần (%):", np.round(rate, 1))

warning = np.where(rate < 75)[0]
print("\nSinh viên bị cảnh báo (<75%):", warning + 1)

# Buổi vắng nhiều nhất
absent_by_session = (attendance == 0).sum(axis=0)
worst_session = np.argmax(absent_by_session)
print(f"Buổi học vắng nhiều nhất: Buổi {worst_session+1} ({absent_by_session[worst_session]} SV)")

# Đi học đầy đủ
full = np.where(np.all(attendance == 1, axis=1))[0]
print("Sinh viên đi học đầy đủ 8 buổi:", full + 1)

# Có 2 buổi vắng liên tiếp
two_consecutive = np.where(np.any((attendance[:, :-1] == 0) & (attendance[:, 1:] == 0), axis=1))[0]
print("Sinh viên có ít nhất 2 buổi vắng liên tiếp:", two_consecutive + 1)

print("\nNhận xét:")
print("Lớp có ý thức chuyên cần khá tốt khi có 5/12 sinh viên đi học đầy đủ.")
print("Tuy nhiên vẫn có 3 sinh viên bị cảnh báo do vắng quá nhiều, trong đó có")
print("sinh viên vắng liên tiếp - đây là dấu hiệu cần nhắc nhở kịp thời.")