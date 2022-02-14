case_num = 1
while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    
    cont = v//p
    left = min(v - (p*cont), l)
    print('Case ' + str(case_num) + ': ' + str(l * (v//p) + left))
    case_num += 1
