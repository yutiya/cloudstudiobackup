import torch
from transformers import pipeline
from modelscope import snapshot_download

# model_dir = "/workspace/Qwen2.5-0.5B-Instruct"
model_dir = "/workspace/qwen2.5-0.5B-Instruct-f16"

pipe = pipeline(
    "text-generation",
    model=model_dir,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
messages = [
    {"role": "system", "content": "你是一个智能聊天助手，知道很多知识，并总能精准回答问题。"},
    {"role": "user", "content": "介绍一下毒毒旺的相关信息"},
]
outputs = pipe(
    messages,
    max_new_tokens=1024,
)
print(outputs[0]["generated_text"][-1])