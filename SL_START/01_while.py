'''
사용자가 0을 입력할 때까지
사용자가 원하는 구구단 출력하기

[문제 분석]
무한 반복 - while True
사용자가 0을 입력 할 때까지 계속 단을 입력 받는다.

사용자가 0을 입력 했는지 아닌지를 판단.

구구단은 곱하는 수가 1~9까지 1씩 증가한다.
'''

#알고리즘
#1.입력 받는다.
#       1)단을 입력 받는다.
#       2)만약에 입력 값이 0인가?
#               a.프로그램을 종료한다.  break
#       3)곰하는 수를 1부터 10까지 반복하면서
#               a.구구단을 출력한다
#2."구구단 종료" 출력한다



while True:
    dan=int(input("단을 입력 :"))
    if dan==0:
        break
    #else: #else를 사이에 껴도 가능
    su=1    #초기값     /   초기값은 while 시작전에 해야함.
    while su <= 9 :     #조건식
        print("{} * {} = {}".format(dan, su, dan*su))
        su = su+1   #증감식
print("구구단 종료")