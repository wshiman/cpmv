import json
import os

def load_filter_and_transfer_data(source_json_path, target_json_path, frame_threshold):

    with open(source_json_path, 'r', encoding='utf-8') as f:
        source_data = json.load(f)

    if os.path.exists(target_json_path):
        with open(target_json_path, 'r', encoding='utf-8') as f:
            target_data = json.load(f)
    else:
        target_data = []

    # 筛选frames数量大于10的数据
    remaining_data = []
    for entry in source_data:
        frames = entry['image']  
        if len(frames) > frame_threshold:
            target_data.append(entry)  
        else:
            remaining_data.append(entry) 


    with open(source_json_path, 'w', encoding='utf-8') as f:
        json.dump(remaining_data, f, ensure_ascii=False, indent=4)


    with open(target_json_path, 'w', encoding='utf-8') as f:
        json.dump(target_data, f, ensure_ascii=False, indent=4)


load_filter_and_transfer_data(
    '/root/cpmv2_6/result_cpmv2_6/processed_train.json',
    '/root/cpmv2_6/result_cpmv2_6/processed_eval.json',
    frame_threshold=10
)
