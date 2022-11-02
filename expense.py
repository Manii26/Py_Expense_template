from PyInquirer import prompt
import csv


expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    #{
     #   "type":"input",
      #  "name":"spender",
       # "message":"New Expense - Spender: ",
    #}

]


def check_spender(): 
    f = open('users.csv')
    ssv = csv.reader(f)
    users = []
    for row in ssv:
        users.append(row[0])
    user_option = {
        "type":"list",
        "name":"user_option",
        "message":"Expenses for sepnder",
        "choices": users
    }
    option = prompt(user_option)
    return option
#check multiple spender

def check_multiple_spender():
    f = open('users.csv')
    ssv = csv.reader(f)
    users = []
    for row in ssv:
        users.append({"name": row[0]})
    user_option = {
        "type":"checkbox",
        "name":"user_option",
        "message":"Expenses for sepnder",
        "choices": users
    }
    option = prompt(user_option)
    return option

def new_expense(*args):

    infos = prompt(expense_questions)
    #spender = []
    spenderSimple = check_spender()
    spender = check_multiple_spender()
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    print(infos)
   
    with open('expense_report.csv', 'a') as f:
        f.write('\n' + infos['amount'] + ',' + infos['label'] + ',' + spenderSimple['user_option'])
        f.write(str(spender['user_option']))
        f.close()

    print("Expense Added !")

    return True


