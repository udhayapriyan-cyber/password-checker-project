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
    print("Length score:1/1\n")
  else:
    print("use length more than 15 characters\nscore:0/1\n")
  if lowercase(password):
    score+=1
    print("Lowercase score:1/1\n")
  else:
    print("use atleast one lowercase character\nscore:0/1\n")
  if uppercase(password):
    score+=1
    print("uppercase score:1/1\n")
  else:
    print("use atleast one uppercase character\nscore:0/1\n")
  if numbers(password):
    score+=1
    print("number score:1/1\n")
  else:
    print("use atleast one digit character\nscore:0/1\n")
  if special_characters(password):
    score+=1
    print("special character score:1/1\n")
  else:
    print("use atleast one special character\nscore:0/1\n")
  return score
