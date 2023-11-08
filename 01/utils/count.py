from utils.function import function

def count_word(s,character):
  assert isinstance(s,str)
  assert isinstance(character,str)
  assert len(character) == 1
  num = 0
  for i in range(len(s)):
    if s[i] == character:
      num = function.add(num,1)
  return num

#うぇえええい