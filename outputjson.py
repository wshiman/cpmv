import json
import os


input_json_path = '/root/cpmv2_6/result_cpmv2_6/modified_squatting.json'
output_json_path = '/root/cpmv2_6/result_cpmv2_6/processed_squatting.json'
frames_base_path = '/root/autodl-tmp/frames/'


with open(input_json_path, 'r') as f:
    data = json.load(f)

new_data = []

for index, entry in enumerate(data):
    video_path = entry["video_path"]
    
    #为了避免index与falling的重复，所以手动加200
    index = index +400

    label_part = video_path.split('/')[-1].split('.')[0]  # '059' 或 '084'
    frames_folder_name = f"squatting{label_part}"  # 'falling059' 或 'falling084'
    frames_path = os.path.join(frames_base_path, frames_folder_name)

    if not os.path.exists(frames_path):
        print(f"Frames path {frames_path} does not exist. Skipping entry.")
        continue


    frames_files = [f for f in os.listdir(frames_path) if f.endswith('.png')]
    num_frames = len(frames_files)

    # 构建image字段
    image_entries = {f"<image_{i:02d}>": os.path.join(frames_path, f'image_{i+1:02d}.png') for i in range(num_frames)}

    # 构建conversations
    user_content = "\n".join(image_entries.keys()) + " Describe the video in detail"
    action_content = f"Classify the text into actions, such as falling, lying, squatting, jumping, etc.\nText: {entry['description']}\nAction:"

    # 构建新的条目
    new_entry = {
        "id": str(index),
        "video_path" : entry["video_path"],
        "image": image_entries,
        "conversations": [
            {"role": "user", "content": user_content},
            {"role": "assistant", "content": entry["description"]},
            {"role": "user", "content": action_content},
            {"role": "assistant", "content": entry["Action"]}
        ]
    }

    new_data.append(new_entry)

with open(output_json_path, 'w') as f:
    json.dump(new_data, f, indent=4)

print(f"Processed data saved to {output_json_path}.")
