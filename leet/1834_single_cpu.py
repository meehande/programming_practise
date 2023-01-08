"""
You are given n​​​​​​ tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, where tasks[i] = [enqueueTimei, processingTimei] means that the i​​​​​​th​​​​ task will be available to process at enqueueTimei and will take processingTimei to finish processing.

You have a single-threaded CPU that can process at most one task at a time and will act in the following way:

If the CPU is idle and there are no available tasks to process, the CPU remains idle.
If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
Once a task is started, the CPU will process the entire task without stopping.
The CPU can finish a task then start a new one instantly.
Return the order in which the CPU will process the tasks.


Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
Output: [0,2,3,1]


Input: tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
Output: [4,3,2,0,1]

"""
from typing import List
from heapq import heappush, heappop


def single_threaded_cpu_ordered_input(input_tasks = [[1,2],[2,4],[3,2],[4,1]]):
    """
    Assumption: tasks come in order of increasing enqueue time -> false assumption
    """
    #input_tasks = [] looks like [[T0_e, T0_p], [T1_e, T1_p]...]
    position_in_tasklist = 0
    t = 0
    queue = []  # looks like [(Tp, index)]
    processed = []
    while True:
        # add tasks to the queue in the appropriate priority if the enque time has been hit
        while position_in_tasklist < len(input_tasks):
            if t >= input_tasks[position_in_tasklist][0]:
                heappush(queue, (input_tasks[position_in_tasklist][1], position_in_tasklist))
                position_in_tasklist += 1
            else:
                break

        # if there is a task on the queue, process it
        if len(queue) > 0:
            priority, index = heappop(queue)
            processed.append(index)  
            t += input_tasks[index][1]
        else:
            t += 1

        if len(queue) == 0 and position_in_tasklist >= len(input_tasks):
            return processed




def preprocess(input_tasks: List[List[int]]):
    queue = []  # looks like [(Tp, index), (Tp, index),...]
    enqueue_times = [] # looks like [T0e, T1e, ...]
    for index, task in enumerate(input_tasks):
        heappush(queue, (task[1], index))
        enqueue_times.append(task[0])
    return queue, enqueue_times


def single_threaded_cpu_unordered_input(input_tasks = [[1,2],[2,4],[3,2],[4,1]]):
    """
    Assumption: input tasks can be in any order
    Note: this will be worst case if the list is in reverse order / the closer to reverse order as 
    it will pop and repush every element on every iteration
    """
    queue, enqueue_times = preprocess(input_tasks)
    t = min(enqueue_times)
    processed = []

    not_ready = []
    while queue:
        next_tp, next_index = heappop(queue)
        while t < enqueue_times[next_index]:
            not_ready.append((next_tp, next_index))
            next_tp, next_index = heappop(queue)
        
        # process next task
        t += next_tp
        processed.append(next_index)
        # repush off not_ready
        while not_ready:
            heappush(queue, not_ready.pop())

    return processed


import numpy as np


def preprocess_arrays(tasks):
    a = np.array(tasks)
    return a[:,0], a[:,1]


def single_threaded_cpu_arrays(tasks):
    enqueue_time, processing_time = preprocess_arrays(tasks)
    n_processed = 0
    n_to_process = len(tasks)
    t = 0
    processed = []
    while n_processed < n_to_process:
        eligible = (enqueue_time <= t) & (enqueue_time >= 0)
        if processing_time[eligible].size > 0:
            # process min
            to_process = np.argmin(np.ma.masked_array(processing_time, mask=eligible==0))

            t += processing_time[to_process]
            processed.append(to_process)
            
            processing_time[to_process] = -1
            enqueue_time[to_process] = -1
            n_processed += 1

        else:
            t += 1
    return processed








input_tasks = [[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]
output = [6,1,2,9,4,10,0,11,5,13,3,8,12,7]

# have to process the list at the start for scale (can't iterate through it on each go)
# or need to pop when 


def sort_input(tasks):
    sorted_tasks = sorted([[t[0], t[1], i] for i, t in enumerate(tasks)])
    enqueue_times = np.array(tasks)[:,0]
    return sorted_tasks, enqueue_times

def single_threaded_cpu_sort_input(tasks = [[1,2],[2,4],[3,2],[4,1]]):

    sorted_tasks, enqueue_times = sort_input(tasks)
    position_in_tasklist = 0
    queue = []  # looks like [(Tp, index)]
    processed = []
    t = min(enqueue_times)
    while True:
        # add tasks to the queue in the appropriate priority if the enque time has been hit
        while position_in_tasklist < len(sorted_tasks):
            if t >= sorted_tasks[position_in_tasklist][0]:
                heappush(queue, (sorted_tasks[position_in_tasklist][1], sorted_tasks[position_in_tasklist][2]))
                position_in_tasklist += 1
            else:
                break

        # if there is a task on the queue, process it
        if len(queue) > 0:
            processing_time, index = heappop(queue)
            processed.append(index)  
            t += processing_time
        else:
            t = min(enqueue_times[enqueue_times>t])

        if len(queue) == 0 and position_in_tasklist >= len(tasks):
            return processed