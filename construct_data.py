import json
import os
from openai import OpenAI  # 确保你已安装并正确配置了OpenAI的Python库

def ask_api(question, api_key):
    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
    
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": question},
        ],
        stream=False
    )
    
    return response.choices[0].message.content

api_key='sk-faa9b1c39b6f4f2aae2c0208c26eb421'

def process_and_reconstruct_json(input_json_path, output_json_path, api_key):
    with open(input_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    new_data = []

    for index, entry in enumerate(data):
        video_path = entry["video_path"]
        label_part = os.path.basename(os.path.dirname(video_path))  # 提取 "falling"
        video_number = os.path.basename(video_path).split('.')[0]  # 提取 "084"
        frames_path = f'/root/cpmv2_6/trimmed{video_number}/image_{{:02d}}.png'  # 图片路径模板

        # 构建 image 字段
        images = {f"<image_{i:02d}>": frames_path.format(i + 1) for i in range(8)}  # 假设有8帧

        # 准备 conversations
        user_content = "\n".join(images.keys()) + " Describe the video in detail"
        assistant_content = entry["response"]
        
        # API调用
        question = f"Classify the text into actions, such as falling, lying, squatting, jumping, etc.\nText: {assistant_content}\nAction:"
        action_response = ask_api(question, api_key)

        # 构建新的 JSON 结构
        new_entry = {
            "id": str(index),  # 为每个条目分配唯一的 id
            "video_path": video_path,
            "image": images,
            "conversations": [
                {"role": "user", "content": user_content},
                {"role": "assistant", "content": assistant_content},
                {"role": "user", "content": "Classify the text above into actions, such as falling, lying, squatting, jumping, etc."},
                {"role": "assistant", "content": action_response}
            ]
        }

        new_data.append(new_entry)

 
    with open(output_json_path, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, indent=4)


process_and_reconstruct_json('/root/cpmv2_6/result_cpmv2_6/cpmv_falling.json', '/root/cpmv2_6/result_cpmv2_6/processed_data.json', api_key)
