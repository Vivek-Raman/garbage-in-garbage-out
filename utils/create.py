print("Enter the Leetcode number and title.")
print("Example: 6767. Title goes Here")

problem_name = input(" > ").strip()

split = problem_name.split(' ')
number_part = split[0].rstrip('.')
words = [w.lower() for w in split[1:]]

target_name = number_part + '-' + '-'.join(words)
target_file = f"{target_name}.py"
print(f"Creating file: {target_file}")

template = f"""
# {problem_name}

class Solution:
  pass


if __name__ == "__main__":
  s = Solution()
  print(s)
""".lstrip()

with open(target_file, mode="w") as fd:
  fd.writelines(template)

print(f"File created. Good luck!")
