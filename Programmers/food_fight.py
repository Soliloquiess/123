def solution(food):
    food = [i // 2 for i in food[1:]] # 물은 0칼로리이므로 제거하고, 2로 나눔.
    tmp = [] 
    for idx, count in enumerate(food):
        tmp += [str(idx+1) for i in range(count)]
        # List Comprehension : 인덱스 + 1 이 칼로리 역할을 하고, 인덱스의 val가 개수를 의미하므로 개수만큼 반복하며 인덱스를 값으로 갖는 리스트를 생성
        # ex) [1, 3, 2] -> 122233
        
    return ''.join(tmp + ['0'] + sorted(tmp, reverse=True)) # 0을 기준으로 tmp를 대칭한 리스트를 문자열로 반환


# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/134240
