def solution(babbling):
    pronounce = ["aya", "ye", "woo", "ma"]
    answer = 0
    for word in babbling:
        temp = word
        for p in pronounce:
            # 연속된 같은 발음이 있는지 확인
            if p * 2 in temp: 
                break
            # 발음 가능한 단어를 제거
            temp = temp.replace(p, " ")
        # 빈 문자열인 경우 카운트
        # strip()으로 공백 문자 제거
        if temp.strip() == "":
            answer += 1
    return answer
