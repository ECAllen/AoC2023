
# First problem 
with open('input.txt') as f:
    data = f.read().splitlines()

total = 0
for line in data:
    nums = ''
    for c in line:
        if c.isdigit():
            nums += c
    new_num = f"{nums[0]}{nums[-1]}" 
    total += int(new_num)
print(f"{total}")

total = 0
for line in data:
    for c in line:
        if c.isdigit():
            first_digit = c
            break
    for i in range(len(line)-1, -1, -1):
        if line[i].isdigit():
            last_digit = line[i]
            break
    total += int(f"{first_digit}{last_digit}")
print(f"{total}")

# Second problem 
total = 0
digits = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
for line in data:
    first_digit = None
    for i in range(len(line)+1):
        if line[i].isdigit():
            first_digit = line[i]
            break
        for digit in digits:
            if digit in line[0:i]:
                first_digit = digits[digit]
                break 
        if first_digit is not None:
            break

    last_digit = None
    for i in range(len(line)-1, -1, -1):
        if line[i].isdigit():
            last_digit = line[i]
            break
        for digit in digits:
            if digit in line[i:]:
                last_digit = digits[digit]
                break 
        if last_digit is not None: 
            break
    total += int(f"{first_digit}{last_digit}")
print(f"{total}")


# Second problem v2 
# fix the ugly breaks above yuck
total = 0
digits = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
for line in data:
    first_digit = None
    i = 0
    while first_digit is None and i <= len(line)+1:
        if line[i].isdigit():
            first_digit = line[i]
        else:
            for digit in digits:
                if digit in line[0:i]:
                    first_digit = digits[digit]
                    break 
        i += 1

    last_digit = None
    i = len(line)-1
    while last_digit is None and i >= 0:
        if line[i].isdigit():
            last_digit = line[i]
        else:
            for digit in digits:
                if digit in line[i:]:
                    last_digit = digits[digit]
                    break 
        i -= 1

    total += int(f"{first_digit}{last_digit}")
print(f"{total}")



