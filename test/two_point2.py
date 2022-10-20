# input: numbers = [1, 2, 5, 7, 11, 15, 17, 29, 31], target = 22
# output: [[2, 6], [3, 5]]
#
# input: numbers = [1, 3, 6, 9, 10, 11, 13, 22, 28, 29, 31, 39], target = 40
# output: [[0, 11], [3, 10], [5, 9]]

def solution(numbers: list, target: int) -> list:
    result = []
    f = 0
    last = len(numbers)-1
    while f <= last:
        two_sum = numbers[f] + numbers[last]
        if two_sum > target:
            last -= 1
        elif two_sum < target:
            f += 1
        elif two_sum == target:
            result.append([f, last])
            f += 1
            last -= 1
    return result


print(solution([1, 2, 5, 7, 11, 15, 17, 29, 31], 22))
print(solution([1, 3, 6, 9, 10, 11, 13, 22, 28, 29, 31, 39], 40))
