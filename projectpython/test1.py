l = [1, [2, 3, [4]], 5, [[6], [7]], 8, [[[9]]]]
#result = 45

for i in range(len(l)):
     

# l = [1, [2, 3, [4]], 5, [[6], [7]], 8, [[[9]]]]
# result = 45
from typing import List


def sum_recursion(lst: List[int | List]) -> int:
    result: int = 0
    for item in lst:
        if isinstance(item, int):
            result += item
        else:
            result += sum_recursion(item)

    return result


l = [1, [2, 3, [4]], 5, [[6], [7]], 8, [[[9]]]]
print(sum_recursion(l))