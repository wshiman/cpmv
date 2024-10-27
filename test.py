# import json
# import os

# # 源文件路径
# source_file_path = '/root/cpmv2_6/result_cpmv2_6/processed_eval.json'
# # 目标文件路径
# target_file_path = '/root/cpmv2_6/result_cpmv2_6/processed_train.json'

# # 加载源 JSON 数据
# with open(source_file_path, 'r', encoding='utf-8') as f:
#     source_data = json.load(f)

# # 加载目标 JSON 数据，如果文件不存在，则初始化为空列表
# if os.path.exists(target_file_path):
#     with open(target_file_path, 'r', encoding='utf-8') as f:
#         target_data = json.load(f)
# else:
#     target_data = []

# # 筛选 images 数量小于 10 的条目
# to_remove = []
# for entry in source_data:
#     if len(entry.get('image', {})) < 10:
#         to_remove.append(entry)

# # 从源数据中移除这些条目
# source_data = [entry for entry in source_data if entry not in to_remove]

# # 将移除的条目追加到目标文件
# target_data.extend(to_remove)

# # 保存更新后的目标文件
# with open(target_file_path, 'w', encoding='utf-8') as f:
#     json.dump(target_data, f, ensure_ascii=False, indent=4)

# print(len(source_data))
# print(len(target_data))
# print("处理完成，已将 images 数量小于 10 的数据追加到目标文件。")


import json
import os

# def transfer_samples(source_json_path, target_json_path, categories, sample_size):
#     # 读取源文件
#     with open(source_json_path, 'r', encoding='utf-8') as f:
#         source_data = json.load(f)

#     # 读取目标文件
#     with open(target_json_path, 'r', encoding='utf-8') as f:
#         target_data = json.load(f)

#     # 创建一个存储转移数据的列表
#     transferred_samples = []

#     for category in categories:
#         # 从目标数据中筛选出指定类别的数据
#         category_samples = [entry for entry in target_data if category in entry['video_path']]

#         # 随机抽取指定数量的样本
#         samples_to_transfer = category_samples[:sample_size]

#         # 将样本添加到转移列表和源数据中
#         transferred_samples.extend(samples_to_transfer)
#         source_data.extend(samples_to_transfer)

#         # 从目标数据中移除已转移的样本
#         target_data = [entry for entry in target_data if entry not in samples_to_transfer]

#     # 将更新后的数据写回源文件
#     with open(source_json_path, 'w', encoding='utf-8') as f:
#         json.dump(source_data, f, ensure_ascii=False, indent=4)
#         print(len(source_data))
#     # 将更新后的数据写回目标文件
#     with open(target_json_path, 'w', encoding='utf-8') as f:
#         json.dump(target_data, f, ensure_ascii=False, indent=4)
#         print(len(target_data))

# # 调用函数
# transfer_samples(
#     '/root/cpmv2_6/result_cpmv2_6/processed_eval.json',
#     '/root/cpmv2_6/result_cpmv2_6/processed_train.json',
#     categories=['falling', 'lying', 'squatting'],
#     sample_size=10
# )

# 源文件路径
source_file_path = '/root/cpmv2_6/result_cpmv2_6/processed_eval.json'
# 目标文件路径
target_file_path = '/root/cpmv2_6/result_cpmv2_6/processed_train.json'

# 加载源 JSON 数据
with open(source_file_path, 'r', encoding='utf-8') as f:
    source_data = json.load(f)
    print(len(source_data))

with open(target_file_path, 'r', encoding='utf-8') as f:
    target_data = json.load(f)
    print(len(target_data))