import pandas as pd

# 读取Excel表格
df = pd.read_excel('/Users/kuiqwang/Desktop/demo.xlsx')

# 获取列一的数据并转换为字符串
column_data = df['模块名称'].fillna('').astype(str).tolist()

# 创建一个Excel写入器
writer = pd.ExcelWriter('output2.xlsx', engine='xlsxwriter')

# 将每个分组输出到单独的表中
for group_name in set(column_data):
    # 替换无效字符为有效字符
    valid_sheet_name = str(group_name).replace('/', '_')  # 替换斜杠为下划线或其他合适的字符
    group_df = df[df['模块名称'] == group_name]
    group_df.to_excel(writer, sheet_name=valid_sheet_name, index=False)

# 保存Excel文件
writer.save()
