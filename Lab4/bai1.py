import numpy as np

print("=== BÀI 1: PHÂN TÍCH ĐIỂM HỌC PHẦN ===")

# dữ liệu điểm: [chuyên cần, giữa kỳ, thực hành, cuối kỳ]
scores = np.array([
    [8.0, 7.5, 8.5, 7.0],
    [6.5, 6.0, 7.0, 6.5],
    [9.0, 8.5, 9.0, 8.5],
    [5.0, 5.5, 6.0, 5.5],
    [7.5, 7.0, 8.0, 7.5],
    [4.5, 5.0, 5.5, 5.0],
    [8.5, 9.0, 8.0, 9.0],
    [6.0, 6.5, 6.0, 6.5],
    [7.0, 7.5, 7.0, 8.0],
    [9.5, 9.0, 9.5, 9.0]
])

# xem nhanh cấu trúc mảng
print("Shape:", scores.shape)
print("ndim :", scores.ndim)
print("dtype:", scores.dtype)

# trọng số từng cột điểm
weights = np.array([0.1, 0.2, 0.3, 0.4])

# tính điểm tổng kết (nhân ma trận)
final_score = scores @ weights

# hàm xếp loại theo thang điểm
def classify(score):
    if score >= 9.0: return 'A'
    elif score >= 8.0: return 'B'
    elif score >= 7.0: return 'C'
    elif score >= 5.0: return 'D'
    else: return 'F'

# áp dụng xếp loại cho toàn bộ sinh viên
ranks = np.array([classify(s) for s in final_score])

print("\nĐiểm tổng kết:", np.round(final_score, 2))
print("Xếp loại:", ranks)

# tìm vị trí sv cao nhất / thấp nhất
max_idx = np.argmax(final_score)
min_idx = np.argmin(final_score)

print(f"\nSinh viên có điểm cao nhất: SV{max_idx+1} ({final_score[max_idx]:.2f})")
print(f"Sinh viên có điểm thấp nhất: SV{min_idx+1} ({final_score[min_idx]:.2f})")

# lọc sv >= 7.0
good_students = np.where(final_score >= 7.0)[0]
print("Sinh viên đạt từ 7.0 trở lên:", good_students + 1)

# check sv có ít nhất 1 môn < 5
low_component = np.any(scores < 5.0, axis=1)
print("Sinh viên có điểm thành phần dưới 5.0:", np.where(low_component)[0] + 1)

# lấy top 3 sv điểm cao nhất
top3_idx = np.argsort(final_score)[::-1][:3]
print("Top 3 sinh viên:", top3_idx + 1)

# chuẩn hóa z-score cho cột cuối kỳ
z_final = (scores[:, 3] - scores[:, 3].mean()) / scores[:, 3].std()
print("\nZ-score điểm cuối kỳ:", np.round(z_final, 3))

# nhận xét nhanh
print("\nNhận xét:")
print("Lớp có sự phân hóa rõ rệt về điểm số. Có 2 sinh viên xuất sắc (trên 9.0),")
print("nhưng cũng có sinh viên yếu với điểm thành phần dưới 5.0. Điểm cuối kỳ")
print("có độ lệch chuẩn khá cao, cho thấy mức độ phân hóa mạnh ở phần thi cuối.")
