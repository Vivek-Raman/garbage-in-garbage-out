from sys import stdin, stdout

count = int(stdin.readline())

data_in = stdin.readline().split()

operations = 0

running_max = 1
for raw_val in data_in:
  val = int(raw_val)
  if val < running_max:
    operations += running_max - val
  else:
    running_max = val

stdout.write(str(operations))
