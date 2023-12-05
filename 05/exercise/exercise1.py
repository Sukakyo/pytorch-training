from pathlib import Path

data_directory = "./data"

data_directory_path = Path(data_directory).resolve()

print("---problem1---")
print(data_directory_path)
#print(type(data_directory_path))
directory_children_pathes = list(data_directory_path.glob("*"))

print("---problem2---")
for path in directory_children_pathes:
  if path.is_dir() :
    print(path)

print("---problem3---")
sum = 0
for path in directory_children_pathes:
  if path.is_dir():
    image_pathes = list(path.glob("*.png"))
    sum += len(image_pathes)

print(sum)
