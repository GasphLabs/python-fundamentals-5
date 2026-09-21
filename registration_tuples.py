# CHECKS IF THE ANSWER IS EMPTY
def isempty(data):
    stripped_data = data.strip()
    global error_popped
    error_popped = False
    while True:
        if not stripped_data:
            print('\nError Code: 112\n Try Again.\n')
            error_popped = True
            break
        else:
            break

# ASSUMES IT SHOULD ALL BE NUMBERS
def isdigit_control(data):
    while True:
        global error_popped
        error_popped = False
        if not data.isdigit():
            print('\nError Code: 113\nTry Again.\n')
            error_popped = True
            # ISDIGIT ERROR CODE -> 113
            break
        else:
            break

# ASSUMES IT SHOULD ALL BE LETTERS
def isalpha_control(data):
    while True:
        global error_popped
        error_popped = False
        if not data.replace(' ', '').replace('.', '').isalpha():
            print('\nError Code: 114\nTry Again.\n')
            error_popped = True
            # ISALPHA ERROR CODE -> 114
            break
        else:
            break

# ASSUMES IT SHOULD BE FLOAT OR INT
def manual_gpa_control(data):
    while True:
        global error_popped
        error_popped = False
        if not type(gpa) in [float, int]:
            print('\nError Code: 115\nTry Again.\n')
            # GPA-CHECK ERROR CODE -> 115
            error_popped = True
            break
        else:
            break

while True:
    print(
        '\n\n\n\n======== WELCOME TO STUDENT REGISTRATION PORTAL ========\n'
        )

    # NAME
    while True:
        name = input('- Your Name: ')
        isalpha_control(name)
        if error_popped:
            continue
        break

    # AGE
    while True:
        age = input('- Your Age: ')
        isdigit_control(age)
        if error_popped:
            continue
        break
    
    # MAJOR
    while True:
        major = input('- Your Major: ')
        isalpha_control(major)
        if error_popped:
            continue
        break

    # GPA
    while True:
        gpa = input('- Your GPA: ')
        manual_gpa_control(gpa)
        if error_popped:
            continue
        break


    student_data = ('Name: ', 'Age: ', 'Major: ', 'GPA: ')
    name, age, major, gpa = student_data

    # HIGHLIGHTS THE IMMUTABILITY OF TUPLES
    print(f'Data of the registered student:\n{student_data}\n')
    question = input('Do you want to try changing one of the values?\n').lower().strip()

    if question_change_value in ['yes', 'yeah', 'sure', 'ofc', 'yep']:
        while True:
            question_change_which_value = input('Which value you would like to change?\n').lower().strip()
            if question_change_which_value == 'name':
                while True:
                    instead_name = input('What would you like to change the name as?')
                    isalpha_control(instead_name)
                    if error_popped:
                        continue
                    name = instead_name
