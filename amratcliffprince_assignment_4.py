
student_name = "Amya"
current_gpa = 3.5     # Float between 1.0-4.0
study_hours = 20      #Integer (Ex. 25)
social_points = 30    # Integer (Ex. 50)
stress_level = 50     # Integer 0-100
#welcom stats
print(f" Welcome {student_name} to your Academic Profile!")
print(f"Current GPA: {current_gpa:.2f}")
print("Study Hours:", study_hours)
print("Social Points:", social_points)
print("Stress Level:", stress_level) 

#step 2
print("Choose your course load:")
print("A) Light (12 credits)")  
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")

#choice input 
choice = input("Your choice: ")
#light course load= less stress, and fewer study hours
if choice == "A":
    study_hours = study_hours - 5
    stress_level = stress_level - 10 
    print("You chose a Light Load. Less stress")
elif choice == "B":      #standard load, balanced
    if current_gpa >= 2.5:
        study_hours = study_hours + 5
        stress_level = stress_level + 5
        print("Standard load could be a little overwhelming with your GPA")
elif choice == "C":     #hevay load, harder depending on GPA
    if current_gpa >= 3.5:
        study_hours = study_hours + 10 
        stress_level = stress_level + 10 
        print(" You chose a Heavy load. Challenging but possible with your GPA! ")
    else:
        study_hours = study_hours + 8 
        stress_level = stress_level + 25
        print("You chose a Heavy load. High stress can put your GPA at risk!")
else:
    print("Invalid choice. Please restart and select A,B, or C.")

#Study strategy decisions 
#list of study options 
study_options = ["Programming", "Math", "English", "History"]

#shows user list of subjects
print("Choose a class to study:")
print(study_options)

#ask the user to pick a subject
choice = input("Your choice: ")

# check if the choice is valid
if choice in study_options:
#if user picks programming
    if choice == "programming":
        current_gpa = current_gpa + 2.0
        social_points = social_points - 5
        print("You picked a difficult subject , less free time more studying ")
#if the user picks Math
    elif choice == "Math":
        current_gpa = current_gpa + 0.3 
        social_points = social_points - 2
        print("You stuied Math. GPA improves a lot, but some social points are lost")
#if user picks English and has 3.0 or higher
    elif choice == "English" and current_gpa >= 3.0:
        social_points = social_points + 10 
        print("You studied English. Strong GPA and increased social points")
#if user picks English or history with below a 3.0
    elif choice == "History" or (choice == "English" and current_gpa < 3.0):
        current_gpa = current_gpa + 0.1
        social_points = social_points + 3
        print("You studied History (or English with low GPA). Small GPA and social boost.")

 # for invalid input           
elif choice not in study_options:
    print("Invalid choice. Please pick from the list.")


#Step 4: Final semester assessment

if type(current_gpa) is float and type(study_hours) is int and type(social_points) is int and type(stress_level) is int:

    if type(current_gpa) is not str:
        if current_gpa >= 3.5:
            if stress_level < 50:
                ending = "Excellent semester! Work was well balanced."
            else:
                ending = "Strong GPA, but stress was high."
    elif current_gpa >= 2.5:
        if study_hours > 20:
             ending = "Solid semester. Hard work kept you on track"
        else:
            ending = "Grades are fine, but may need more study time."
    else:
        if social_points > 40:
            ending = "Struggled academically, but was socially active."
        else:
            ending = "Hard semester. Low grades and high stress. :/"
    
    print("\n=== Final Semester Assessment ===")
    print(f"{ending}")
    print(f"GPA: {current_gpa:.2f}, Study_hours: {study_hours}, Social Points: {social_points}, Stress: {stress_level}")

else:
    print("Error: Variable types are not correct - check GPA, hours, points, stress.")


    
