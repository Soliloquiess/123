# # 1. 재귀함수
# def cola_div(a, b, n):
#     if a <= n:
#         free = (n // a) * b
#         return cola_div(a, b, n % a + free) + free
#     return 0
    
# def solution(a, b, n):
#     return cola_div(a,b,n)
    
# 2. 반복문
def solution(a, b, n):
    answer = 0
    while a <= n:
        free = n // a * b
        answer += free
        n = n % a + free
    return answer

if __name__ == '__main__':
    print(solution(2, 1, 20)) # Answer = 19
    print(solution(3, 1, 20)) # Answer = 9
