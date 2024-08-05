class Solution:
    def __init__(self):
        self.max_value = pow(2, 31) - 1
        self.min_value = -self.max_value + 1

    def myAtoi(self, s: str) -> int:
        number = 0
        negative = False
        started = False
        for ch in s:
            match ch:
                case ' ':
                    if started:
                        break
                case '-':
                    if started:
                        break
                    started = True
                    negative = True
                case '+':
                    if started:
                        break
                    started = True
                case '0':
                    started = True
                    if number <= 0:
                        continue
                    number *= 10
                case '1':
                    started = True
                    number *= 10
                    number += 1
                case '2':
                    started = True
                    number *= 10
                    number += 2
                case '3':
                    started = True
                    number *= 10
                    number += 3
                case '4':
                    started = True
                    number *= 10
                    number += 4
                case '5':
                    started = True
                    number *= 10
                    number += 5
                case '6':
                    started = True
                    number *= 10
                    number += 6
                case '7':
                    started = True
                    number *= 10
                    number += 7
                case '8':
                    started = True
                    number *= 10
                    number += 8
                case '9':
                    started = True
                    number *= 10
                    number += 9
                case _:
                    started = False
                    break;
        if negative:
            number *= -1
        return max(min(number, self.max_value), self.min_value)


if __name__ == '__main__':
    # print(Solution().myAtoi("1337c0d3"))
    print(Solution().myAtoi(" 0-1"))
