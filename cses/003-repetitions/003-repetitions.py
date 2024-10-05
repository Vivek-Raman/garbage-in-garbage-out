from sys import stdin, stdout

data_in = stdin.readline().strip()

max_length = 1

i = 0
while i < len(data_in) - 1:
  if data_in[i + 1] == data_in[i]:
    length = 1
    for j in range(i+1, len(data_in)):
      if data_in[i] != data_in[j]:
        break
      length += 1
    if length > max_length:
      max_length = length
    i = j
  else:
    i += 1

stdout.write(str(max_length))
