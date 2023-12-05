from torch import nn

class MyModel(nn.Module):
  def __init__(self ,in_channel:int=3 ,out_channel:int=256 ,kernel_size:int=5 ,padding:int=0 , stride: int=8):
    super().__init__()
    self.in_channel = in_channel
    self.out_channel = out_channel
    self.kernel_size = kernel_size
    self.padding = padding
    self.stride = stride


  def forward(self, _in):

    conv = nn.Conv2d(self.in_channel,self.out_channel,self.kernel_size,padding=self.padding,stride=self.stride)
    out1 = conv(_in)
    norm = nn.BatchNorm2d(num_features=out1.size()[1])
    out2 = norm(out1)
    relu = nn.ReLU()
    out3 = relu(out2)
    #print(repr(out3.size()))
    size = out3.size()
    #re_out3 = torch.reshape(out3,(size[0],size[1]*size[2]*size[3]))
    
    re_out3 = out3.view(size[0],size[1] * size[2] * size[3])
    #print(re_out3.size())
    linear = nn.Linear(re_out3.size()[1],64)
    out4 = linear(re_out3)


    return out4

