print("\n=== BÀI 5: TỔNG HỢP SO SÁNH ===")

print("1. Dữ liệu ở hai bài giống nhau ở điểm nào về cấu trúc?")
print("   → Đều là ma trận 2 chiều (2D ndarray) của NumPy.")

print("\n2. Phép toán NumPy nào được dùng ở cả hai bài?")
print("   → .sum(), .mean(), np.where(), np.argmax(), np.argsort(), boolean indexing.")

print("\n3. Bài nào sử dụng boolean indexing nhiều hơn? Vì sao?")
print("   → Bài 2 (Chuyên cần) sử dụng nhiều hơn vì cần lọc nhiều điều kiện phức tạp:")
print("     (tỉ lệ < 75%, vắng liên tiếp, đi đầy đủ...).")

print("\n4. Lợi ích của xử lý vector hóa so với dùng vòng lặp là gì?")
print("   → Nhanh hơn rất nhiều (hàng trăm lần), code ngắn gọn, dễ đọc và ít lỗi hơn.")

print("\n5. Nếu số lượng dữ liệu tăng gấp 100 lần, NumPy hỗ trợ gì?")
print("   → NumPy vẫn xử lý rất tốt nhờ tối ưu C backend, broadcasting, và có thể")
print("     kết hợp với Pandas hoặc Dask khi dữ liệu cực lớn.")