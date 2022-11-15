input_name = input('Enter your name:') # input name

lowered_input_name = input_name.lower()

students = ['Amanzi', 'Angela', 'Holly'] #list of students for class
students_lower=[] #empty list for changing list to lower case
students_checker = []

for name in students: #loop through student list
    name_lower = name.lower() #create variable to hold lower case names
    students_lower.append(name_lower) #add lower case names to empty list student_lower
    # print(name_lower)
    # print("Students list Lowered")
  
    # print(students_lower)
    # print(" ")

    if len(students_lower) == len(students): #when students_lower is the same size as student progress on
        for x in students_lower:               #Loop through students_lower
            
            if x == lowered_input_name:          #if you find lower_input_name, print statement
                print("Hi! " + input_name)
                break
            if lowered_input_name not in students_lower: #if input name is not found, print reject statement
                print("Sorry " + input_name + ", You shall not pass! Go back to the shadow") 
                break

    #I found this code below more effecient than the nested loop starting at line 19. but I wanted to use the nested loop per the assignment
        #if lowered_input_name in students_lower:
              #print("Hi! " + input_name)
        #if lowered_input_name not in students_lower:
            #print("Sorry " + input_name + ", You shall not pass! Go back to the shadow")