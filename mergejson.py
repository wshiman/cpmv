import json

def merge_json_files(falling_json_path, lying_json_path, squatting_json_path,output_json_path, remaining_json_path):

    with open(falling_json_path, 'r', encoding='utf-8') as f:
        falling_data = json.load(f)


    with open(lying_json_path, 'r', encoding='utf-8') as f:
        lying_data = json.load(f)


    with open(squatting_json_path,'r',encoding='utf-8') as f:
        squatting_data =json.load(f)

    # 提取数据
    filtered_falling = [entry for entry in falling_data if int(entry["video_path"].split('/')[-1].split('.')[0]) < 80]
    remaining_falling = [entry for entry in falling_data if int(entry["video_path"].split('/')[-1].split('.')[0]) >= 80]

    filtered_lying = [entry for entry in lying_data if int(entry["video_path"].split('/')[-1].split('.')[0]) < 70]
    remaining_lying = [entry for entry in lying_data if int(entry["video_path"].split('/')[-1].split('.')[0]) >= 70]

    filtered_squatting = [entry for entry in squatting_data if int(entry["video_path"].split('/')[-1].split('.')[0]) < 70]
    remaining_squatting = [entry for entry in squatting_data if int(entry["video_path"].split('/')[-1].split('.')[0]) >= 70]
    # 合并数据
    merged_data = filtered_falling + filtered_lying + filtered_squatting


    with open(output_json_path, 'w', encoding='utf-8') as f:
        json.dump(merged_data, f, indent=4)


    remaining_data = remaining_falling + remaining_lying + remaining_squatting
    with open(remaining_json_path, 'w', encoding='utf-8') as f:
        json.dump(remaining_data, f, indent=4)

# 设置文件路径
falling_json_path = '/root/cpmv2_6/result_cpmv2_6/processed_falling.json'
lying_json_path = '/root/cpmv2_6/result_cpmv2_6/processed_lying.json'
squatting_json_path = '/root/cpmv2_6/result_cpmv2_6/processed_squatting.json'
output_json_path = '/root/cpmv2_6/result_cpmv2_6/merged_processed.json'
remaining_json_path = '/root/cpmv2_6/result_cpmv2_6/remaining_processed.json'


merge_json_files(falling_json_path, lying_json_path,squatting_json_path, output_json_path, remaining_json_path)
