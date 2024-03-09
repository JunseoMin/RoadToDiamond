def solution(phone_book):
    phone_dict = {}
    
    for number in phone_book:
        phone_dict[number] = 1
        
    for number in phone_book:
        pre = ""
        for numchar in number:
            pre += numchar
            if pre in phone_dict and not pre == number:
                return False
    
    return True


# 빠른 접근에 hash이용 가능
# 길이가 제한된 경우라면 해당 시간 복잡도를 크게 고려할 필요 없음 (전화번호의 길이 == 20)