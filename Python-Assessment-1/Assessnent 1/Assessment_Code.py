# This is NOT the correct answer for this assessment.
# You MUST modify this code and make it satisfy the specification.
 
# Do NOT modify anything inside the quotation marks "".
 
score1 = 95
score2 = 90
score3 = 70
score4 = 50
  
grade1 = "A+"
grade4 = "A"
grade3 = "B"
grade7 = "C"
grade5 = "Fail"
 
course1 = "DTEC101"
 
mn = 0
mx = 100
mid = 50
 
name1 = input("Please enter your first name: ")
name2 = input("{}, please enter your last name: ".format(name1))
 
 
bigproblem = True
 
while bigproblem == True:
    number = input("{}, please enter your mark for assessment 1: ".format(name1))
    if (number == mx):
         print("Sorry {}, {} was too low. Please re-enter the mark.".format(name1, number)) 
    print("Sorry {}, {} was too high. Please re-enter the mark.".format(name1, number))
    bigproblem = False
 
 
if number == score1:
    grade = grade1
elif number == score3:
    grade = grade7
else:
    if number == score3:
        grade = grade3
if number == score4:
    grade = grade4
else:
    grade = grade5
 
    if number == mx:
        print("Congratulations {} {}, you have passed {} with a grade of {}.".format(course1, name2, grade, name1))
    print("Unfortunately {} {}, you have not passed {}. You received the grade {}.".format(course1, name2, grade, name1))
