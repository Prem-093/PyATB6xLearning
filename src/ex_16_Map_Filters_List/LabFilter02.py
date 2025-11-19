nums=[1,2,3,4,5,6]

def even_num(x):
    return x%2==0

evennum=list(filter(even_num,nums))
print(evennum)


list_student=[48,47,49,50,52,51]

def student(marks):
    if marks>50:
        return True


selected_student=list(filter(student,list_student))
print(selected_student)

list_student=[48,47,49,50,52,51]

def student(marks):
    if marks<50:
        return True


selected_student=list(filter(student,list_student))
print(selected_student)