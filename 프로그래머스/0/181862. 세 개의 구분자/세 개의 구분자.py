import re
def solution(myStr):
    split_result = re.split('[abc]', myStr)    
    result = [s for s in split_result if s]    
    if not result:
        return ["EMPTY"]    
    return result
