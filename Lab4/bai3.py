import numpy as np


print("\n=== BÀI 3: PHÂN TÍCH DOANH THU ===")

sales = np.array([
    [120, 150, 130, 140, 160],
    [125, 145, 128, 142, 158],
    [130, 155, 135, 150, 162],
    [135, 160, 140, 152, 168],
    [140, 165, 145, 155, 170],
    [138, 162, 142, 153, 169],
    [145, 170, 150, 160, 175]
])

daily_total = sales.sum(axis=1)
product_total = sales.sum(axis=0)
product_mean = sales.mean(axis=0)

print("Tổng doanh thu từng ngày:", daily_total)
print("Tổng doanh thu từng sản phẩm:", product_total)

best_day = np.argmax(daily_total)
best_product = np.argmax(product_total)
print(f"\nNgày có doanh thu cao nhất: Ngày {best_day+1} ({daily_total[best_day]})")
print(f"Sản phẩm bán chạy nhất: Sản phẩm {best_product+1} ({product_total[best_product]})")

# Tăng 8% cho sản phẩm 2 và 5
new_sales = sales.astype(float).copy()
new_sales[:, [1, 4]] *= 1.08

before = sales.sum()
after = new_sales.sum()
print(f"\nTổng doanh thu trước điều chỉnh: {before}")
print(f"Tổng doanh thu sau điều chỉnh: {after:.0f} (tăng {after-before:.0f})")

# Ngày có doanh thu > trung bình
high_days = np.where(daily_total > daily_total.mean())[0] + 1
print("Các ngày có doanh thu cao hơn trung bình:", high_days)

# Sản phẩm ổn định nhất
stable = np.argmin(sales.std(axis=0))
print(f"Sản phẩm có độ ổn định cao nhất (std nhỏ nhất): Sản phẩm {stable+1}")

print("\nNhận xét:")
print("Sản phẩm 2 và 5 có tiềm năng tăng trưởng tốt khi chỉ cần tăng 8% đã")
print("làm tổng doanh thu tăng đáng kể. Nên ưu tiên đẩy mạnh bán sản phẩm 2")
print("và 5 vì doanh thu cao và có khả năng mở rộng.")