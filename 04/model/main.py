import torch
import model


if __name__ == "__main__":
  _in = torch.ones((32,3,128,128))

  mymodel = model.MyModel(in_channel=3,out_channel=256,kernel_size=5,stride=8)

  print(mymodel(_in).size())
    