n = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))

min_oil = oil[0]
result = 0

for i in range(len(oil)-1):
    if min_oil > oil[i]:
        min_oil = oil[i]
    result += (min_oil * road[i])
print(result)


## first solve code 
# n = int(input())
# road = list(map(int, input().split()))
# oil = list(map(int, input().split()))

# left = [i for i in road]
# for i in range(len(road)-1, 0, -1):
#     left[i-1] += left[i]
# left.append(0)

# values = []
# for i in range(len(road)):
#     values.append((oil[i], i, left[i]))

# values.sort()
# now_index = n-1
# result = 0
# for val in values:
#     if now_index < val[1]:
#         continue
#     result += (val[0] * (val[2] - left[now_index]))
#     now_index = val[1]
# print(result)

