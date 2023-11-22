import torch
from torch import nn

if __name__ == "__main__":

  my_tensor = torch.full((32,3,128,128),2.718)

  conv = nn.Conv2d(in_channels=3,out_channels=64,kernel_size=3)
  out = conv(my_tensor)
  print("===== problem2 =====\n",repr(out.size()))

  conv2 = nn.Conv2d(in_channels=3,out_channels=256,kernel_size=3,padding=1,stride=2)
  out2 = conv2(my_tensor)
  print("===== problem3 =====\n",repr(out2.size()))

  new_conv = nn.Conv2d(in_channels=3,out_channels=64,kernel_size=5,padding=1)
  new_out = new_conv(my_tensor)
  print("===== problem4_1 =====\n",new_out.size())

  new_conv2 = nn.Conv2d(in_channels=3,out_channels=256,kernel_size=5,padding=2,stride=2)
  new_out2 = new_conv2(my_tensor)
  print("===== problem4_2 =====\n",new_out2.size())

