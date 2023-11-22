from torch import nn

class MyModel(nn.Module):
  def __init__(self):
    super().__init__()

    self.conv = nn.Conv2d