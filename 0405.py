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

#while
'''
while 조건 :
     수행문1   
else :
     수행문2
''' 
#sum , 0~10까지 숫자를 찍고 sum을 구하자
n = 0
while n < 11 :
     #print("n : ", n)
     sum += n
     print(n, "번째 sum : ", sum)
     #print(n, end="")
     n= n +1

print("while 밖에서 sum의 값 : ", sum)

while False :
     print("실행이 되지 않음")

while 0 :
     print("실행이 되지 않음")

print("while 0 다음 줄입니다.")

#while True :
#     print("무한루프")

#while False :
#     print("실행이 되지 않음")


#break continue
#단어 입력을 무한 루프로 받는다.
# 그 글자를 3번 서 줌
# exit -> 루프를 끝내고 종료함
#"apple" -> 3번 안 쓰고 그냥 다시 단어 입력을 받음.
''' 
<시나리오 구성>
while True :
     단어 입력을 받는다.
     if exit인 경우 :
         break
     elif apple인 경우 :
        continue
     else :
          for : 
          3번 찍는다.
'''

while True : 
     word = input("단어를 입력하세요.")
     if word == "exit":
          print("넌 exit을 입력했고 break를 만날 거야")
          break
          print("break 뒤의 문장")
     elif word == "apple":
          print("넌 apple을 입력했다. continue를 만난다.")
          continue
          print("continue 뒤의 문장")
     else :
          for i in range(3):
               print(word, end='')
          print("해당 단어 끝!")
     print("※ apple을 넣으면 이걸 절대 볼 수 없음!")

#import random

#print(random.randint(0,10000))

from random import randint
#from random2 import randint
print(randint(0,10000))

#놀이동산 놀이기구 탑승 문제
#총 정원 4명
#정원이 차면, 놀이기구 시작
#조건 키 150 이상만 탈 수 있음.
#사람들한테 키를 물어보고, 탑승시키시오.
# 150 이상 4명이 되면 놀이기구를 실행시킴.
#수도 코드를 작성해 볼 것

while True : 
     height = input("키가 몇인가요?")

     if height < 150 :
          print("키가 150이 되지 않아서 놀이기구를 탈 수 없어.")
          break
          print("break 뒤의 문장")
     elif height >= 150 :
          print("넌 키가 150이구나! 탈 수 있겠어")
          continue
          print("continue 뒤의 문장")
     else :
          for i in range(3):
               print(word, end='')
          print("해당 단어 끝!")
     print("※ apple을 넣으면 이걸 절대 볼 수 없음!")
