import random
#Helper function to add line numbers to each line
def add_line_numbers(lines_list):
  for i in range(len(lines_list)):
        lines_list[i] = f"{i+1} {lines_list[i]}"
  return lines_list

#Main functions
def get_file_lines(filename):
    poem = open(filename, "r")
    return poem.read().splitlines()

def print_lines_backward(lines_list):
    lines_list.reverse()
    for line in lines_list:
      print(line)

def lines_printed_random(lines_list):
  random.shuffle(lines_list)
  for line in lines_list:
    print(line)

#Prints all the even lines then prints the odd lines
def lines_printed_custom(lines_list):
  #Prints the even lines
  for i in range(len(lines_list)):
    if i%2==0:
      print(lines_list[i])
  #prints the odd lines
  for i in range(len(lines_list)):
    if not i%2==0:
      print(lines_list[i] if not i%2==0 else None)

poem_lines = get_file_lines("poem.txt") #Kept this around just in case you don't want line numbers for something
poemWithNumbers = add_line_numbers(poem_lines) #Use this as the poem list, it has the line numbers in it