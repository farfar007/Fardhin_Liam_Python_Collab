#University Registration
courses = ["Calculus I", "Calculus II", "Linear Algebra", "Differential Equations", "Discrete Mathematics", 
        "Probability and Statistics", "Mathematical Logic", "Complex Analysis", "Abstract Algebra", "Numerical Analysis", 
        "General Biology", "Genetics", "Microbiology", "Molecular Biology", "Human Anatomy", 
        "Biochemistry", "Evolutionary Biology", "Ecology", "Immunology", "Neuroscience", 
        "General Chemistry", "Organic Chemistry", "Inorganic Chemistry", "Physical Chemistry", "Analytical Chemistry", 
        "Quantum Chemistry", "Environmental Chemistry", "Chemical Thermodynamics", "Materials Chemistry", "Biophysical Chemistry", 
        "Classical Mechanics", "Electricity and Magnetism", "Modern Physics", "Thermodynamics and Statistical Mechanics", "Quantum Mechanics", 
        "Optics", "Electromagnetic Theory", "Solid State Physics", "Nuclear Physics", "Particle Physics", 
        "Relativity", "Astrophysics", "Plasma Physics", "Computational Physics", "Mathematical Physics" ] 
# This is the coruses that we offer in llist form
rc = [] #Intilaize list
def displaycourses(courses): #Function to see courses
    print("Available Courses: ") #Register for courses 
    x = 1 #Intilaize variable
    for i in courses: #Use a for loop 
        print(f"{x} - {i}")
        x += 1
    #Show all the courses    
def registercourses(courses, rc): #Function to register for courses
    if len(rc) >= 3: # Checl to see if they have max amount of courses
        print("You already have the maximum amount of courses this semester")
        return
    displaycourses(courses) # Show courses 
    c = int(input("Please enter the course number for registration: ")) 
    if (int(c)<1) or (int(c) > len(courses)): # Cehck to see if the course they want was valid
        print("Numerical choice is invalid, please enter a valid cousrse choice")
        return
    sc = courses[int(c) - 1] #Check if they have already registered fro this course
    if sc in rc:
        print("You have already registered for this course. ")
    else: 
        rc += [sc] #Now if it is valid then they can register
        print(f"You are now registered for {sc},")
def viewregisteredcourses(rc): #Fucntion to view their registered courses
    if len(rc) == 0:
        print("You have not registered for any courses yet. ")
    else: # If they haven't registered for any courses
        print("Current Courses: ")
        for course in rc: #Show courses
            print(f"- {course} ")
def main():
    choice = ""
#Call for the fucntuion when they enter a number
    while choice != 4:
        print("\nUniversity Registration System:") 
        print("1. View available courses")
        print("2. Register for a course")
        print("3. View registered courses")
        print("4. Exit")

        choice = input("Please enter a number between 1 and 4: ")
        choice = int(choice)

        if choice == 1:
            displaycourses(courses)
        elif choice == 2:
            registercourses(courses, rc)
        elif choice == 3:
            viewregisteredcourses(rc)
        elif choice == 4:
            print("Now exiting the registration system...")
        else:
            print("Invalid, please enter a number between 1 and 4.")

main()