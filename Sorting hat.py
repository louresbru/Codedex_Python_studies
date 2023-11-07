#sorting_hat

print('Q1) Do you like Dawn or Dusk?')
print('    1) Dawn')
print('    2) Dusk')
answer = int(input('Enter the number of your answer: '))

if answer == 1:
  G1 = 1 
  G2 = 0
  R1 = 1
  R2 = 0
  H1 = 0
  H2 = 0
  S1 = 0
  S2 = 0
elif answer == 2:
  G1 = 0
  G2 = 0
  R1 = 0
  R2 = 0
  H1 = 0
  H2 = 1
  S1 = 0
  S2 = 1
else:
  print('Wrong input')

print("Q2) When I'm dead, I want people to remember me as:")
print('    1) The Good')
print('    2) The Great')
print('    3) The Wise')
print('    4) The Bold')
answer = int(input('Enter the number of your answer: '))

if answer == 1:
  H3 = 2
  S3 = 0
  R3 = 0
  G3 = 0
elif answer == 2:
  S3 = 2
  H3 = 0
  R3 = 0
  G3 = 0 
elif answer == 3:
  R3 = 2
  H3 = 0
  S3 = 0
  G3 = 0
elif answer == 4:
  G3 = 2
  H3 = 0
  S3 = 0
  R3 = 0
else:
  print('Wrong input')

print("Q2) Which kind of instrument most pleases your ear?")
print('    1) The violin')
print('    2) The trumpet')
print('    3) The piano')
print('    4) The drum')
answer = int(input('Enter the number of your answer: '))

if answer == 1:
  S4 = 4
  H4 = 0
  R4 =0
  G4 = 0
elif answer == 2:
  H4 = 4
  S4 = 0
  R4 = 0
  G4 = 0
elif answer == 3:
  R4 = 4
  S4 = 0
  H4 = 0
  G4 = 0
elif answer == 4:
  G4 = 4
  S4 = 0
  H4 = 0
  R4 = 0
else:
  print('Wrong input')

H = (H1 + H2 + H3 + H4)
R = (R1 + R2 + R3 + R4)
S = (S1 + S2 + S3 + S4)
G = (G1 + G2 + G3 + G4)

result = max(H, R, S, G)

if max(H, R, S, G) == H:
  print('Hufflepuff')
if max(H, R, S, G) == R:
  print('Ravenclaw')
if max(H, R, S, G) == S:
  print('Slytherin')
if max(H, R, S, G) == G:
  print('Gryffindor')



