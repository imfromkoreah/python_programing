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


