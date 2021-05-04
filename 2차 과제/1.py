# 시험 점수 자동 채점 프로그램

# 세 변수 선언 - 합격기준점수와 최대/최소점수
cut, maximum, minimum = 65, 100, 0

# 수학, 영어, 국어 과목 점수 입력받기
math_score = int(input("수학 과목 점수 : "))
eng_score = int(input("영어 과목 점수 : "))
kor_score = int(input("국어 과목 점수 : "))

# 우선 세 과목의 점수가 0~100사이의 점수인지 따지기
if math_score > maximum or eng_score > maximum or kor_score > maximum:
    print("잘못된 점수가 입력되었습니다")
elif math_score < minimum or eng_score < minimum or kor_score < minimum:
    print("잘못된 점수가 입력되었습니다")
else:
    # 세 점수가 모두 0 ~ 100사이라면, 모든 점수가 합격기준을 넘는지 따지기
    if math_score >= cut and eng_score >= cut and kor_score >= cut:
        print("합격")
    else:
        print("불합격")