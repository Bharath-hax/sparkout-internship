student_rec=[]

print("***enter the student name and marks***")
name=input("enter name of the student :")
mark=input("enter the mark of the student:")

student_rec.append([name,mark])
for name,mark in student_rec:
    e_name=input("enter ur name as same as in ur record")
    if name==e_name:
       new_mark=input("enter the new mark u want to update")
       student_rec.update([new_mark])
       print([name,mark])

    
         
