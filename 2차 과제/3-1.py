# 과일채소가게 상품관리 프로그램

# 과알 카테고리인 fruit와 채소 카테고리인 vegetable이란 리스트 생성
fruit = ['사과', '오렌지', '포도']
vegetable = ['당근', '호박', '오이']

# 함수 정의 - 카테고리와 상품명을 파라미터로 받는다
def friut_or_vegetable(category, product_name):

    # 우선 카테고리가 과일인지 채소인지 다른 것인지 먼저 판단
    if category == "과일":
        # 만약 카테고리가 과일인데, fruit리스트에 없는 상품이라면 fruit리스트에 해당 품명 추가
        if product_name not in fruit:
            fruit.append(product_name)
        else:
            print("이미 등록된 과일입니다.")
    elif category == "채소":
        # 만약 카테고리가 채소인데, vegetable리스트에 없는 상품이라면 vegetable리스트에 해당 품명 추가
        if product_name not in vegetable:
            vegetable.append(product_name)
        else:
            print("이미 등록된 채소입니다.")
    else:  
        print("존재하지 않는 카테고리입니다")


# 카테고리와 품명 입력받기
category = input("품종이 뭔가요? : ")
product_name = input("품명은요? ")

# 입력받은 값을 파라미터로 넘겨 함수 실행
friut_or_vegetable(category, product_name)

# 리스트 출력
print(fruit)
print(vegetable)