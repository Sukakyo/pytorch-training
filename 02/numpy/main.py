import numpy as np

data = np.array([
  [[85,78],[67,82],[92,88],[75,70],[60,64]],
  [[70,68],[77,72],[85,90],[60,65],[78,76]],
  [[80,84],[88,87],[66,68],[72,73],[64,60]]  
])

if __name__ == "__main__":
  print(np.shape(data))
  print(np.mean(data,axis=1))
  print(np.max(data[:,:,1]))
  print(np.max(data.reshape(np.shape(data)[2],np.shape(data)[0] * np.shape(data)[1]),axis=1) - np.min(data.reshape(np.shape(data)[2],np.shape(data)[0] * np.shape(data)[1]),axis=1))
  print(np.shape(data[data[:,:,0] >= 80])[0])
  #print(np.sum(data[np.sum(data,axis=2) > 135],axis=1))
  print(np.shape(data[np.sum(data,axis=2) > 135])[0])
  print(np.reshape(data.transpose(2,0,1)[0],-1))
  print((np.sum((np.reshape(data.transpose(2,0,1)[0],-1) - np.mean(np.reshape(data.transpose(2,0,1)[0],-1))) 
        * (np.reshape(data.transpose(2,0,1)[1],-1) - np.mean(np.reshape(data.transpose(2,0,1)[1],-1)) ))) / 15
        / (np.std(np.reshape(data.transpose(2,0,1)[0],-1)) * np.std(np.reshape(data.transpose(2,0,1)[1],-1))))