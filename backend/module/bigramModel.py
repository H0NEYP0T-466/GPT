import torch
import torch.nn as nn
from torch.nn import functional as F
from config.tokenizer import vocab_size,xb,yb

torch.manual_seed(1337)

class bigramModel(nn.Module):
    def __init__(self,vocab_size):
        super().__init__()
        self.token_embedding_table=nn.Embedding(vocab_size, vocab_size)
    
    def forward(self,idx,targets):
        logits=self.token_embedding_table(idx)
        return logits


m=bigramModel(vocab_size)
out=m.forward(xb,yb)
print("logits shape:",out.shape,"data type:",out.dtype)