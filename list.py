list=[1,10,5,2,3,4]
# print(list.index(10))
#  print(list)
#  for i in list:
#     print(i, end=" ")

# list.append(5)
# list.insert(2,10)
# list1=[6,7,8,9]
# list.extend(list1)

# list.remove(10)
# list.clear()
# list.sort()
# print(list)
# print(len(list))

num=int(input("Enter an number of student: "))
std_lst=[]
for i in range(num):
    
    marks=int(input(f"Enter an marks {i+1}:"))
    std_lst.append(marks)

print(std_lst)
print(max(std_lst))
print(min(std_lst))