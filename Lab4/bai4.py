import numpy as np


print("\n=== BÀI 4: QUẢN LÝ TỒN KHO ===")

stock = np.array([35, 8, 12, 5, 40, 18, 7, 22, 9, 15])
min_stock = np.array([20, 15, 15, 10, 25, 20, 12, 18, 12, 15])

need_import = np.maximum(min_stock - stock, 0)

print("Số lượng cần nhập:", need_import)

status = np.where(stock < min_stock, "Thiếu hàng", "Đủ hàng")
print("Trạng thái:", status)

price = np.array([30, 25, 28, 22, 35, 20, 18, 24, 19, 21])

cost = need_import * price
total_cost = cost.sum()
print(f"Tổng chi phí nhập hàng: {total_cost:,} VND")

top3 = np.argsort(need_import)[::-1][:3]
print("3 mặt hàng thiếu nhiều nhất:", top3 + 1)

# Giới hạn tối đa 20 đơn vị
limited_need = np.clip(need_import, 0, 20)
limited_cost = (limited_need * price).sum()

print(f"Tổng chi phí sau khi giới hạn 20 đơn vị: {limited_cost:,} VND")

print("\nNhận xét:")
print("Kho hàng đang thiếu khá nghiêm trọng ở một số mặt hàng (đặc biệt mặt hàng 4 và 7).")
print("Tổng chi phí cần nhập khoảng 1.5 triệu VND. Nên ưu tiên nhập ngay các mặt hàng")
print("thiếu nhiều nhất để tránh gián đoạn kinh doanh.")