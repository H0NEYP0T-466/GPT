from .preprocessing import clean
from pathlib import Path
import torch

path=Path(__file__).parent.parent / "dataset/input.txt"
with open(path, "r") as f:
        dataset=f.read()

chars=clean(dataset)
vocab_size=len(chars)


def encoder(text):
    return [chars.index(c) for c in text]
def decoder(indices):
    return ''.join([chars[i] for i in indices])

finalData=torch.tensor(encoder(dataset),dtype=torch.long)

print("final data shape:", finalData.shape,"data type:", finalData.dtype)
print(finalData[:1000])
print("---"*10)



n=int(0.8*len(finalData))
train_data=finalData[:n]
test_data=finalData[n:]

torch.manual_seed(1337)
batch_size=4
context_window=8
train_data[:context_window+1]

def getbatch(split):
    data=train_data if split=="train" else test_data
    ix=torch.randint(len(data)-context_window,(batch_size,))
    x=torch.stack([data[i:i+context_window] for i in ix])
    y=torch.stack([data[i+1:i+context_window+1] for i in ix])
    return x,y

xb,yb=getbatch("train")

print("inputs:",xb.shape,xb)
print("targets:",yb.shape,yb)


