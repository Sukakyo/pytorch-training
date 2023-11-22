import torch
from torch import nn

if __name__ == "__main__":
  _in = torch.ones((32,1024))

  fc1 = nn.Linear(in_features=1024,out_features=256,bias=True)
  out = fc1(_in)
  print(repr(out.size()))
  re_out = torch.reshape(out,(32,16,16))
  print(repr(re_out.size()))
  fc2 = nn.Linear(in_features=1024,out_features=2048,bias=True)
  print(repr(fc2(_in).size()))