student_dict={}
num=int(input("Enter an number of student:"))
for i in range(num):
    name=input(f"Enter an Name {i+1}:")
    marks=int(input(f"Enter an marks{i+1}:"))
    student_dict[name]=marks

max_marks=int(input("Enter an pass marks:"))
for key,value in student_dict.items():
    if value>=max_marks:
        print(f"Student name is {key} and marks is {value}")



        
print(student_dict)
