#문자열
str = "파이썬수업1 파이썬수업2 파이썬 씨수업3 파이썬수업4 파이썬수업5 파이썬수업6"

#split
print(str.split(",")) 
# -> ","로 구분해 줘

#join
#내가 원하는 스트링 "**" 을 사이사이에 끼워달라는 뜻
print("**".join(str))

#format의 목적
print(3, "+", 4, "=", 7) #원래 방식
f1 = "{} + {} = {}"
f = "{} + {} = {}".format(3,4,7)
f2 = "{0} + {1} = {2}, {2}, {2}".format(3,4,3+4)
f3 = "{0:d} + {1:f} = {2:f}, {2}, {2}".format(3,4.0,3+4.0)  #형식 알려주기 (써도 되고 안 써도 됨.)
f4 = "{0:10d} + {1:10f} = {2:10.3f}".format(3,4.0,3+4.0)  #칸수만큼 공간을 주고 찍어라!/..
print(f2)
print(f3)
print(f4)

#replace
print(str.replace("파이썬","자바",3))  #앞단에 있는 세 숫자만 바꿔줘~

#count
print(str.count("파이썬")) #파이썬이라는 글자가 몇 번 있는지 찾아줌.

#find, index
'''
print("find: ", str.find("파이썬"), "index : ", str.index("씨"))
print(str.find("AI"))  #str에서 AI위치를 알려줘 -> "AI" 라는 단어 없다고 판단 -> retrun값을 -1로 반환
print(str.index("AI")) #str에서 AI위치를 알려줘 -> "AI" 라는 단어 없다고 판단 -> error 냄
'''

#boolean(true, false)
print(type(True),type(False))
a = "hello"
print(bool(a))
print(bool("hello"), bool("hi"), bool(3), bool(-3)) #true
print(bool(""),bool(0)) #false 빈문자, 0

#조건문
'''
if 조건1 :
    실행문1
else :
    실행문2
'''

#오전/오후
h = 9
if h < 12 :
    #h가 12보다 작을 때
    print("오전", h, "가 12보다 작다.")
else :
    #실행문2
    #h가 12보다 크다.
    print("오후 ", h, "는 12보다 크다.")

h = 10
if h < 12 :
    print("오전 ", h, "가 12보다 작다") #h가 12보다 작을 때
elif h < 18 : # 12 < h < 18
    print("오후 ", h, "가 12보다 크고 18보다 작음")
else : # 18 < h
    print("저녁", h, "는 18보다 크다.")

lunch = input("밥 먹을래?")
if lunch == "yes" :
    print("밥을 먹고 싶군요")
    cafeteria = input("학식 고?")
    if cafeteria == "yes" :
        print("학식당으로 가자")
    else :
        print("학식 싫구나")
        subway = input("서브웨이 가실?")
        if subway == "yes" :
            print("서브웨이 가자")
        else :
            print("서브웨이도 싫어?")
else :
            print("밥 먹지 마")

# for, while 반복문
# in range
for i in 1,2,3,4,5,6 :
    print("i: ", i)

#range
for i in range(0,20,1): #0에서 19까지 1씩 증가
     print("i : ", i)

for i in range(20):
     print("i : ", i)

for i in range(1,21,2): #20까지 수 중 짝수만 출력
     print("i : ", i)

#1부터 10까지 합을 구하시오
#2가지 방법으로, range도 쓰고, 그냥 명시도 하고...
sum = 0
for i in 1,2,3,4,5,6,7,8,9,10 :
    sum = sum + i
    #sum += i
    print(i , "번째 loop입니다. sum은 ", sum , "입니다.")

print("range를 사용하였음")
sum = 0
for i in range(1, 11, 1) :
     sum += i
     #sum = sum + i
     print(i, " 번째 loop입니다. sum은" , sum , "입니다.")
