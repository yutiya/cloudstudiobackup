# 训练安装的一些库，缺少的需要继续补充

```
pip install --no-deps bitsandbytes accelerate xformers==0.0.29 peft trl triton
pip install --no-deps cut_cross_entropy unsloth_zoo
pip install sentencepiece protobuf datasets huggingface_hub hf_transfer
pip install --no-deps unsloth

pip install modelscope
```

# llama.cpp 
## https://github.com/ggerganov/llama.cpp/blob/master/docs/build.md

```
apt update
apt install cmake

git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
```

```CPU
cmake -B build
cmake --build build --config Release
```

```CUDA
cmake -B build -DGGML_CUDA=ON
cmake --build build --config Release
```

```
echo 'export PATH=$PATH:/workspace/llama.cpp/build/bin' >> ~/.bashrc
source ~/.bashrc
```

```
llama-cli -m ./Qwen2.5-0.5B-Instruct-f16.gguf

python convert_hf_to_gguf.py /workspace/Qwen2.5-0.5B-Instruct-f16 --outfile Qwen2.5-0.5B-Instruct-f16.gguf

llama-quantize /workspace/Qwen2.5-0.5B-Instruct-f16.gguf ./Qwen2.5-0.5B-Instruct-Q4_K_M.gguf Q4_K_M
```