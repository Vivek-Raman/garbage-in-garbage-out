from collections import deque
from typing import List, Tuple


class Solution:

  def props(self, asteroid: int) -> Tuple[int, int]:
    strength = abs(asteroid)
    direction = asteroid // strength
    return strength, direction

  def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    stack = deque()
    for i, asteroid in enumerate(asteroids):
      stack.appendleft(asteroid)

      inc = self.props(asteroid)
      top = self.props(stack[-1])
      if top[1] < 0 and inc[1] > 0:
        diff = asteroid + stack.pop()
        if diff > 0:
          asteroids[i] = 0
        elif diff < 0:
          stack.

        stack.appendleft(max(inc, top, key=lambda x: x[0]))

      # while self.props(stack[-1])[1] != self.props(asteroid)[1] \
      #    or self.props(stack[-1]):
      #   pass

    ans = []
    for a in asteroids:
      if a != 0:
        ans.append(a)
    return ans


if __name__ == "__main__":
  s = Solution().asteroidCollision([5, 10, -5])
  # s = Solution().asd([8, -8])
  print(s)
