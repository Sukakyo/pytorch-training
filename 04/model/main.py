import torch
import model


if __name__ == "__main__":
  _in = torch.ones((32,3,128,128))

  mymodel = model.MyModel()

  #print("===== before =====")
  print(repr(_in.size()))
  #print("===== after =====")
  print(repr(mymodel(_in).size()))
    