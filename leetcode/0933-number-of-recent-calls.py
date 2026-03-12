# 933. Number of Recent Calls

from collections import deque


class RecentCounter:

  def __init__(self) -> None:
    self.counter = deque()

  def ping(self, t: int) -> int:
    self.counter.append(t)
    while self.counter[0] < t - 3000:
      self.counter.popleft()
    return len(self.counter)


if __name__ == "__main__":
  s = RecentCounter()
  print(s.ping(1))
  print(s.ping(1000))
  print(s.ping(3001))
  print(s.ping(3002))
