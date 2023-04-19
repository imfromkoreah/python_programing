#0419 _ 6장

#list
l1 = [1,2,3,4,5]
#tuple _ 수정 불가
t1 =(1,2,3,4,5,6,4,5,4,3,2,1,2,3)
print(l1)
print(t1)
print(t1.count(2)) #2가 몇 번 나오는지 출력
print(t1.index(3)) #2가 몇 번째에 나오는지

#커피숍 프로그램
menu = ("아메","라떼","자몽차")

# 아이스티 추가 _ menu1 튜플을 새로 만들어 추가함.
menu1 = ("아메","라떼","자몽차","아이스티")

# 리스트로 바꾼 후 추가하는 방법
menu1 = list(menu)
menu1.append("디카페인")
print(menu1)
menu = tuple(menu1)
print(menu)

t2 = ()
print(t2)
t3 = 10,20,30,40,50 #괄호를 사용하지 않아도 튜플로 인식
print(t3)

t4 = 10, #int 뒤에 ',' 사용시 튜플로 전환됨.
print(type(t4))
print(t4)

'''
lst = [10,20,30,44,5,6,1,1]
lst.sort() #원본이 바뀜
sorted() #원본이 바뀌진 않지만 다른 리스트로 바꿔서 정렬
'''

t5 = 1074,205,3,1,78
print("sorted(t5) : ", sorted(t5))
print("t5: ",t5)

t10 = 1,2,3,4,5
for i  in 1,2,3,4,5 :
    print(i)

#dictionary
#key 와 value의 페어. {Key1:Value1, Key2:Value2,...}
'''
d1 = {k1:v1, k2:v2, k3:v3, k1:v4} #k1,k2,k3는 중복 불가, v값은 중복 가능.
'''
student = {}
d2 = dict() #dictionary로 만드는 함수.

#사전에 값을 추가하자.
# 1) 추가 방법 1
student[101] = '홍길동'
student[102] = '이보경'
student[103] = '그레이' #키 103에 대응되는 value값 추가
print(student)

print("student[101] : ", student[101])
print("student[102] : ", student[102])
print("student[103] : ", student[103])

lec = {}
lec['강좌명'] = '파이썬'
lec['개설년도'] = 2023 #문자형 -> int 바뀌어도 적용됨.
lec['수강생'] = ['홍','김','박','고'] 
lec['인원'] = 35
print(lec)

#인원수를 변경하는 방법1 
lec['인원'] = 20 #인원key에 대한 value를 20으로 변경함
print(lec)

#인원수를 변경하는 방법2 update 사용
lec.update({'인원':10})
print(lec)

lec.update({'강의실':213, '교수':'이희진'}) #새로운 key값 추가하는 방법
print(lec) #추가 가능함. update키: 동일한 key에 대한 값을 변경하는 것도 가능하고
                        #존재하지 않는 값에 대해서는 새로운 key로 추가하는 것도 가능.

#월 (총 12개의 원소가 있는 dictionary)
month = {'k1':'1월','k2':'2월','k3':'3월','k4':'4월','k5':'5월','k6':'6월','k7':'7월','k8':'8월','k9':'9월','k10':'10월','k11':'11월','k12':'12월'}

#결과출력해보기
'''
1월
2월
3월
'
'
'
11월
12월
''' 
'''
print('=====#1=====')
for key in range(1,13): #1,2,3,4,...,12
    print(month[key])   

print('=====#2=====')
for key in 1,2,3,4,5,6,7,8,9,10,11,12 :
    print(month[key]) 

print(month.keys())
print(month.values())
print(month.items())
'''

print('=====#3=====')
#month.keys()
print(month.keys())
for i in month.keys() : #[k1,k2,k3,k4,k5,k6,...,k12]
    #month[key] => value
    print(month[i])

print('=====#4=====')
#month.values()
for v in month.values() : #[1월,2월,3월,...,12월]
    print(v)

print('=====#5=====')
#month.items()
for item in month.items() :
    print(item)

print('=====#6=====')
#month.items()
for item in month.items() :
    # item -> (k1,v1)
    print("key   : ", item[0])
    print("value : ", item[1])
    print("   ")
#key: xxx
#value: xxx

for haha in month :
    print(haha) #key값만 출력

print(month.get('k1'))
print(month.get('k100'))
print(month['k1'])
print(month['k100'])

#dictionary 삭제
print(month)
print("month.pop('k1'): ",month.pop('k1')) #key값을 줘야 함
print(month) #2월부터 출력 k1 삭제됨.
print("month.popitem(): ",month.popitem()) #맨 마지막 것을 삭제함.
print(month) #2월부터 11월까지 존재함.

