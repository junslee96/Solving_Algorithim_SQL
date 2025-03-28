T = int(input())
for _ in range(T):
    C = int(input())
    
    quarter = 25
    dime = 10
    nickel = 5
    penny = 1
    
    quarter_count = C // quarter
    C %= quarter
    dime_count = C // dime
    C %= dime
    nickel_count = C // nickel
    C %= nickel
    penny_count = C
    print(quarter_count, dime_count, nickel_count, penny_count)