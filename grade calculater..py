from typing import TypedDict
    
class Record(TypedDict):
    name: str
    score: float
def student_record():
    my_record:Record={"name":"default","score":0.0}
    while True:
         menu={"1":"Add Student Records",
                "2":"Calculate and Display Grades", 
                "3":"Exit"}
         print(menu)
         choice:int=int(input("enter choice:"))
         match choice:
            case 1:
                entered_name=input("enter your name: ")
                entered_score=float(input("enter your score:"))
                
                my_record["name"]=entered_name
                my_record["score"]=entered_score
                
                print(f"{entered_name},{entered_score} is succesfully saved")
            case 2:
                score = my_record["score"]
                if score==100:
                    print("you won O grade\n")
                elif score >= 90:
                    print("grade A\n")
                elif score <=90 and score >= 60:
                    print("grade B")
                else:
                    print("grade C\n")
            case 3:
                print("good bye!")
                break
    return my_record                 




student_record()                       
                   
