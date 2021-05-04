# 유저 DB 갱신 프로그램

# 유저 정보를 담을 빈 딕셔너리 만들기
dicUser = {}

# 입력받은 값을 리턴하는 함수 선언
def userInfo(comment):
  val = input(comment)
  return val

# userInfo함수를 통해 이름, 나이, 연락처 입력받아 각 변수들에 저장
name = userInfo("이름 : ")
age = userInfo("나이 : ")
phone_num = userInfo("엽락처 : ")

# update메소드를 통해 dicUser 딕셔너리의 정보를 갱신
# uadate 메소드 - 키의 값(value)를 수정 가능, 키가 없으면 캬-값 쌍을 해당 딕셔너리에 추가함
dicUser.update({'name' : name})
dicUser.update({'age' : age})
dicUser.update({'phone' : phone_num})

# 잘 됐나 확인하기
print(dicUser)
