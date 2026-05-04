"""
E-Scooter Distance

You start at position 0 and need to reach a given endpoint along a number line.
E-scooters are placed at various positions along the way. Each scooter, once
taken, travels exactly 10 units before being dropped.

Rules:
    - Walk forward from your current position until you reach a scooter.
    - If a scooter is available, take it and ride exactly 10 units.
    - Continue until you reach (or pass) the endpoint.
    - Return the total distance traveled *using scooters* (not walking).

Example:
    endpoint = 20
    scooters = [7, 4, 14]
    output   -> ?

Function signature:
"""

def scooter_distance(endpoint: int, scooters: list[int]) -> int:
    # your code here
    heapq.heapify(scooters)
    num = 0 # position 
    totalScoot = 0 
    while scooters and num <= endpoint:
        while scooters and scooters[0] < num:
            heapq.heappop(scooters) # update the value 

        
        if not scooters: # we just walk the rest
            break
        if scooters[0] >= endpoint:  # we went past the limit 
            break  
        ride = min(10, endpoint - num)
        totalScoot += ride
        num += ride
    return totalScoot 