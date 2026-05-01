from collections import defaultdict

problem_787 = """
787. Cheapest Flights Within K Stops
There are n cities, labeled 0 to n - 1, connected by some number of flights.
You are given a list `flights`, where flights[i] = [from_i, to_i, price_i]
represents a directed flight from city `from_i` to city `to_i` costing `price_i`.
You are also given three integers: `src`, `dst`, and `k`.
Return the cheapest total price to travel from `src` to `dst` using at most
`k` stops (i.e., at most k + 1 flights). If no such route exists, return -1.
Function signature:
    def findCheapestPrice(n: int, flights: list[list[int]],
                          src: int, dst: int, k: int) -> int
Example 1:
    Input:  n = 4,
            flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],
            src = 0, dst = 3, k = 1
    Output: 700
    Explanation: 0 -> 1 -> 3 costs 100 + 600 = 700. The path 0 -> 1 -> 2 -> 3
                 is cheaper (400) but uses 2 stops, exceeding k = 1.
Example 2:
    Input:  n = 3,
            flights = [[0,1,100],[1,2,100],[0,2,500]],
            src = 0, dst = 2, k = 1
    Output: 200
    Explanation: 0 -> 1 -> 2 costs 200 with 1 stop.
Example 3:
    Input:  n = 3,
            flights = [[0,1,100],[1,2,100],[0,2,500]],
            src = 0, dst = 2, k = 0
    Output: 500
    Explanation: With 0 stops allowed, only the direct flight 0 -> 2 works.
Constraints:
    - 1 <= n <= 100
    - 0 <= flights.length <= (n * (n - 1)) / 2
    - flights[i].length == 3
    - 0 <= from_i, to_i < n
    - from_i != to_i
    - 1 <= price_i <= 10^4
    - There are no duplicate flights between the same pair of cities.
    - 0 <= src, dst, k < n
    - src != dst
"""


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)  # from : (to, cost)
        step = [float('inf')] * n  # 0th index
        for flight in flights:
            adjList[flight[0]].append([flight[1], flight[2]])

        step[src] = 0
        cheapestFlight = float('inf')

        for _ in range(k + 1):
            prev = step[:]
            for i in range(n):
                if prev[i] == float('inf'):  # not reachable yet
                    continue  # no need to keep computing
                for end, cost in adjList[i]:
                    step[end] = min(step[end], prev[i] + cost)  # keep the same or go from path

            cheapestFlight = min(cheapestFlight, step[dst])
        return -1 if cheapestFlight == float('inf') else cheapestFlight


if __name__ == "__main__":
    s = Solution()

    # Example 1 -> 700
    print(s.findCheapestPrice(
        4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
        0, 3, 1
    ))

    # Example 2 -> 200
    print(s.findCheapestPrice(
        3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
        0, 2, 1
    ))

    # Example 3 -> 500
    print(s.findCheapestPrice(
        3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
        0, 2, 0
    ))
