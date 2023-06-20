'''
학과 : 컴퓨터공학부
학번 : 202395034    
이름 : 한유진

학생 정보를 사전에 저장하고, (학번, 이름)
특정 학생의 정보(학번)를 입력하여 학생을 찾아주세요.

[알고리즘]
1. 학생 정보 저장 사전 만들기 - 빈 사전 만들기
2. 학생 정보 입력 - 사전에 저장 (z 키를 누르면 종료 - 무한 반복)
3. 학번으로 검색하여 학생 찾기 (학번이 빈칸이면 검색 종료 - 무한 반복)
'''
student = {}

print("::학생 정보 입력::")
while True :
    student_id = input("추가 하실 학생의 학번을 입력하시오 : ")
    if student_id == 'z':
        print("입력 종료")
        break
    student_name = input("추가 하실 학생의 이름을 입력하시오 : ")
    if student_name == 'z':
        print(student)
        print("입력 종료")
        break
    student[student_id] = student_name

print("학생 검색")
while True :
    student_id = input("찾으실 학생의 학번을 입력하시오 : ")
    if student_id == '':
        print("프로그램 종료")
        break
    elif student_id in student:
        print('찾으시는 학생의 정보는 : {}'.format(student[student_id]))
    else :
        print("찾으시는 학생이 없습니다.")
    