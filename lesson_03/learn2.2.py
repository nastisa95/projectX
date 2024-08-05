while True:
    user_input = input("Enter your name: ")
    if user_input:
        break
print(f"You entered {user_input }")


i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)