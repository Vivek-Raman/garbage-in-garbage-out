from sys import stdin, stdout

val = int(stdin.readline())
while val != 1:
    stdout.write(str(val) + ' ')
    if val % 2 == 0:
        val //= 2
    else:
        val = 3 * val + 1

stdout.write(str(val))
