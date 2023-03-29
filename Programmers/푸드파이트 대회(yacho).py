def solution(food):
    food_str = ''
    for i in range(1, len(food)):
        food_str += str(i) * (food[i] // 2)
    food_str += '0' + food_str[::-1]    #완성후 0부터 역순으로 만든다.
    return food_str

print(solution([1, 3, 4, 6]))
print(solution([1, 7, 1, 2]))

# https://school.programmers.co.kr/learn/courses/30/lessons/134240
