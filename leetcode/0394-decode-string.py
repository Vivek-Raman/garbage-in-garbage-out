# 394. Decode String

from collections import deque


class Solution:

  def decodeString(self, s: str) -> str:
    result = ''
    stack = deque[str]()

    for c in s:
      if c == '[':
        stack.append(c)
      elif c == ']':
        # flush until [, pop again for repeat count
        to_repeat = deque[str]()
        while len(stack) > 0:
          popped = stack.pop()
          if popped == '[':
            break
          to_repeat.appendleft(popped)

        reps = deque[str]()
        while len(stack) > 0 and stack[-1].isdigit():
          reps.appendleft(stack.pop())
        reps = int(''.join(reps))
        # print(' '.join(stack), to_repeat, reps)

        if len(stack) == 0:
          to_repeat = ''.join(to_repeat)
          result += to_repeat * reps
        else:
          while reps > 0:
            for ch in list(to_repeat):
              stack.append(ch)
            reps -= 1

      elif len(stack) <= 0 and not c.isdigit():
        result += c
      else:
        # accumulate
        stack.append(c)
      # print(' '.join(stack))
    return result


if __name__ == "__main__":
  s = Solution().decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef")
  print(s)
