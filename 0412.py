# 0412
# 자료형 - 리스트, 튜플, 딕셔너리, 집합
# "김밥", "떡볶이", "돈까스"

'''
# 리스트
["김밥","떡볶이","돈까스"]

#튜플
("김밥","떡볶이","돈까스")

딕셔너리 - 사전, apple - 동그란 빨간 과일
{k1:v1, k2:v2}
adress = {"홍길동":"구로구", "김길동":"부천", "박길동":"인천"}

<json 형식>
key:value
"국어":100
"사회:80
'''

#1. 빈 리스트를 만들어서, 하나씩 원소를 추가하는 방식
lst = []
print(type(lst))
lst.append("김밥")
lst.append("햄버거")
lst.append("감자튀김")
lst.append("탕수육") #append라는 메소드를 이용하여 리스트에 추가함. append:요소추가 메소드
print(lst)
lst.append("파스타")
print(lst)
lst.insert(0,"고구마피자") #리스트에 요소 삽입 insert(a,b)는 리스트의 a번째 위치에 b를 삽입.
print(lst)
lst.insert(0,"서브웨이")
print(lst)
print("리스트에서 3번째에 있는 값을 출력합니다: ", lst[2])

lst.append("해장국")
lst.append("감자탕")
print(lst)

#점심메뉴 출력하기
for i in range(len(lst)):
           print(lst[i])
#점심메뉴 출력하기2
for item in lst :
        print(item)

print(lst)
lst.count("탕수육") #리스트에 탕수육이라는 단어가 많을시 탕수육이 몇 번 나왔는지 알려줌

print(lst)
print('lst.count("탕수육")',lst.count("탕수육"))

#slicing
'''
lst[start:end:step] #-> 전체 출력
lst[0,10,1] : 0~(10-1),step수만큼 뛰어 넘어라.
'''
print(lst[::]) #전체 출력
print(lst[0:len(lst):1])
print(lst[0:8:2])

lst.remove("김밥") #리스트 요소 제거 remove(x)는 리스트에서 '첫번째'로 나오는 x를 삭제하는 함수.
print(lst)

#"커피"가 존재하지 않을 때
item1 = "커피"
if item1 in lst :
    lst.remove(item1)
    print("커피 존재함", lst)

else:
    print("커피 존재 안함", lst)
#"커피"가 존재할 때
lst.append("커피")
item1 = "커피"
if item1 in lst :
    lst.remove(item1)
    print("커피 존재함", lst)

else:
    print("커피 존재 안함", lst)

#pop :리스트 요소 끄집어내기 -> 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제함
print(lst)
print("lst.pop() : ", lst.pop())
print(lst)
print("lst.pop(1) : ", lst.pop(1))
print(lst)

# 리스트 추가하여 합치기
dessert = ["케잌","커피","우유","와플","크로플"]
lst.extend(dessert)
print(lst)

'''
x = "15" #String
print(type(x))
# x를 숫자로 바꿈 . +1
print(x + 1) #151 "15" + "1" => 두가지 스트링 합친 값이 나옴.
print(int(x) + 1) #16
print(type(x)) #어떤 타입?


#sort : 리스트의 요소를 순서대로 정리해 준다
l1 = ["orange","apple","mango","kiwi","banana"]
print(l1) #정렬되지 않은 순서대로 나옴
print(sorted(l1)) #정렬된 순서로 나옴

print("=======l1.sort()실행======")
l1.sort()
print(l1)

#reverse : 역순으로 뒤집기
lst.reverse()
print(l1)

l1.clear() #비어있음 l1 = []
print(l1)

del l1
print(l1)
'''

#리스트 컴프리핸션
#리스트를 선언할 때, 짧고 간결하게 하고 싶은 목적.
#0~10까지 숫자가 있는 리스트를 선언하라.
# 1) 그냥 선언
l2 = [0,1,2,3,4,5,6,7,8,9,10]
print("l2 : ", l2)


#2) for문으로 append
l3 = []
for i in range(11) : # 0~10, 0,1,2,3,4,5,....,10
      l3.append(i)
print("l3 : ", l3)

#3) 리스트 컴프리핸션
l4 = [ i for i in range(11)]
print("l4 : ", l4)

# Quiz1 : 0~10까지의 숫자의 제곱을 리스트에 넣어라.
#[0,1,4,9,16,.....,81,100] i**2
a = [i**2 for i in range(11)]
print(a)
'''
같은 방법 => for문으로...
a1 = []
for i in range(11): #0~10
      a1.append(i**2)
'''

# Quiz2 : 0~10까지의 숫자의 3배수을 리스트에 넣어라.
#[0,3,6,9,12,.....,27,30]
b = [i*3 for i in range(11)]
print(b)

# Quiz3 : hello를 10번 넣어라
#['hello','hello','hello',...'hello','hello'] 
c = ["hello" for i in range(11)]
print(c)

#4) 0~10까지 짝수들의 제곱을 리스트에 넣으시오.
#[0,4,16,36,64,...100]
d = [i**2 for i in range(11) if i % 2 == 0]
print(d)

#List를 복사하기
a = [0,4,16,36,64,100]
b = a
a.pop()
print("a : ", a)
print("b : ", b)

a.pop()
print("===after a.pop() ===")
print("a : ", a)
print("b : ", b)

#deep copy
c = a[:] # a[:]
print("deep copy")
print("a : ", a)
print("c : ", c)

a.pop()
print("===after a.pop()===")
print("a : ", a)
print("b : ", b)
print("c : ", c)

c.append(555)
print("===after c.pop(555)===")
print("a : ", a)
print("b : ", b)
print("c : ", c)


