from funasr import AutoModel

model = AutoModel(model="ct-punc", model_revision="v2.0.4")

res = model.generate(input="你好小智 有什么可以帮到你的吗 我随时都在的 有什么需求你就说")
print(res)