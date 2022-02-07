n = int(input())

meet = []
for i in range(n):
    start, ending = map(int, input().split())
    meet.append((ending, start))

meet.sort()

answer = 0
now_ending = 0
for i in range(n):
    ending, start = meet[i]
    if start >= now_ending:
        answer += 1
        now_ending = ending
print(answer) 

