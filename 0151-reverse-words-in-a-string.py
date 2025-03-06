from collections import deque

class Solution:
  def reverseWords(self, s: str) -> str:
    q = deque()
    res = []
    for word in s.strip().split(' '):
      word = word.strip()
      if word == '':
        continue
      q.appendleft(word)
    while len(q) > 0:
      res.append(q.popleft())
    return ' '.join(res);

if __name__ == '__main__':
  print(Solution().reverseWords('the sky is blue'))
