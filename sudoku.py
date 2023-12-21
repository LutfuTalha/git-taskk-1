import random

x = True
while x:
  a1 = random.randint(1, 3)
  a2 = random.randint(1, 3)
  a3 = random.randint(1, 3)
  b1 = random.randint(1, 3)
  b2 = random.randint(1, 3)
  b3 = random.randint(1, 3)
  c1 = random.randint(1, 3)
  c2 = random.randint(1, 3)
  c3 = random.randint(1, 3)
  if (a1 == b1) or (a1 == c1) or (a1 == a2) or (a1 == a3):
    y = 0
  elif (a2 == b2) or (a2 == c2) or (a2 == a3):
    y = 0
  elif (a3 == b3) or (a3 == c3):
    y = 0
  elif (b2 == c2) or (b2 == b1) or (b2 == b3):
    y = 0
  elif (b1 == c1) or (b1 == b3):
    y = 0
  elif (b3 == c3):
    y = 0
  elif (c1 == c2) or (c1 == c3) or (c2 == c3):
    y = 0
  else:
    x = False

else:
  three_by_three = [[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]]

T = True
while T:
  a = random.randint(0,2)
  b = random.randint(0,2)
  c = random.randint(0,2)
  d = random.randint(0,2)
  if (a == c) and (b == d):
    y = 0
  else:
    T = False
backup = three_by_three[a][b]
backup2 = three_by_three[c][d]
three_by_three[a][b] = "X"
three_by_three[c][d] = "Y"


for i in three_by_three:
  print(i)
three_by_three[a][b] = backup
three_by_three[c][d] = backup2
answer1 = input("X yerine ne yazılmalıdır? \n")
if three_by_three[a][b] == int(answer1):
  answer2 = input("Y yerine ne yazılmalıdır? \n")
  if int(answer2) == three_by_three[c][d]:
    print("Tebrikler cevaplarınız doğru!")
    for i in three_by_three:
      print(i)
  else:
    print("Yanlış yaptın :( Devam etmek için tekrar başlatın!")
  
else:
  print("Yanlış yaptın :( Devam etmek için tekrar başlatın!")
