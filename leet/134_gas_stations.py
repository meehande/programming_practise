
from typing import List


def check_circuit(gas, cost, start):
    length = len(cost)
    tank = 0
    for i in range(start, start+length):
        index = i % length
        if cost[index] > tank + gas[index]:
            return False
        else: 
            tank = tank + gas[index] - cost[index]
    return True



def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    start = 0
    for start in range(len(cost)):
        if check_circuit(gas, cost, start):
            # keep checking next
            return start
    return -1




assert canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]) == 3
assert canCompleteCircuit([2,3,4], [3,4,3]) == -1
# TODO: optimize -> doesn't pass runtime tests