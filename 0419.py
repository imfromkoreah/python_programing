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