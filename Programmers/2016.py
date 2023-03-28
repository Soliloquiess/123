def solution(a, b):
    
    day_to_week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    month_to_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    return day_to_week[(sum(month_to_day[:(a-1)]) + b - 1) % 7]