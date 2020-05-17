from datetime import date
import datetime

today = date.today()

users_passwords = {}
in_file = open("user.txt", "r")
contents = in_file.read().splitlines()

for i in contents:
    both = i.split(",")
    usern = both[0]
    passw = both[1].replace(" ", "")
    users_passwords.update({usern: passw})


def admin_menu():
    print("")
    print("Please select one of the following options: ")
    print("")
    print("r - \t register user")
    print("a - \t add task")
    print("va - \t view all tasks")
    print("vm - \t view my tasks")
    print("gr - \t generate reports")
    print("s - \t display statistics")
    print("dr - \t display reports")
    print("e - \t exit")
    print("")
    opt = input()

    if opt == "r":  # This statement will call reg_user and a user can be registered
        reg_user()
    elif opt == "a":  # The user is asked to add details for the new task
        add_task()
    elif opt == "va":  # All of the tasks in the tasks.txt is displayed in this elif
        view_all()
    elif opt == "vm":  # This elif statement will display all the tasks of the username which is currently logged in
        view_mine()
    elif opt == "gr":  # This elif statement will generate reports based on the tasks and users text files
        gen_report()
    elif opt == "ds":  # This elif statement will display statistics about the users and tasks
        view_stats()
    elif opt == "dr": # This elif statement will display the reports to the screen
        display_rep()
    elif opt == "e":  # If the user enters 'e' the program will close.
        print("Closing Task manager")
        temp_file = open("templogin.txt", "w")
        temp_file.close()
        exit()


def menu():  # This menu is for everyone except the admin

    print("")
    print("Please select one of the following options: ")
    print("")
    print("a - \t add task")
    print("va - \t view all tasks")
    print("vm - \t view my tasks")
    print("e - \t exit")
    print("")
    opt = input()

    if opt == "a":  # The user is asked to add details for the new task
        add_task()
    elif opt == "va":  # All of the tasks in the tasks.txt is displayed in this elif
        view_all()
    elif opt == "vm":  # This elif statement will display all the tasks of the username which is currently logged in
        view_mine()
    elif opt == "s":  # if the admin chooses 's', this if statement will execute
        view_stats()
    elif opt == "e":  # If the user enters 'e' the program will close.
        print("Closing Task manager")
        temp_file = open("templogin.txt", "w")
        temp_file.close()
        exit()

def display_rep():  # Displays the reports on created text files user_overview and task_overview
    in_content1 = open("task_overview.txt", "r", encoding='utf-8')
    content1 = in_content1.read()
    in_content1.close()

    in_content2 = open("user_overview.txt", "r", encoding='utf-8')
    content2 = in_content2.read()
    in_content2.close()

    print("======== Displaying reports ========")
    print("")
    print(content1)
    print("=========================")
    print(content2)



def reg_user():
    username = input("Enter username again to start register process: ")
    if username == 'admin':  # This if statement will only execute if the user logged in is admin
        print("Register process started")
        new_u = input("Enter username: ")  # Adding a new username
        new_p1 = input("Enter password: ")  # Adding a new password for the username
        new_p2 = input("Confirm password: ")  # Confirmation of password that is used in the next while loop

        while new_p1 != new_p2:  # Checking if  passwords match
            print("Passwords do not match! Please try again")
            new_p1 = input("Enter password: ")
            new_p2 = input("Confirm password: ")
        else:  # If the two passwords match, the credentials is accepted it is written in the user.txt file

            if username in users_passwords:
                print("Username taken, please enter a new username")
                new_u = input("Enter username: ")
                print("Username and password accepted")
                in_user = open("user.txt", "r+")
                usercon_old = in_user.read()
                usercon_new = new_u + ", " + new_p2
                in_user.write("\n" + usercon_new)
                users_passwords.update({new_u: new_p2})
                print("New user added")
                in_user.close()

            else:
                print("Username and password accepted")
                in_user = open("user.txt", "r+")
                usercon_old = in_user.read()
                usercon_new = new_u + ", " + new_p2
                in_user.write("\n" + usercon_new)
                users_passwords.update({new_u: new_p2})
                print("New user added")
                in_user.close()
    else:  # Only admin is allowed to register a user
        print("Sorry, only admin can add a user")


def add_task():
    print("")
    print("Add a task")
    add_use = input("Enter username of person the task is assigned for: ")
    add_tit = input("Enter title of task: ")
    add_dis = input("Enter description of task: ")
    add_ddate = input("Enter due date (dd mmm yyyy): ")
    in_tasks = open("tasks.txt", "r+")
    taskcon_old = in_tasks.read()
    cur_date = today.strftime("%d %b %Y")  # Getting the current date
    taskcon_new = add_use + ", " + add_tit + ", " + add_dis + ", " + cur_date + ", " + add_ddate + ", No"
    in_tasks.write("\n" + taskcon_new)  # New data is written to file
    print("Task added successfully")
    in_tasks.close()


def view_all():
    print("")
    print("Viewing all tasks")
    print("")
    in_tasks = open("tasks.txt", "r")
    content = in_tasks.read().splitlines()  # Reading the contents and splitting the lines
    task = {}
    count = 0
    for i in content:  # This for loop will iterate through the number of lines in the tasks.txt file
        task = i.split(",")  # Splitting the lines using the ","
        print("Task number: " + str(count))
        print("Task: " + "\t" + task[1])
        print("Assigned to: " + "\t" + task[0])
        print("Task description: " + "\t" + task[2])
        print("Date assigned: " + "\t" + task[3])
        print("Due date: " + "\t" + task[4])
        print("Task complete?  \tNo")
        print("")
        count = count + 1
    in_tasks.close()
    print("")


def get_month_code(month):  # Changing the month abbreviation to the month number
    if month == 'Jan':
        month = 1
    elif month == 'Feb':
        month = 2
    elif month == 'Mar':
        month = 3
    elif month == 'Apr':
        month = 4
    elif month == 'May':
        month = 5
    elif month == 'Jun':
        month = 6
    elif month == 'Jul':
        month = 7
    elif month == 'Aug':
        month = 8
    elif month == 'Sep':
        month = 9
    elif month == 'Oct':
        month = 10
    elif month == 'Nov':
        month = 11
    else:
        month = 12
    return month


def gen_report():
    in_file = open("tasks.txt", "r", encoding='utf-8')
    contents = in_file.read().splitlines()
    task_lines = contents
    in_file.close()
    taskcount = 0
    for i in contents:  # Counting the number of tasks in the tasks.txt file
        taskcount = taskcount + 1

    task_file = open("tasks.txt", "r+", encoding='utf-8')
    contents = task_file.read()
    contents = contents.replace("\n", ",")
    task_string = contents.split(",")
    new_list = []
    for i in task_string:
        element = i.strip()
        new_list.append(element)

    complete = 0
    not_complete = 0

    for i in range(0, len(new_list), 6):  # Counting the number of completed tasks and not completed
        if i == 'Yes':
            complete += 1
        else:
            not_complete += 1

    not_complete_per = (taskcount / not_complete) * 100  # Calculating the percentage of tasks not complete

    due_old = []
    for i in range(4, len(new_list), 6):
        due_date = new_list[i]
        due_old.append(due_date)
    due_new = []
    for i in range(0, len(due_old)):
        year = due_old[i][7:]
        month = due_old[i][3:6]
        month = get_month_code(month)

        day = due_old[i][:2]

        d1 = datetime.datetime(int(year), month, int(day))
        due_new.append(d1)

    date_n = datetime.date.today()
    date_no = str(date_n)
    now_year = date_no[:4]
    now_month = date_no[5:7]
    now_day = date_no[8:]
    date_now = datetime.datetime(int(now_year), int(now_month), int(now_day))
    due_count = 0

    for i in range(0, len(due_new)):
        if due_new[i] < (date_now):
            due_count += 1
        else:
            due_count += 0
    overdue_per = (taskcount / due_count) * 100  # Calculating percentage of overdue tasks

    task_overview = open("task_overview.txt", "w")
    task_overview.write("Task Overview\n")
    task_overview.write("-------------\n")
    task_overview.write("Total number of tasks: " + str(taskcount) + "\n")
    task_overview.write("Tasks completed: " + str(complete) + "\n")
    task_overview.write("Tasks not completed: " + str(not_complete) + "\n")
    task_overview.write("Tasks not completed & overdue: " + "\n")
    task_overview.write("Percentage of incomplete tasks: " + str(not_complete_per) + "%\n")
    task_overview.write("Percentage of overdue tasks: " + str(overdue_per) + "%\n")
    print("Task Overview created")

    user_overview = open("user_overview.txt", "w")
    user_overview.write("User Overview\n")
    user_overview.write("Users registered: " + str(user_count()) + "\n")
    user_overview.write("Total number of tasks: " + str(taskcount) + "\n" + "\n" + "\n" + "\n")
    # first loop through to print out the different users
    users_file = open("user.txt", "r")
    users_file_content = users_file.read().splitlines()
    current_user = ''
    today_date = datetime.datetime.today()
    for line in users_file_content:
        line = line.split(",")
        current_user = line[0]
        user_overview.write("======== Task summary for user: " + current_user + " ========\n")
        user_tot_tasks_assigned = 0
        user_tot_tasks_completed = 0
        overdue_counter = 0
        for t in task_lines:
            #task stuff
            task_line = t.split(",")
            user = task_line[0]
            is_complete = task_line[5]
            #date stuff
            date_due = task_line[4].split(" ")
            day1 = date_due[1]
            month1 = date_due[2]
            month1 = get_month_code(month1)
            year1 = date_due[3]
            due_date_pretty = datetime.datetime(int(year1), month1, int(day1))
            #overdue counter

            if user == current_user:
                user_tot_tasks_assigned += 1
                if is_complete == " Yes":
                    user_tot_tasks_completed += 1
                else:
                    if today_date > due_date_pretty:
                        overdue_counter += 1

        user_overview.write("Total number of tasks assigned: " + str(user_tot_tasks_assigned) + "\n")
        user_overview.write("Percentage of all tasks assigned: " + str(round((user_tot_tasks_assigned/taskcount*100), 2)) + "%\n")
        perc_completed = 0
        if user_tot_tasks_assigned > 0:
            perc_completed = round((user_tot_tasks_completed / user_tot_tasks_assigned * 100), 2)
            user_overview.write("Percentage of all tasks completed: " + str(perc_completed) + "%\n")
        else:
            perc_completed = 0
            user_overview.write("Percentage of all tasks completed: 0 %\n")
        user_overview.write("Percentage of tasks still to be completed: " + str((100 - perc_completed)) + "%\n")
        user_overview.write("Tasks Overdue and not completed: " + str(overdue_counter) + "\n")
        user_overview.write("\n" + "\n")

    user_overview.write("--------------")
    print("User overview created")

def view_mine():
    in_file = open("tasks.txt", "r", encoding='utf-8')
    content = in_file.read().splitlines()

    all_tasks = {}
    count = 0
    for i in content:
        task = i.split(",")
        taskstring = task[0] + "," + task[1] + "," + task[2] + "," + task[3] + "," + task[4] + "," + task[5]
        all_tasks.update({count: taskstring})
        count = count + 1

    temp = open("templogin.txt", "r")
    content = temp.read()
    temp.close()
    key = 0
    my_tasks = {}
    for i in all_tasks.values():
        elements = i.split(",")
        user = elements[0]

        if user != content:
            print("")

        else:
            print("")
            print("Assigned to: " + content)
            print("Task number: " + str(key))
            print("Task: " + elements[1])
            print("Description: " + elements[2])
            print("Date assigned: " + elements[3])
            print("Due date: " + elements[4])
            print("Complete: " + elements[5])
            taskstring = content + "," + elements[1] + "," + elements[2] + "," + elements[3] + "," + elements[4] + "," + \
                         elements[5]
            my_tasks.update({key: taskstring})
            key = key + 1
    print("")
    show_task = int(input("To show specific task enter task number(-1 to return to main menu): "))

    if show_task != -1: # If the user does not choose to return to menu
        if show_task in my_tasks.keys():    # If user chooses a correct task number
            print("")
            elements = my_tasks[show_task].split(",")
            print("Assigned to: " + elements[0])
            print("Task number: " + str(show_task))
            print("Task: " + elements[1])
            print("Description: " + elements[2])
            print("Date assigned: " + elements[3])
            print("Due date: " + elements[4])
            print("Complete: " + elements[5])
            print("")
            print("1. Mark task as complete\n2. Edit task")
            sel = int(input("What would you like to do?\n"))

            if sel == 1:    # If the user chooses to change a task completion to yes
                task_file = open("tasks.txt", "r+", encoding='utf-8')
                contents = task_file.read()
                contents = contents.replace("\n", ",")
                task_string = contents.split(",")
                new_list = []
                for i in task_string:
                    element = i.strip()
                    new_list.append(element)
                print("")

                temp = open("templogin.txt", "r")
                username = temp.read()
                u_count = -1

                for i in range(0, len(new_list)):
                    if new_list[i] == username:
                        u_count = u_count + 1

                        if u_count == show_task:
                            new_list[i + 5] = ('Yes')

                i = 0
                in_tasks = open("tasks.txt", "w")

                while i in range(0, len(new_list) - 1):
                    new_line = new_list[i] + ", " + new_list[i + 1] + ", " + new_list[i + 2] + ", " + new_list[
                        i + 3] + ", " + new_list[i + 4] + ", " + new_list[i + 5]
                    i += 6
                    in_tasks.write(new_line + "\n")
                in_tasks.close()
                print("Task updated")

            elif sel == 2:  # If the user chooses to edit a task

                task_file = open("tasks.txt", "r", encoding='utf-8')
                contents = task_file.read()
                contents = contents.replace("\n", ",")
                task_string = contents.split(",")

                new_list2 = []
                for i in task_string:
                    element = i.strip()
                    new_list2.append(element)

                print("")
                edit_name = input("Enter username for selected task: ")
                edit_due = input("Enter due date for selected task(dd mmm yyyy): ")

                temp = open("templogin.txt", "r")
                username2 = temp.read()

                u_count1 = -1

                for i in range(0, len(new_list2)):
                    if new_list2[i] == username2:
                        u_count1 = u_count1 + 1

                        if u_count1 == show_task:
                            new_list2[0] = (edit_name)
                            new_list2[4] = (edit_due)

                i = 0
                in_tasks = open("tasks.txt", "w")

                while i in range(0, len(new_list2) - 1):
                    new_line = new_list2[i] + ", " + new_list2[i + 1] + ", " + new_list2[i + 2] + ", " + new_list2[
                        i + 3] + ", " + new_list2[i + 4] + ", " + new_list2[i + 5]
                    i += 6
                    in_tasks.write(new_line + "\n")
                in_tasks.close()
                print("Task updated")

                temp = open("templogin.txt", "r", encoding='utf-8')
                contents = temp.read()

                if contents == "admin":
                    admin_menu()
                else:
                    menu()

        else:
            print("Task selected: " + str(show_task))
            print("Incorrect task number entered!")

    else:
        print("Exiting to main menu")
        temp = open("templogin.txt", "r")
        user = temp.read()

        if user == 'admin':
            admin_menu()
        else:
            menu()


def user_count():
    in_users = open("user.txt", "r")
    content = in_users.read().splitlines()
    usercount = 0  # Setting a counter/control variable for the amount of users
    for i in content:  # Iterating through the lines in the content of the user.txt
        usercount = usercount + 1  # User count is incremented by one for each iteration
    return usercount


def view_stats():
    in_tasks = open("tasks.txt", "r")
    content = in_tasks.read().splitlines()
    taskcount = 0  # Setting a counter /control variable for the amount of tasks
    for i in content:  # Iterating through the lines in the content of the task.txt
        taskcount = taskcount + 1  # Task count is increment by one for each iteration

    print("Statistics")
    print("Number of tasks: " + str(taskcount))
    print("Number of users: " + user_count())
    in_tasks.close()


def login():
    use = False  # Setting a boolean value for the username to false
    pas = False  # Setting a boolean value for the password to false

    while use == False or pas == False:  # While the username and password booleans are False, this loop will continue. If the username and password is correct, the values are changed to true and the credentials are accepted for login
        print("Task Manager V2.0")
        username = input("Enter username: ")  # Requesting username
        password = input("Enter password: ")  # Requesting password

        in_file = open("user.txt", "r")  # Opening the 'user.txt' file to read the contents
        u_content = in_file.read().splitlines()  # Storing the content of the file in variable u_content

        temp_file = open("templogin.txt", "w")
        temp_file.write(username)
        temp_file.close()

        usernames = []

        for i in u_content:  # For loop for iterating through the lines of u_content, then splitting the content and appending the username to the usernames list
            u_name = i.split(",")
            u_name = u_name[0]
            usernames.append(u_name)

        if username in usernames:  # Checking if the username entered is indeed in the usernames list, if so the username is accepted, else it is not accepted and the user is asked again for input
            use = True
            print("")
            print("Username accepted")
        else:
            use = False
            print("")
            print("No such username!")
            username = input("Enter username again: ")  # Requesting username again
        in_file.close()

        in_file = open("user.txt", "r")  # Opening the 'user.txt' file to read the contents
        p_content = in_file.read().splitlines()  # Storing the content of the file in variable p_content
        passwords = []

        for i in p_content:  # For loop for iterating through the lines of p_content, then splitting the content and appending the password to the passwords list
            passw = i.split(",")
            passw = passw[1]
            passwords.append(passw.replace(" ", ""))

        if password in passwords:  # Checking if the password entered is indeed in the passwords list, if so the password is accepted, else it is not accepted and the user is asked again for input
            pas = True
            print("Password accepted")
        else:
            pas = False
            print("")
            print("Password incorrect")
            password = input("Enter password again: ")  # Requesting password again
        in_file.close()
    else:  # Here the else executes only if the boolean values for use and pas is true, then the user has successfully logged in
        print("")
        print("Login successfull")

    if username == 'admin':
        admin_menu()
    else:
        menu()


login()
