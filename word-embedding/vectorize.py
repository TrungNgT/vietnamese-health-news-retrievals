from FlagEmbedding import BGEM3FlagModel

model = BGEM3FlagModel("BAAI/bge-m3", use_fp16=False)

# For the first time, it will download the model from the Hugging Face model hub and cache it in the .cache/huggingface folder in my local machine.

def embedding(passage: str):
    passage = passage.replace("\n", " ")
    return model.encode(passage)["dense_vecs"]

