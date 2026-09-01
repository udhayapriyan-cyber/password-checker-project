def length(password):
  if len(password)>15:
    return True
  return False
def lowercase(password):
  for ch in password:
    if ch.islower():
      return True
  return False
def uppercase(password):
  for ch in password:
    if ch.isupper():
      return True
  return False
def numbers(password):
  for ch in password:
    if ch.isdigit():
      return True
  return False
def special_characters(password):
  for ch in password:
    if not ch.isalnum():
      return True
  return False
def check_strength(password):
  score=0
  if length(password):
    score+=1
  if lowercase(password):
    score+=1
  if uppercase(password):
    score+=1
  if numbers(password):
    score+=1
  if special_characters(password):
    score+=1
  return score
