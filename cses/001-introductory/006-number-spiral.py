from sys import stdin, stdout

# tests = [(2, 3), (1, 1), (4, 2)]
tests = []
for i in range(int(stdin.readline())):
  tests.append(tuple(map(int, stdin.readline().split())))

answers = []
for (r, c) in tests:
  # r odd  = increase over c
  # r even = decrease over c
  diag_rc = max(r, c)
  delta_r, delta_c = diag_rc - r, diag_rc - c
  ans = 1 + (diag_rc - 1) * diag_rc

  # r odd  = inc over c
  if delta_c > 0 and r % 2 == 1:
    ans -= delta_c

  # r even = dec over c
  elif delta_c > 0 and r % 2 == 0:
    ans += delta_c

  # c odd  = dec over r
  elif delta_r > 0 and c % 2 == 1:
    ans += delta_r

  # c even = inc over r
  elif delta_r > 0 and c % 2 == 0:
    ans -= delta_r

  answers.append(ans)

stdout.write('\n'.join(map(str, answers)))
