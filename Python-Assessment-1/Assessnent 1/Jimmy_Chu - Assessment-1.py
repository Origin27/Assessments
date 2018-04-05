#Jimmy Chu , Jimmycar321@gmail.com
#Assessment 1
#Date: 05/04/2018

#---------------------------------------------------------------------
#Declaring the appropiate variables to later use 
grade_a_plus = "A+"
grade_a = "A"
grade_b = "B"
grade_c = "C"
grade_fail = "Fail"
 
course_code = "DTEC101"
 
#---------------------------------------------------------------------
#asking the user for their first name and last name 
first_name = input("Please enter your first name: ").strip()
first_name = first_name.capitalize()

last_name = input("{}, please enter your last name: ".format(first_name)).strip()
last_name = last_name.capitalize()

#---------------------------------------------------------------------
#checking the users mark to see what grade they got or if they inputted a valid mark

problem = True
 
while problem:
    user_mark = input("{}, please enter your mark for assessment 1: ".format(first_name))



    if user_mark.isdigit():

        user_mark = int(user_mark)
        
        if user_mark <= 100 and user_mark >= 95:                    
                user_grade = grade_a_plus
                problem = False
                pass_mark = True
        elif user_mark <= 94 and user_mark >= 90:                    
                user_grade = grade_a
                problem = False
                pass_mark = True
        elif user_mark <= 89 and user_mark >= 70:                    
                user_grade = grade_b
                problem = False
                pass_mark = True
        elif user_mark <= 69 and user_mark >= 50:                    
                user_grade = grade_c
                problem = False
                pass_mark = True
        elif user_mark <= 49 and user_mark >= 0:                   
                user_grade = grade_fail
                problem = False
                pass_mark = False
        elif user_mark > 100:
            print("Sorry {}, {} was too high. Please re-enter the mark.".format(first_name, user_mark))            
        
    else:
        print("Sorry {}, {} was too low. Please re-enter the mark.".format(first_name, user_mark))
        
#---------------------------------------------------------------------
#telling the user what grade they got and also if they passed the assessment. 

if pass_mark == True:
    print("Congratulations {} {}, you have passed {} with a grade of {}.".format(first_name, last_name, course_code, user_grade))
else:
    print("Unfortunately {} {}, you have not passed {}. You received the grade {}.".format(first_name, last_name, course_code, user_grade))


