Total_credits = 0 #학점 합계
Total_score = 0.0 #점수 합계
score = {'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}
for _ in range(20):
    a,b,c = input().split()
    if c != 'P':
        Total_credits += float(b)
        Total_score += score[c] * float(b)
print(Total_score/Total_credits)                