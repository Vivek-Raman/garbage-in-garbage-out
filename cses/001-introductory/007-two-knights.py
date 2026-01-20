from sys import stdin, stdout


def total_configs(k):
  first = k**2
  second = k**2 - 1
  return first * second // 2


def attack_configs(k):
  twos = k - 1
  threes = k - 2
  two_by_threes = 2 * twos * threes
  three_by_twos = 2 * threes * twos
  return two_by_threes + three_by_twos


k = int(stdin.readline())

out = []
for i in range(k):
  total = total_configs(i + 1)
  atks = attack_configs(i + 1)
  out.append(total - atks)

stdout.write('\n'.join(map(str, out)))
