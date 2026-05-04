"""
Flip the States

Given an array of states [0, 0, 0, ...] and a sequence of operations
["L", "L", "C1", "C10", "L", ...], apply them as follows:

    "L"   -> Find the first 0 from the left and flip it to 1.
    "C{i}" -> Flip the value at index i back to 0 (ignore its current value).

Finally, return the resulting state as a string, e.g., "10011000".

Example:
    states = [0, 0, 0, 0, 0, 0, 0, 0]
    ops    = ["L", "L", "C1", "C10", "L"]
    output -> "10100000"
"""

def flip_states(states: list[int], ops: list[str]) -> str:
    # your code here
    n = len(states) 
    zeros = [i for i in range(n)] # indicies are zero since auto intialized to all 0
    # zeros = [i for i, val in enumerate(states) if val == 0]
    heapq.heapify(zeros)

    for op in ops:
        if op == "L":
            while zeros and states[zeros[0]] != 0:
                heapq.heappop(zeros)
            if zeros:
                i = heapq.heappop(zeros)
                states[i] = 1 # we set it to 1
        else:
            index = int(op[1:]) # all the values after C
            if index < n: # make sure not out of bounds else ignore 
                states[index] = 0
                heapq.heappush(zeros, index) # we need to add the 0 
    
    return "".join(map(str, states))