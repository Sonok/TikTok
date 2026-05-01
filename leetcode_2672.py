from typing import List


problem_2672 = """
2672. Number of Adjacent Elements With the Same Color

You are given an integer n representing an array `colors` of length n where all
elements are initially 0 (uncolored). You are also given a 2D array `queries`
where queries[i] = [index_i, color_i].

For the i-th query:
    1. Set colors[index_i] = color_i.
    2. Count the number of adjacent index pairs (j, j+1) such that
       colors[j] == colors[j+1] AND both are colored (non-zero).

Return an array `answer` of the same length as `queries`, where answer[i] is
the count after the i-th query.

Function signature:
    def colorTheArray(n: int, queries: list[list[int]]) -> list[int]

Example:
    Input:  n = 4, queries = [[0,2],[1,2],[3,1],[1,1],[2,1]]
    Output: [0, 1, 1, 0, 2]
"""


class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        if n == 1:
            return [0] * len(queries)

        answer = []          # return value
        colors = [0] * n     # ledger
        pairs = 0

        for query in queries:
            i, color = query[0], query[1]

            if colors[i] == color:  # no change
                answer.append(pairs)
                continue

            if i == 0:
                if colors[i] > 0 and colors[i] == colors[i + 1]:
                    pairs -= 1
                elif color == colors[1]:
                    pairs += 1
            elif i == n - 1:
                if colors[i] > 0 and colors[i] == colors[i - 1]:
                    pairs -= 1
                elif color == colors[i - 1]:
                    pairs += 1
            else:
                # left neighbor
                if colors[i] > 0 and colors[i] == colors[i - 1]:
                    pairs -= 1
                elif color == colors[i - 1]:
                    pairs += 1
                # right neighbor
                if colors[i] > 0 and colors[i] == colors[i + 1]:
                    pairs -= 1
                elif color == colors[i + 1]:
                    pairs += 1

            colors[i] = color
            answer.append(pairs)  # set the final value

        return answer


if __name__ == "__main__":
    s = Solution()

    # Main example -> [0, 1, 1, 0, 2]
    print(s.colorTheArray(4, [[0, 2], [1, 2], [3, 1], [1, 1], [2, 1]]))

    # Edge: n = 1 with multiple queries -> [0, 0, 0]
    print(s.colorTheArray(1, [[0, 1], [0, 2], [0, 3]]))

    # Edge: repeated same color -> [0, 0]
    print(s.colorTheArray(3, [[0, 5], [0, 5]]))
