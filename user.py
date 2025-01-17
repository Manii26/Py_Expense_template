from PyInquirer import prompt

user_questions = [
    {
    "type":"input",
    "name":"Name",
    "message":"New User - Name : "
    }
]

def add_user(*args):
    infos = prompt(user_questions)
    # This function should create a new user, asking for its name
    # info returns an a new line in the csv file
    b = infos['Name']
    while b == " " or b == "":
        print("Please enter a valid name")
        infos = prompt(user_questions)
        b = infos['Name']
    with open('users.csv', 'a') as f:
        f.write('\n' + infos['Name'] )   
        f.write(' ')
        f.close()
    print("User Added !")
    return True

def user_status():
    # This function should show the status of the user

    return True
