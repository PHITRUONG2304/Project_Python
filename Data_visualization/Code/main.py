"""Pandas là một thư viện Python cung cấp các cấu trúc dữ liệu nhanh, mạnh mẽ, linh hoạt và mang hàm ý."""
from hashlib import new
import pandas as pd
"""Numpy (Numeric Python): là một thư viện toán học phổ biến và mạnh mẽ của Python."""
import numpy as np
"""Matplotlib là một thư viện rất hữu ích của Python dùng để vẽ đồ thị"""
import matplotlib.pyplot as plt
"""Seaborn là một thư viện Python được sử dụng để tạo biểu đồ trực quan hóa cho tập dữ liệu"""
import seaborn as sb


"""Load dataset"""
data = pd.read_csv('../data/cereal.csv')
# print(data)

"""Irrelevant filter"""
i_fields = ['shelf', 'weight', 'cups', 'rating']
new_cereal_df = data.drop(i_fields, axis=1)
# print(new_cereal_df.head())

"""Correlation data"""
cereal_corr = new_cereal_df.corr()
# print(cereal_corr)

"""ones_like can build a matrix of booleans with the same shape as your data"""
ones_corr = np.ones_like(cereal_corr, dtype=bool)
# print(ones_arr)

"""triu function: return only upper triangle matrix"""
mask = np.triu(ones_corr)
# print(mask)

"""draw a graph"""
# sb.heatmap(data=cereal_corr, mask=mask)

adjust_mask = mask[1:, :-1]
adjust_cereal_corr = cereal_corr.iloc[1:, :-1]

fig, ax = plt.subplots(figsize=(10,8))
"""fmt: format, cmap: color map, annot: display factor respectively"""
sb.heatmap(data=adjust_cereal_corr, mask=adjust_mask, annot=True, fmt=".2f", cmap="Blues", vmin=-1, vmax=1, linewidths=0.5)

# upper label in figure map
yticks = [i.upper() for i in adjust_cereal_corr.index]
xticks = [i.upper() for i in adjust_cereal_corr.columns]

ax.set_yticklabels(yticks, rotation=0)
ax.set_xticklabels(xticks, rotation=0)

title = 'CORRELATION MATRIX\nSAMPLE CEREALS COMPOSITION\n'

ax.set_title(title, loc="left", fontsize=18)
plt.show()

