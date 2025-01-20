#두 정수 입력
H,M=map(int,input().split())
#알람설정
M_alarm = M-45
#M이 0보다 작아질 때만 고려하기
if M_alarm<0:
    H=H-1
    if H == -1:
        H = 23
    M_alarm = 60+M_alarm
print(H,M_alarm)