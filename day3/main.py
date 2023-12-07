# Part 1

import string

def get(lst, n):
    try:
        a = lst[n]
    except IndexError:
        a = '.' 
    return a

def get_surroundings(data, i):
    return [get(data, i-139), get(data, i-140), get(data, i-141),get(data, i-1), get(data, i), get(data, i+1), get(data, i+139), get(data, i+140), get(data, i+141)]   

with open('input.txt') as f:
    data = f.read()

data = data.replace('\n', '')

i = 0
total = 0
while i < len(data):
    c = data[i]
    # another period, dont care
    # some punctuation, dont care
    if c == '.' or c in string.punctuation: 
        i += 1
        continue
    # ooooh a digit, start checking the surrounding chars
    if c.isdigit():
        num = []
        surroundings = get_surroundings(data, i) 
        num.append(c)
        i += 1
        while get(data, i).isdigit():
            surroundings = surroundings + get_surroundings(data, i)
            num.append(get(data, i))
            i += 1
        # check surrounding for part
        for s in surroundings:
            if s == '.':
                continue  
            if s in string.punctuation:
                total += int(''.join(num))
                break
        # print(f"{num}{surroundings}")
print(total)
# 539713


# Part 2

def get_num(data, start):
    num = []
    n = start
    print(f"get_num: {start}, {n}, {num}, {get(data, n)}")
    if  get(data, n-1).isdigit() is False and get(data, n+1).isdigit() is False:
        return int(get(data, n))
    while get(data, n-1).isdigit():
        n -= 1
    while get(data,n).isdigit():
        print(f"get_num: {n} get: {get(data,n)}")
        num.append(get(data,n))
        n += 1
    return int(''.join(num))

i = 0
total = 0
while i < len(data):
    if data[i] == '*': 
        surroundings = get_surroundings(data, i) 
        # check if there is a number both to the right and left of the * 
        if True in [x.isdigit() for x in surroundings[0:4]] and True in [x.isdigit() for x in surroundings[5:9]]:
            print("============")
            nums = []
            # now have to find the numbers in each row 3x3 with the * in the center
            # first row
            cols = [x.isdigit() for x in surroundings[0:3]]
            print(f"first row:{cols}{surroundings[0:3]}")
            for ci, col in enumerate(cols):
                if col is True:
                    num = get_num(data,i-139+ci)
                    print(f"{col} {ci} {i} start: {i-139+ci} number: {get(data,i-139+ci)} returned_num: {num}")
                    nums.append(num)
            # get(data, i-139), get(data, i-140), get(data, i-141)
            # print(f"{i}{surroundings}")
            # second row, the one with *
            print(f"second row:{cols}{surroundings[3:6]}")
            cols = [x.isdigit() for x in surroundings[3:6]]
            # print(f"second row:{cols}{surroundings[3:6]}")
            for ci, col in enumerate(cols):
                if col is True:
                    # print(f"{col} {ci} {i} start {i-1+ci}, number {get(data,i-1+ci)}")
                    num = get_num(data,i-1+ci)
                    print(f"{col} {ci} {i} start: {i-1+ci} number: {get(data,i-1+ci)} returned_num: {num}")
                    nums.append(num)
            # get(data, i-139), get(data, i-140), get(data, i-141)
            # print(f"{i}{surroundings}")
            # third row
            print(f"third row:{cols}{surroundings[6:9]}")
            cols = [x.isdigit() for x in surroundings[6:9]]
            # print(f"second row:{cols}{surroundings[6:9]}")
            for ci, col in enumerate(cols):
                if col is True:
                    # print(f"{col} {ci} {i} start {i+139+ci}, number {get(data,i+139+ci)}")
                    num = get_num(data,i+139+ci)
                    print(f"{col} {ci} {i} start: {i+139+ci} number: {get(data,i+139+ci)} returned_num: {num}")
                    nums.append(num)
            print(f"{surroundings}")
            print(nums)
            nums = list(set(nums))
            if len(nums) == 2:
                total += nums[0]*nums[1]
            else:
                total += nums[0]
    i += 1
print(total)
