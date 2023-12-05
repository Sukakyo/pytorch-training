import matplotlib.pyplot as plt
from PIL import Image
from pathlib import Path
#import torch
from torch.utils.data import Dataset
from torchvision import transforms as transforms

class MyDataset(Dataset):

  def __init__(self,dataset_dir):
    dir_path_resolved = Path(dataset_dir).resolve()
    self.img_list = list(dir_path_resolved.glob("*.png"))
    self.transform = transforms.Compose([
      transforms.ToTensor(),
    ])

  def __len__(self):
    return len(self.img_list)
  
  def __getitem__(self, idx):
    img_path = self.img_list[idx]
    img = Image.open(img_path)
    img_tensor = self.transform(img)

    img_path = Path(img_path)
    parts = img_path.parts
    label = int(parts[-1][:3])

    return img_tensor, label
  

if __name__ == "__main__":
  dir_path = "./data"
  datasets = []
  data_children_path = list(Path(dir_path).glob("*"))
  for path in data_children_path:
    if path.is_dir():
      datasets.append(MyDataset(path))
      
  #print(datasets)

  sum = 0
  for data in datasets:
    sum += len(data)

  print("===problem1.1===")
  print(datasets[0][2][0].size())
  
  print("===problem1.2===")
  print(str(datasets[0][2][1]).zfill(3))