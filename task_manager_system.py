import os
import csv
from datetime import datetime

# the first function is call if the user using the system is the admin


def admins() :
      
  print("\nPlease select one of the following options :")
  print("r - register user")
  print("a - add task")
  print("va - view all tasks")
  print("vm - view my tasks")
  print("gr  - to generate reports")
  print("s  - to view statisticts")
  print("exit")
  print("\n")
  
 # the function is called and displays the menu onced the registered user logs in
  
def users() :
  print("\nPlease select one of the following options :")
  print("a - add task")
  print("vm - view my tasks")
  print("exit")
  print("\n")
    
    

# used to register new users 

def reg_user() :
  
  write_in = open("user.txt","a")


  if pass_word != "admin" :  # checks if the user is the admin 
    
    print("you are not urthurised in this section") # only admin is allowed to reg
    
  # if user is the admin then thet are allowed to register the user
  else :
    username = input("enter new username : ")
    password = input("enter new password  : ")
    confirm  = input("please confirm your password : ")

    if password == confirm : # if passwords matches then continue testing


      while True:
        
         # Check if user name already exist
        if username  not in open('user.txt','r').read():
          
          write_in.write("\n"+str(username)+" , "+str(password))
          
          print("user successfuly registered !!!")

          break

        
        else :
          # if username already exist the program will ask for new details
          
          print("username already exist try again!!!!\n")
          username = input("enter new username : ")
          password = input("enter new password  : ")
          confirm  = input("please confirm your password : ")
          
          write_in.write("\n"+str(username)+" , "+str(password))

          print("\nuser successfuly registered !!!") # program will promtp out a succesful message if user is registered 
          break
        
          

      
    
  write_in.close()    
  

# function used to add a new task for a user
def add_task() :
      
   # write all the task information  in a file called tasks.txt
   
  username = input("\nEnter the username of the person the task is assigned to : ")
  tittle =   input("\nEnter title of the task : ")
  description = input("\nDescription of a task : ")
  date = input("\nEnter the date today :")
  task_complete= input("\nIs the task completed? :")
  write_in = open("tasks.txt","a")
  write_in.write("\n"+str(username)+", "+str(tittle)+", "+str(description)+", "+str(date)+","+str(task_complete))
  write_in.close()
  print("Task sucessfuly added!!!")



# view all the task information plus users assignted to those tasks

def view_all() :

 
  task_file = open("tasks.txt","r")
  
  for line in task_file :

    if line : 
      username,tittle,description,date,task_complete =  line.split(",")
   
      print("""
      Assigned to       :      {}
      Task tittle       :      {}
      Task description  :      {}
      Date Assigned     :      {}
      Task completed?    :     {}
        """.format(username,tittle,description,date,task_complete))
  task_file.close()
  

# views only the task information of the logged user
# each task is assigned a unique identify
def view_mine(name) :
  
  counter =0    
  task_file = open("tasks.txt","r")
  
  for line in task_file :
    username,tittle,description,date,task_complete =  line.split(",")
   
    counter+=1
    if user_name == username :
      hold=(f"""
Assigned to       :     {username}.
Task tittle       :     {tittle}.
Task description  :     {description}.
Date Assigned     :     {date}
Task completed?   :     {task_complete}
""")

      print(f""" {counter} . {hold}""")
  task_file.close()
  
  print("\Enter the number of the task you want to work on or -1 to return to a main menu")
  
  # gives user options ....to choose the number of the task or return to a main menu
  choose = input()

  if choose == "1" :

    with open("tasks.txt","r") as task_file :
      
      count = 0
        
      for line in task_file :
   
        task = line.split(",")

        count +=1
          
        if str(task[0]) == name and count == 1 :
        
    #task_file.close()
          print(f"""your selected task is : *{str(task[1])}*!!!
      
type *mark*!! if you wish to mark as complete  or  type *edit* to edit task!!
                """)
          chose = input()
          chose = chose.lower()
          
          if chose == "mark" :

            update = input("are you done if this task??? (yes/no)")

            if update == "yes" : # will change the status of the task from a *No* to a *Yes*

              updater = open("tasks.txt","r")

              line = updater.readlines()

              count = 0
  
              for line in task:

                count +=1

                task = line.split(",")

                if task[0] == name and count == 1 :
                      
                      
                  
                 
                  lastword = str(task).split()[-1]
                  
                  task = str(task).replace(lastword,"yes")
                  
                  with open("tasks.txt","a") as filer :
                    
                    for i in task :
                    
                     filer.write(str(i))

              print("\ntask finally completed!!!")

          
          

    task_file.close()          
       
 

    
  
  elif choose == "3" :

    with open("tasks.txt","r") as task_file :
      
      count = 1
        
      for line in task_file :
   
        task = line.split(",")

        count +=1
          
        if str(task[0]) == name and line[-1] :
        
          
          print(f"""your selected task is : *{str(task[1])} *

type *mark*!! if you wish to mark as complete  or  type *edit* to edit task!!
                """)
          
          chose = input()
          
          chose = chose.lower()
          
          if chose == "mark" :

            update = input("are you done if this task??? (yes/no)")

            if update == "yes" :

              updater = open("tasks.txt","r")

              line = updater.readlines()

              count = 0
  
              for line in task:

                count +=1

                task = line.split(",")

                if task[0] == name and count == 1 :
                      
                      
                  #1234
                  # del task[-1]  
                 
                  lastword = str(task).split()[-1]
                  
                  task = str(task).replace(lastword,"yes")
                  
                  with open("tasks.txt","a") as filer :
                    
                    for i in task :
                    
                     filer.write(str(i))

              print("\ntask finally completed!!!")

          
          
          
          
          

  elif choose == "2" :

    with open("tasks.txt","r") as task_file :
      
      count = 1
        
      for line in task_file :
   
        task = line.split(",")

        count +=1
          
        if str(task[0]) == name and line[-1] :
        
          
          print(f"""your selected task is : *{str(task[1])} *

type *mark*!! if you wish to mark as complete  or  type *edit* to edit task!!
                """)
          
          
          chose = input()
          chose = chose.lower()
          
          if chose == "mark" :

            update = input("are you done if this task??? (yes/no)")

            if update == "yes" :

              updater = open("tasks.txt","r")

              line = updater.readlines()

              count = 0
  
              for line in task:

                count +=1

                task = line.split(",")

                if task[0] == name and count == 1 :
                      
                      
                  #1234
                  # del task[-1]  
                 
                  lastword = str(task).split()[-1]
                  
                  task = str(task).replace(lastword,"yes")
                  
                  with open("tasks.txt","a") as filer :
                    
                    for i in task :
                    
                     filer.write(str(i))

              print("\ntask finally completed!!!")

   # returns the program to the main menu       
  elif choose == "-1" :
    
    admins()

  

       
      
    task_file.close()

def statistics():
    # User overview
    
    print("\n\n**************        User Overview       **************")
    with open("user_overview.txt","r") as user_stats:
      
      for i in  user_stats:
        print(i)


   
    print("\n\n**************       Task Overview         ***************\n")        
    # Tasks overview
    with open("task_overview.txt","r+") as stats:
      
      for i in stats:
        print(i)






# the program will first ask for password and username

pass_word= input("Enter your password : ")
user_name= input("Enter your username : ")


#then take the password and username intered and check if they are available
#the program will display the invail text if they are not correct until user enters correct cridentials

reads =  open("user.txt","r+") 
read_lines = reads.readlines()
index =0

for line in read_lines :
  
 
  index+=1     
  
  if line :

    # if the password is correct it will display the task of the login user esle it will ask you to enter correct details
    
    if user_name in line :
      break

    else :
      
      if index == len(read_lines) : # helps in to check each line in the file
        
        print("invaild username or password!!! || try again\n")
        pass_word= input("Enter your password : ")
        user_name= input("Enter your username : ")
        read_lines = reads.readlines()

        for line in read_lines :
          if pass_word in line :
    
           break
      

#if the user login is the admin the program will display the admin menu else if its not the admin the program displays the user menu

#below is the admin menu
    
if user_name == "admin" :
      
  admins()
 
#the else code below displays the user maenu
  
else :
  print("\nPlease select one of the following options :")
  print("a - add task")
  print("vm - view my tasks")
  print("exit")
  print("\n")
    
      
      
   
    
reads.close()     

charactor = input()
charactor = charactor.lower()
  





#if the user enters *r* the  program will allow them to register a new user

if charactor == "r" :
  
  
  reg_user()
     



if charactor == "a" :

  add_task()

 
# if the user enters va then the program will print out all the task in the file

if charactor == "va" :

  view_all()
 

# if the user enters vm then the program will print out only  the task of the loggedin user

if charactor == "vm" :

  view_mine(user_name) 
  
#if they enters *s* the program will display a statistics
  
if charactor == "s" :
  statistics()

if  charactor == "gr" : 
  
  task_file = open("tasks.txt","r")
  counter = 0
  for i in task_file :
    if i :
      counter +=1
  tasks = f"""Number Of Tasks ==  {counter}\n"""
  task_files = open("task_overview.txt","w")
  task_files.write(str(tasks))  
  task_files .close() 
   
  
  
  
  
  task_file = open("tasks.txt","r")
  
  search = task_file.read()
  
  find = search.count("yes")
  finder = f"""Task completed == {find}\n"""
  task_files = open("task_overview.txt","a")
  task_files.write(str(finder))  
  task_files .close() 
  
  
  
  find_uncomplete = search.count("no")
  
  uncomplete = f"""Task uncompleted == {find_uncomplete}\n"""
  task_files = open("task_overview.txt","a")
  task_files.write(str(uncomplete))  
  task_files .close() 
  
  
  
  f = open("tasks.txt","r")
  
  lines = f.readlines()
  
  counter = 0
  
  for i in lines :
        
    counter +=1
    
  percentage_of_incomplete = (find_uncomplete/counter)*100
  
  percentage = f"""Percentage of incomplete is == {round(percentage_of_incomplete)}""" 
 
  task_files = open("task_overview.txt","a")
  task_files.write(percentage)
  task_files .close() 
  
  
  
 
  # the code used to compare times and check which ones are overdued
  # i have being struggling to get this time for so long then a friend of mine advised that i use the csv_file and the time library to do so
  with open('tasks.txt') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    for row in csv_reader:
   
            # The total number of tasks that haven’t been completed and that are overdue.
      overdue_task = 0
      now = datetime.now()
      timestamp = datetime.timestamp(now)
      date_time = datetime.fromtimestamp(timestamp)
      current_date = date_time.strftime("%d %B %Y")
      date = row[4]
      if  current_date > date :
            
        overdue_task += 1

            # The percentage of tasks that are incomplete.
   
    percentage_complete = (overdue_task/counter) * 100
     
    task_files = open("task_overview.txt","a")
    task_files.write(str(f"""\nTask  incomplete and over due == {overdue_task}\n"""))
    task_files.write(str(f"""The percentage of tasks overdue == {round(percentage_complete)}\n"""))
    task_files .close()  
   
    print("The task overview is being generated !!!!")
      
 
    with open("user.txt","r") as filer :
        
       
      counter = 0
      for i in filer :
        if i :
          counter +=1
      tasks = f"""Number Of registered users  ==  {counter}\n"""
      task_files = open("user_overview.txt","w")
      task_files.write(str(tasks))  
      task_files .close() 
   
      
        
        
        
    with open("tasks.txt","r") as filer :
        
       
      counter = 0
      for i in filer :
        if i :
          counter +=1
      tasks = f"""Total number Of Tasks  ==  {counter}\n"""
      task_files = open("user_overview.txt","a")
      task_files.write(str(tasks))  
      task_files .close() 
      
    filer.close()
      
  task_files = open("tasks.txt","r")
  
  search = task_files.read()
  
  find = search.count("admin")
  admin_task_percentage = find/counter *100
  admin_percentage_completed =  find/3 * 100
  admin_task_percentage_that_are_incomplete = 0/find_uncomplete*100
  incompleted_and_are_overdue = 0
  
  
  with open("user_overview.txt", "a") as f:
    
    f.write("\n******     A D M I N   R E C O R D S      *****\n\n")
    f.write(f"""Total number of tasks assigned == {find}\n""")
    f.write(f"""Percentage of the total number of tasks == {round(admin_task_percentage)}\n""")
    f.write(f"""Percentage of the tasks assigned that are completed == {round(admin_percentage_completed)}\n""")
    f.write(f"""Percentage of the tasks assigned that are incomplete == {round(admin_task_percentage_that_are_incomplete)} \n""")
    f.write(f"""Percentage of the tasks assigned that are incompleted and are overdue == {incompleted_and_are_overdue} \n""")
    
    find1 = search.count("thabang")
    thabang_task_percentage = find1/ counter * 100
    thabang_percentage_completed = 1/2 *100
    thabang_task_percentage_that_are_incomplete = 1/2 *100
    
    # the code used to compare times and check which ones are overdued
    # i have being struggling to get this time for so long then a friend of mine advised that i use the csv_file and the time library to do so
    with open("tasks.txt") as csv_file:
      
      csv_reader = csv.reader(csv_file)
    
      for row in csv_reader:
   
            # The total number of tasks that haven’t been completed and that are overdue.
        overdue_tasks = 0
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        date_time = datetime.fromtimestamp(timestamp)
        current_date = date_time.strftime("%d %B %Y")
        date = row[4]
        if  row[1]== "thabang" and current_date > date :
            
          overdue_tasks += 1
    
        incompleted_and_are_overdue = overdue_tasks/2 *100
    f.write("\n******    Thabang   R E C O R D S     *****\n\n")
    f.write(f"""Total number of tasks assigned == {find1}\n""")
    f.write(f"""Percentage of the total number of tasks == {round(thabang_task_percentage)}\n""")
    f.write(f"""Percentage of the tasks assigned that are completed == {round(thabang_percentage_completed)}\n""")
    f.write(f"""Percentage of the tasks assigned that are incomplete == {round(thabang_task_percentage_that_are_incomplete)} \n""")
    f.write(f"""Percentage of the tasks assigned that are incompleted and are overdue == {incompleted_and_are_overdue} \n""")
    
    
    
    find2 = search.count("tshepo")
    tshepo_task_percentage = find2/ counter * 100
    tshepo_percentage_completed = 1/1 *100
    tshepo_task_percentage_that_are_incomplete = 0/1 *100
    
    with open('tasks.txt') as csv_file:
        # the code used to compare times and check which ones are overdued
        # i have being struggling to get this time for so long then a friend of mine advised that i use the csv_file and the time library to do so
      csv_reader = csv.reader(csv_file)
    
      for row in csv_reader:
   
            # The total number of tasks that haven’t been completed and that are overdue.
        overdue_tasks = 0
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        date_time = datetime.fromtimestamp(timestamp)
        current_date = date_time.strftime("%d %B %Y")
        date = row[4]
        if  row[1]== "tshepo" and current_date > date :
            
          overdue_task += 1
    
        incompleted_and_are_overdue = overdue_task/2 *100
    f.write("\n******     Tshepo   R E C O R D S      *****\n\n")
    f.write(f"""Total number of tasks assigned == {find2}\n""")
    f.write(f"""Percentage of the total number of tasks == {round(tshepo_task_percentage)}\n""")
    f.write(f"""Percentage of the tasks assigned that are completed == {round(tshepo_percentage_completed)}\n""")
    f.write(f"""Percentage of the tasks assigned that are incomplete == {round(tshepo_task_percentage_that_are_incomplete)} \n""")
    f.write(f"""Percentage of the tasks assigned that are incompleted and are overdue == {round(incompleted_and_are_overdue)} \n""")
    
    f.close()
  
  

if charactor == "exit" :
  print("u have exited your program Bye !!! Bye!!!")
  quit()


  
os.system("pause")

    
   
