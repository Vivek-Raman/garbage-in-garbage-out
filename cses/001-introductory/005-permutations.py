from sys import stdin, stdout

data_in = int(stdin.readline())

if data_in in (2, 3):
  stdout.write("NO SOLUTION")
else:
  out = []

  # even
  for i in range(2, data_in + 1, 2):
    out.append(i)

  # odd
  for i in range(1, data_in + 1, 2):
    out.append(i)

  stdout.write(' '.join(map(str, out)))
