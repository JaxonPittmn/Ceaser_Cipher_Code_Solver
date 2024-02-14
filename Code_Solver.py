done = False
alphabet = ["a", "b", "c", "d","e", "f", "g", "h", "i", "j", "k", "l", "m" ,
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
upper_alphabet = ["A", "B", "C", "D","E", "E", "G", "H", "I", "J", "K", "L", "M" ,
  "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
mod = int(input("What is your mod?: "))

while not done:
  message = input("What is your message?: ")
  new_message = ""
  new_message1 = ""
  found = 0
  for i in range(len(message)):
    new_message += message[i]
  
  for i in range(len(new_message)):
    if new_message[i] == " ":
      new_message1 += " "
    elif new_message[i] == "?":
      new_message1 += "?"
    elif new_message[i] == ".":
      new_message1 += "."
    elif new_message[i] == ",":
      new_message1 += ","
    elif new_message[i] == "!":
      new_message1 += "!"
    elif new_message[i] == "'":
      new_message1 += "'"
    else:
      find = new_message[i]
      for l in range(len(alphabet)):
        if find == alphabet[l]:
          new_message1 += alphabet[l - mod]
        elif find != alphabet[l] and find == upper_alphabet[l]:
          new_message1 += upper_alphabet[l - mod]
  print(new_message1)
  answer = input("Do you want to do a new message?: ")
  answer.lower()
  if answer == "yes":
    done = False
  else:
    done = True
  