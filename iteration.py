# for 변수 in 리스트(또는 튜플, 문자열):
#     수행할 문장1
#     수행할 문장2


# for, while
#
# for i in range(5):
#     print ("반복문")

# for i in range(1,6,1):#1~6까지 스텝은 1
#     print (i, end=" ")

    #10 부터 시작해서 1까지

# for i in range(10,0,-1):
#     print(i, end=" ")

#1~100까지의 합을 구하라
# sum=0
# for i in range(1,101):
#     sum+=i
# print(sum)
#
# def pow(a):
#     if(a==1):
#         return 1
#     return a*pow(a-1)
# n=int(input("정수를 입력\n"))
# print(pow(n))
#while로 1~100 합
# count=1
# sum=0
# while True:
#     sum+=count
#     count=count+1
#     if count>100:
#         break
# print (sum)
#암호 입력후 안맞으면 반복
# password='python'
# while(True):
#     pw=input("암호를 입력하시오\n")
#     if(pw==password):
#         break
#for써서 *10개 5번
# for i in range(5):
#     for q in range(10):
#         print('*',end='')
#     print()

#직각 삼각형
# for i in range(5):
#     for w in range(i+1):
#         print("*" ,end ="")
#     print()

# test_list=['one','two','three']
# for i in test_list:
#     print (i)
# a=[(1,2),(3,4),(5,6)]
# for (f,s) in a:
#     print(f,s)
# marks=[90,25,67,45,80]
# number=0
# for mark in marks:
#     number=number+1
#     if mark>=60:
#         print("%d=pass"%number)
#     else:
#         print ("%d=fail"%number)

#range(10)는 0~10 미만의 숫자의 리스트를 만들어준다
#range(10)=range(0,10)   10은 미포함


#무한 반복을 이용한 신호등
# sign = True
# while sign:
#     light=input("식호등 색을 입력하시오\n")
#     if(light=='blue'):
#         break

#악보를 연주하는 순서를 출력하는 프로그램을 반복문을 이용하여 작성하시오
# ab(도돌이표)cd(도돌이표)
#abcdcd
print("연주순서")
print("A", end=" ")
print("B", end=" ")
for i in range(2):
    print("C", end=" ")
    print("D", end=" ")



