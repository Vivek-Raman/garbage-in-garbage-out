from collections import deque

class Solution:
  def predictPartyVictory(self, senate: str) -> str:
    radiants = deque()
    dires = deque()

    for i, s in enumerate(senate):
      if (s == 'R'):
        radiants.append(i)
      else:
        dires.append(i)

    next_idx = len(senate)
    while len(radiants) > 0 and len(dires) > 0:
      r = radiants.popleft()
      d = dires.popleft()
      if r < d:
        radiants.append(next_idx)
        next_idx += 1
      else:
        dires.append(next_idx)
        next_idx += 1

    return 'Dire' if len(radiants) == 0 else 'Radiant'

if __name__ == '__main__':
  print(Solution().predictPartyVictory('RDD'))
