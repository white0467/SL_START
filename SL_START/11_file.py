'''
랜덤으로 10명의 학생의 키와 몸무게 생성하여 파일에 저장
'''

import random

f_name=list('김이박서차전한소남조홍')
a_name=list('가나다라마바사아자차카타파하')

with open("C:/대학sw/info.txt","w") as f:    #파일 객체
    for i in range(10):
        print(i)
# with open("C:/대학sw/info.txt","w") as file:
#     for i in range(10):
#         # name=random.choice(f_name) + random.choice(a_name) + random.choice(a_name)
#         # weight=random.randrange(40, 100)
#         # height=random.randrange(140, 200)

#         # file.write("{}, {}, {} \n".format(name, weight, height))

#         print(i)