import akshare as ak
import pandas as pd

# 获取可转债数据
bond_data = ak.bond_cov_comparison()

# 将最新价列转换为数值类型
bond_data['转债最新价'] = pd.to_numeric(bond_data['转债最新价'], errors='coerce')

# 筛除最新价不是数字的行
bond_data = bond_data.dropna(subset=['转债最新价'])

numeric_columns = ['正股涨跌幅', '转债涨跌幅', '转股溢价率']
bond_data[numeric_columns] = bond_data[numeric_columns].astype(float)

# 计算活跃度指标
bond_data['活跃度得分'] = bond_data['正股涨跌幅'] * bond_data['转债涨跌幅'] / bond_data['转股溢价率']

# 根据活跃度得分降序排序
sorted_bonds = bond_data.sort_values(by='活跃度得分', ascending=False)

# 筛选前N个活跃的可转债
top_n = 10
active_bonds = sorted_bonds.head(top_n)



# 打印筛选结果
print("Top {} 活跃的可转债：".format(top_n))
print(active_bonds.iloc[:, [1, 2, 3, 4,8,11,20]])


