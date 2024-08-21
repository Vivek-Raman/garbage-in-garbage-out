from sys import stdin, stdout

data_in = list(map(int,stdin.readline().split()))

out = 0

for i in data_in:
    out += i

stdout.write(str(out))
