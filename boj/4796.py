import heapq
n = int(input())

class_list = []
for i in range(n):
    start, ending = map(int, input().split())
    class_list.append((start, ending))

class_list.sort()

apply_list = [] 
for i in range(n):
    start, ending = class_list[i]
    is_adopt = False
    for j in range(len(apply_list)):
        smallest = heapq.heappop(apply_list)
        if smallest <= start:
            heapq.heappush(apply_list, ending)
            is_adopt = True
            break
        else:
            heapq.heappush(apply_list, smallest)
    if not is_adopt:
        heapq.heappush(apply_list, ending)

print(len(apply_list))