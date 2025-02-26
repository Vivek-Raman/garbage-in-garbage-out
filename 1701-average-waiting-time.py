from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        free_at = customers[0][0]
        waiting_time = 0
        for customer in customers:
            arrival = customer[0]
            prep_time = customer[1]
            cust_waiting = prep_time
            if arrival < free_at:
                cust_waiting += free_at - arrival
            else:
                free_at = arrival
            free_at += prep_time

            waiting_time += cust_waiting
        return waiting_time / len(customers)


if __name__ == '__main__':
    # print(Solution().averageWaitingTime([[1, 2], [2, 5], [4, 3]]))
    print(Solution().averageWaitingTime([[2, 3], [6, 3], [7, 5], [11, 3], [15, 2], [18, 1]]))
