# input: numbers = [1, 2, 4, 7, 11, 15, 17, 29, 31], target = 22
# output: [3, 5]
#
# input: numbers = [9, 11, 12, 22, 28, 29], target = 33
# output: [1, 3]

def solution(numbers: list, target: int):
    f = 0
    last = len(numbers)-1
    while f <= last:
        two_sum = numbers[f] + numbers[last]
        if two_sum > target:
            last -= 1
        elif two_sum < target:
            f += 1
        elif two_sum == target:
            return [f, last]
    return -1


print(solution([1, 2, 4, 7, 11, 15, 17, 29, 31], 22))
print(solution([9, 11, 12, 22, 28, 29], 33))
