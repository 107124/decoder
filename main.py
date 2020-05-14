# ask user if they want to code or decode
# get user input
# loop each letter and assign it a number with a dictionary library
# assign spaces to a random number from 27 - 100
# print coded version of input
# for the decoder, assign numbers to letter in the dictionary
# if number is 27 + then assign a space
import random

def codeSentence(codeBook):
  sentence = input("Please type or paste your input here and hit enter:\n")
  for letter in sentence:
    if letter.upper() in codeBook:
      print(codeBook.get(letter.upper()))
    elif letter == " " or letter == "  ":
      print(random.randint(27,101))
    


def decodeSentence(codebook):
  sentence = input("Please type or paste the code you want translated and hit enter:\n") 
  for number in sentence:
    if number in codeBook:
     print(codeBook.get(number))



codeBook = {
  "A" : "1",
  "B" : "2",
  "C" : "3",
  "D" : "4",
  "E" : "5",
  "F" : "6",
  "G" : "7",
  "H" : "8",
  "I" : "9",
  "J" : "10",
  "K" : "11",
  "L" : "12",
  "M" : "13",
  "N" : "14",
  "O" : "15",
  "P" : "16",
  "Q" : "17",
  "R" : "18",
  "S" : "19",
  "T" : "20",
  "U" : "21",
  "V" : "22",
  "W" : "23",
  "X" : "24",
  "Y" : "25",
  "Z" : "26"
}

repeat = True

while repeat == True:
  status = input("1 for coding and 2 for decoding\n")

  if status == "1":
    print("You chose to code an input\n")
    repeat = False
  elif status == "2":
    print("You chose to decode an input\n")
    repeat = False
  else:
    print("Please select 1 or 2\n")
    repeat = True

if status == "1":
  codeSentence(codeBook)

elif status == "2":
  decodeSentence(codeBook)