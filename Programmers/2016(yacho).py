def solution(a, b):
    days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']  
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  #(윤년)
    total_days = sum(month_days[:a-1]) + b  # 주어진 날짜까지의 총 일 수 계산
    first_day = 5  # 1월 1일이 금요일이므로 첫 번째 요일은 5 (금요일)
    return days[(first_day + total_days - 1) % 7]  # 첫 번째 요일과 총 일 수를 더한 후, 요일 리스트에서 인덱스를 계산하여 요일을 반환 -1은 1월 1일 뺴는거

# https://school.programmers.co.kr/learn/courses/30/lessons/12901