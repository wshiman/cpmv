import json

def process_conversations(input_json_path, output_json_path):

    with open(input_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for entry in data:
        if "conversations" in entry:
            
            entry["conversations"] = entry["conversations"][:2]

    
    with open(output_json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


input_json_path = '/root/cpmv2_6/result_cpmv2_6/eval.json'
output_json_path = '/root/cpmv2_6/result_cpmv2_6/processed_eval.json'


process_conversations(input_json_path, output_json_path)
