import datetime
import  time
import os



def view():
    
    try:
        with open("C:/Windows/System32/drivers/etc/hosts", 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File not found.")
    except IOError:
        print(f"Error reading file.")



def un():
    os.system('cls')
    view()
    line_number=int(input("Enter line NO : "))
    with open("C:/Windows/System32/drivers/etc/hosts", 'r') as file:
        lines = file.readlines()

    
    if line_number >= 1 and line_number <= len(lines):
        del lines[line_number - 1]
    else:
        print("Invalid line number!")

    with open("C:/Windows/System32/drivers/etc/hosts", 'w') as file:
        file.writelines(lines)
    

    print("Unblocked Successfully!")

    
    # et=datetime.datetime(2023,6,2)
    # site_block=[]
    # n=int(input("Enter Number of Site should unblock : "))
    # print(" Site Should be Entered into : \n\t\t Format : www.instagram.com")
    # for i in range(0,n):
    #     sit=input("Enter Site :")
    #     site_block.append(sit)


    # hp="C:/Windows/System32/drivers/etc/hosts"
    # rd="127.0.0.1"
    # print("Blocked the  Website till : ",et)
    # while True:
    #     if datetime.datetime.now()<et:
    #         with open(hp,"r+") as  hosts_file :
    #             content=hosts_file.read()
    #             for web in site_block:
    #                 if web not in content:
    #                     hosts_file.write(rd+" "+web+"\n")
    #                 else:
    #                     pass

    #     else:
    #         with open(hp, "r+") as hosts_file:
    #             content=hosts_file.readline()
    #             hosts_file.seek(0)
    #             for line in content:
    #                 if not any(web in line for web in site_block):
    #                     hosts_file.write(line)

    #             hosts_file.truncate()

    #         time.sleep(5)


def add():
    et=datetime.datetime(2023,6,6)
    site_block=[]
    n=int(input("Enter Number of Site should Block : "))
    print(" Site Should be Entered into : \n\t\t Format : www.instagram.com")
    for i in range(0,n):
        sit=input("Enter Site :")
        site_block.append(sit)


    hp="C:/Windows/System32/drivers/etc/hosts"
    rd="127.0.0.1"
    print("Blocked the  Website till : ",et)
    while True:
        if datetime.datetime.now()<et:
            with open(hp,"r+") as  hosts_file :
                content=hosts_file.read()
                for web in site_block:
                    if web not in content:
                        hosts_file.write(rd+" "+web+"\n")
                    else:
                        pass

        else:
            with open(hp, "r+") as hosts_file:
                content=hosts_file.readline()
                hosts_file.seek(0)
                for line in content:
                    if not any(web in line for web in site_block):
                        hosts_file.write(line)

                hosts_file.truncate()

            time.sleep(5)
    
def intro():
    print("---------------------------------------------------------------------------------------------------------------------------------------------")

    print("\n\n\n\t\t\t\tN.K Orchid College of Enginnering and Technology, Solapur\n\n\n")

    print("-------------------------------------------------------------------------------------------------------------------------------------------")

    print("\n\n\n\t\t\t\t\tPython Practical 14\n")
    print("\t\tTopic:Website Blocker\n")
    print("\t\tMembers :\n")
    print("\t\t1.Om Sawant\n")
    print("\t\t2.Priyanka Sul\n\n\n")
    print("\t\t\tSelect Choice : \n\n")
    print("\t\t1.Add Site\n")
    print("\t\t2.View Blocked Sites\n")
    print("\t\t3.Unblock site\n")
    a=int(input("Enter : "))

    match a:
        case 1:add()
        case 2:view()
        case 3:un()
        case _:
            print("PLz try again !!!")
            os.system('cls')
            intro()






os.system('cls')
intro()
