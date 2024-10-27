import json


input_path = "/root/cpmv2_6/result_cpmv2_6/cpmv_falling(2).json"
with open(input_path, "r", encoding="utf-8") as file:
    data = json.load(file)


for entry in data:
    video_filename = entry["video_path"].split('/')[-1]
    entry["video_path"] = f"/root/autodl-tmp/data/falling/{video_filename}"


with open(input_path, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print("Original JSON file updated.")
