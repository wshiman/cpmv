# import json
# import os
# from PIL import Image
# from decord import VideoReader, cpu

# MAX_NUM_FRAMES = 32  # if cuda OOM set a smaller number

# def encode_video(video_path):
#     def uniform_sample(l, n):
#         gap = len(l) / n
#         idxs = [int(i * gap + gap / 2) for i in range(n)]
#         return [l[i] for i in idxs]

#     vr = VideoReader(video_path, ctx=cpu(0))
#     sample_fps = round(vr.get_avg_fps() / 1)  # FPS
#     frame_idx = [i for i in range(0, len(vr), sample_fps)]
#     if len(frame_idx) > MAX_NUM_FRAMES:
#         frame_idx = uniform_sample(frame_idx, MAX_NUM_FRAMES)
#     frames = vr.get_batch(frame_idx).asnumpy()
#     frames = [Image.fromarray(v.astype('uint8')) for v in frames]
#     print('num frames:', len(frames))
#     return frames

# def save_frames(frames, save_dir):
#     os.makedirs(save_dir, exist_ok=True)
#     for idx, frame in enumerate(frames):
#         frame.save(os.path.join(save_dir, f'image_{idx+1:02d}.png'))

# def process_videos(json_path, output_dir):
#     with open(json_path, 'r', encoding='utf-8') as f:
#         data = json.load(f)

#     for entry in data:
#         video_path = entry["video_path"]
        
#         # 提取视频标签部分作为保存路径
#         label_part = os.path.basename(os.path.dirname(video_path))  # 获取 "falling"
#         video_number = os.path.basename(video_path).split('.')[0]  # 获取 "084"
#         save_dir = os.path.join(output_dir, f'frames/{label_part}{video_number}')  # 生成路径 falling084

#         # 编码视频并保存帧
#         frames = encode_video(video_path)
#         save_frames(frames, save_dir)

# # 调用处理函数
# process_videos('/root/cpmv2_6/result_cpmv2_6/cpmv_falling.json', '/root/autodl-tmp')


import json
import os
from PIL import Image
from decord import VideoReader, cpu

MAX_NUM_FRAMES = 32  # if cuda OOM set a smaller number

def encode_video(video_path):
    def uniform_sample(l, n):
        gap = len(l) / n
        idxs = [int(i * gap + gap / 2) for i in range(n)]
        return [l[i] for i in idxs]

    vr = VideoReader(video_path, ctx=cpu(0))
    sample_fps = round(vr.get_avg_fps() / 1)  # FPS
    frame_idx = [i for i in range(0, len(vr), sample_fps)]
    if len(frame_idx) > MAX_NUM_FRAMES:
        frame_idx = uniform_sample(frame_idx, MAX_NUM_FRAMES)
    frames = vr.get_batch(frame_idx).asnumpy()
    frames = [Image.fromarray(v.astype('uint8')) for v in frames]
    print('num frames:', len(frames))
    return frames

def save_frames(frames, save_dir):
    os.makedirs(save_dir, exist_ok=True)
    for idx, frame in enumerate(frames):
        frame.save(os.path.join(save_dir, f'image_{idx+1:02d}.png'))

def process_videos(json_path, output_dir):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for entry in data:
        video_path = entry["video_path"]
        
        # 提取视频编号并检查是否大于100
        video_number = int(os.path.basename(video_path).split('.')[0])  # 获取视频编号

        if video_number > 100:  # 只处理编号大于100的视频
            # 提取视频标签部分作为保存路径
            label_part = os.path.basename(os.path.dirname(video_path))  # 获取 "falling"
            save_dir = os.path.join(output_dir, f'frames/{label_part}{video_number}')  # 生成路径 falling084

            # 编码视频并保存帧
            frames = encode_video(video_path)
            save_frames(frames, save_dir)
            print("ok!")
        # else:
        #     print(f"Skipping video {video_path} with number {video_number}.")

process_videos('/root/cpmv2_6/result_cpmv2_6/cpmv_falling(2).json', '/root/autodl-tmp')
