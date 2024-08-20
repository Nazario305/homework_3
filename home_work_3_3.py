numbers = [1, 2, 3, 4, 5, 6]

part1 = numbers[: len(numbers) // 2]
part2 = numbers[len(numbers) //2:]

kf = len(numbers) - len(numbers)//2
part3 = numbers[:kf]
part4 = numbers[kf:]

if len(numbers) % 2 == 0:
    print([part1, part2])
else:
    print([part3, part4])

