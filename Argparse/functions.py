import os

def register(r):
    with open('Tasks.txt', 'a') as file:
        file.write(f"Task -> {r[0].upper()}   Date =  {r[1]} \n")

def list():
    with open('Tasks.txt', 'r') as file:
      f = file.readlines()
      for line in f:
        print(line[0:-1])

def delete(task):
    string = " ".join(task).upper()
    with open("Tasks.txt", "r") as input:
        with open("temp.txt", "w") as output:
            # iterate all lines from file
            for line in input:
                # if substring contain in a line then don't write it
                if string not in line.strip("\n"):
                    output.write(line)
    os.replace('temp.txt', 'Tasks.txt')
    
