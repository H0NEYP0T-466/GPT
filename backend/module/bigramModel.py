import torch
import torch.nn as nn
from torch.nn import functional as F
from config.tokenizer import vocab_size,xb,yb,decoder


torch.manual_seed(1337)

class bigramModel(nn.Module):
    def __init__(self,vocab_size):
        super().__init__()
        self.token_embedding_table=nn.Embedding(vocab_size, vocab_size)
    
    def forward(self,idx,targets=None):
        logits=self.token_embedding_table(idx)
        if targets is None:
            loss=None
        else:
            loss=F.cross_entropy(logits.view(-1,vocab_size),targets.view(-1))
            return logits,loss
    
        def generate(self,idx,max_new_tokens):
            for _ in range(max_new_tokens):
                logits,loss=self(idx)
                logits=logits[:,-1,:]
                probs=F.softmax(logits,dim=-1)
                idx_next=torch.multinomial(probs,num_samples=1)
                idx=torch.cat((idx,idx_next),dim=1)
            return idx



m=bigramModel(vocab_size)
out=m.forward(xb,yb)
print("logits shape:",out[0].shape,"data type:",out[0].dtype)
print("loss:",out[1])
idx=torch.zeros((1,1),dtype=torch.long)

print("---"*10)
print(decoder(m.generate(idx,max_new_tokens=100)[0].tolist()))