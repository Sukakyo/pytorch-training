import torch
import numpy as np

data = np.array([
  [[85,78],[67,82],[92,88],[75,70],[60,64]],
  [[70,68],[77,72],[85,90],[60,65],[78,76]],
  [[80,84],[88,87],[66,68],[72,73],[64,60]]  
])

tensor_data = torch.tensor(data)

print("===== problem 1 =====\n",tensor_data)
tensor_remake = torch.permute(tensor_data,(2,0,1))
print("===== problem 2 =====\n",tensor_remake)
#print(torch.Tensor.size(tensor_remake))
tensor_sum = torch.sum(tensor_remake,dim=0)
print("===== problem 3 =====\n",tensor_sum)
tensor_mean = torch.mean(tensor_sum,dim=1,dtype=float)
print("===== problem 4 =====\n",tensor_mean)
tensor_mean2 = torch.sum(tensor_sum,dim=1,dtype=float) / torch.Tensor.size(tensor_sum)[1]
#tensor_mean2 = 
print("===== problem 5 =====\n",tensor_mean2)