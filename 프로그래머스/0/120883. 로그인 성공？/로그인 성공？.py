def solution(id_pw, db):
    user_id, user_pw = id_pw
    for db_id, db_pw in db:
        if user_id == db_id:  # 아이디가 일치
            if user_pw == db_pw:  # 비밀번호도 일치
                return "login"
            else:  # 비밀번호가 틀림
                return "wrong pw"
    # 아이디가 일치하는 회원이 없음
    return "fail"
