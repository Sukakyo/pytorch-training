from torchvision import transforms as transforms
from PIL import Image
import matplotlib.pyplot as plt

if __name__ == "__main__":
  image_path = "./example_data/dog_img.png"
  image = Image.open(image_path)


  preprocess_1 = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5,0.5,0.5],std=[0.5,0.5,0.5])
  ])

  preprocess_2 = transforms.Compose([
    transforms.RandomHorizontalFlip(0.5),
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.2),
    transforms.ToTensor()
  ])

  preprocess_3 = transforms.Compose([
    transforms.RandomHorizontalFlip(0.5),
    transforms.RandomResizedCrop((224,224)),
    transforms.ToTensor()
  ])

  processed_image1 = preprocess_1(image)
  processed_image2 = preprocess_2(image)
  processed_image3 = preprocess_3(image)


  print(type(processed_image1))
  print(type(processed_image1.permute((1,2,0))))
  
  plt.imshow(image)
  plt.show()
  plt.imshow(processed_image1.permute((1,2,0)))
  plt.show()
  plt.imshow(processed_image2.permute((1,2,0)))
  plt.show()
  plt.imshow(processed_image3.permute((1,2,0)))
  plt.show()

