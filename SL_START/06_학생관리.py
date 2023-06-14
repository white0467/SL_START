'''
"학생 관리" 프로그램을 작성하시오.

이 프로그램은 종료 시킬 때까지 무한 반복된다.
- "작업 선택 : " 에서 0 입력 시 프로그램이 종로된다.
- "작업 선택 : " 에서 1 입력 시 관리하는 학생 목록이 조회된다.
- "작업 선택 : " 에서 2 입력 시 학생을 추가할 수 있다.
- "작업 선택 : " 에서 3 입력 시 학생을 삭제할 수 있다.
이때 입력한 학생은 관리하는 학생 목록에 있는 데이터만 삭제 가능하도록 하며
목록에 없는 학생을 삭제하고자 합 때는
'삭제할 학생이 없습니다. 다시 입력하세요!'를 화면에 출력한다.
'''
student=[]

print("===================")

print("::: 학생관리 :::")
print("0. 종료")
print("1. 학생 조회")
print("2. 학생 추가")
print("3. 학생 삭제")
print("==================")

while True:
    job=int(input("작업 선택 : "))
    if job == 1:
        print("학생 조회 :", student)
    elif job == 2:
        student.append(input("2. 학생 추가"))
    elif job == 3:
        del_student=input("삭제 할 학생 입력 :")
        if student.count(del_student) == 0:
            print("삭제 할 학생이 없습니다")
            continue
        else:
            student.remove(del_student)
    elif job == 0:
        print("프로그램을 종료")
        break
