def solution(a, b, n):
    answer = 0
    empty_bottles = n  
    while empty_bottles >= a:  # a개 이상의 빈 병이 있을 때까지 반복
        exchanged_bottles = empty_bottles // a  # a개의 빈 병으로 교환 가능한 콜라 병의 개수
        answer += exchanged_bottles * b  # 콜라 병의 수 업데이트
        empty_bottles = empty_bottles % a + exchanged_bottles * b  # 새로운 빈 병의 개수 업데이트
    return answer