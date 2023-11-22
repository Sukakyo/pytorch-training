from typing import Any
import torch
from torch.nn import Module

class ExerciseModel(Module):
  def __init__(self, mytensor,elem_add, elem_multiply):
    super().__init__()
    self.mytensor = mytensor
    self.elem_add = elem_add
    self.elem_multiply = elem_multiply

  def forward(self,input):
    output1 = self.mytensor + input
    output2 = output1 + self.elem_add
    output3 = output2 * self.elem_multiply
    return output1,output2,output3
  
if __name__ == "__main__":
  mymodel = ExerciseModel(torch.ones((3,3)),4,6)
  p2out,p3out,p4out = mymodel(torch.full((3,3),2))

  print("===== problem2 =====")
  print(repr(p2out))
  print("===== problem3 =====")
  print(repr(p3out))
  print("===== problem4 =====")
  print(repr(p4out))