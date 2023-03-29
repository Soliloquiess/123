def solution(food):
    food = [i // 2 for i in food[1:]]
    tmp = []
    for idx, count in enumerate(food):
        tmp += [str(idx+1) for i in range(count)]
        
    return ''.join(tmp + ['0'] + sorted(tmp, reverse=True))