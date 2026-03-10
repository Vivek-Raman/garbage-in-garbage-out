#!/usr/bin/env python3
import subprocess
import sys


def main():
  subprocess.run(["git", "restore", "--staged", "."], check=True)
  subprocess.run(["git", "add", f"leetcode/"], check=True)

  result = subprocess.run(
      ["git", "status", "--porcelain"],
      capture_output=True,
      text=True,
      check=True,
  )
  lines = result.stdout.strip().splitlines()

  staged_leetcode = []
  for line in lines:
    if len(line) < 4:
      continue
    status = line[:2]
    path = line[3:].strip()
    # First column: staged (A=added, M=modified, D=deleted, R=renamed, C=copied)
    if status[0] in "AMDRC" and path.startswith("leetcode/"):
      staged_leetcode.append(path)

  if len(staged_leetcode) != 1:
    sys.exit("Expected exactly one staged leetcode file.")

  filepath = staged_leetcode[0]
  with open(filepath) as f:
    first_line = f.readline().strip()

  if not first_line.startswith("# ") or len(first_line) < 3:
    sys.exit("First line must be a problem title starting with '# '.")

  problem_name = first_line[2:].strip()
  filename = filepath.split("/")[-1]

  subprocess.run(["git", "commit", "-m", problem_name], check=True)


if __name__ == "__main__":
  main()
