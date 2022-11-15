input_name = input('Enter your name:') # input name

lowered_input_name = input_name.lower()

students = ['Amanzi', 'Angela', 'Holly'] #list of students for class
students_lower=[] #empty list for changing list to lower case


for name in students: #loop through student list
    name_lower = name.lower() #create variable to hold lower case names
    students_lower.append(name_lower) #add lower case names to empty list student_lower
    # print(name_lower)
    # print("Students list Lowered")
  
    # print(students_lower)
    # print(" ")

#     if len(students_lower) == len(students):
    if lowered_input_name in students_lower: #check if input name is in the list
                    
        print("Hello, " + input_name)  #print hello statement
        break     
    else:
        print("Sorry " + input_name + ", You shall not pass! Go back to the shadow") #if name is not in list, reject them
        break    