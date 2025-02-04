from funasr import AutoModel

model = AutoModel(model="fa-zh", model_revision="v2.0.4")

wav_file = f"/workspace/asr_example_zh.wav"
text_file = f"/workspace/text.txt"
res = model.generate(input=(wav_file, text_file), data_type=("sound", "text"))
print(res)

# 检测每一个字的开始和结束时间 ms数据