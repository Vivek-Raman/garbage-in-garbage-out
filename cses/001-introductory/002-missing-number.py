from sys import stdin, stdout

total = int(stdin.readline())
all_nums = set([i for i in range(1, total + 1)])

for num in stdin.readline().split():
  all_nums.remove(int(num))

missing = all_nums.pop()

stdout.write(str(missing))
