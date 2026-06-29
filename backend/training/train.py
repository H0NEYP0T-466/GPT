import torch
from config.tokenizer import getbatch, vocab_size,xb,yb
from module.bigramModel import bigramModel,random

m=bigramModel(vocab_size)

optimizer=torch.optim.AdamW(m.parameters(),lr=1e-3)
batch_size=32

for steps in range(10000):
    xb,yb=getbatch("train")
    logits,loss=m.forward(xb,yb)
    optimizer.zero_grad(set_to_none=True)
    loss.backward()
    optimizer.step()
    print("loss:",loss.item())


print("Generating text after training:",random())
    