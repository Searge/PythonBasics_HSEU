number = int(input())
hat = "   _~_    "
eyes = "  (o o)   "
mouth = " /  V  \  "
knees = "/(  _  )\ "
toes = "  ^^ ^^   "
penguin = [hat, eyes, mouth, knees, toes]

for member in penguin:
    print(member * number)
