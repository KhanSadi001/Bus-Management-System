import pandas as pd   
import time as t
from datetime import *
#function for red bus reservation
def red_reser():
    try:
        o = open("redr.txt", 'r')
        l1 = list(o.readline())
        l2 = list(o.readline())
        l3 = list(o.readline())
        l4 = list(o.readline())
        l5 = list(o.readline())
        l6 = list(o.readline())
        l7 = list(o.readline())
        l8 = list(o.readline())
        l9 = list(o.readline())
        l10 = list(o.readline())
        o.close()

        print("R1: ", l1[0:6])
        print("R2: ", l2[0:6])
        print("R3: ", l3[0:6])
        print("R4: ", l4[0:6])
        print("R5: ", l5[0:6])
        print("R6: ", l6[0:6])
        print("R7: ", l7[0:6])
        print("R8: ", l8[0:6])
        print("R9: ", l9[0:6])
        print("R10:", l10[0:6])
        f = open("redr.txt", "r")
        lines = f.readlines()
        rn = datetime.now()
        dt_string = rn.strftime("%H:%M %p")

        if dt_string[0:2] == "10" and dt_string[3:5] == "00" and dt_string[5:8] == "PM":
            linesreset = ['12345\n', '12345\n', '12345\n', '12345\n', '12345\n', '12345\n', '12345\n', '12345\n', '12345\n', '12345']
            k = open("redr.txt", "w")
            k.writelines(linesreset)
            k.close()

        flag = False

        while flag==False:
            try:
                time = int(input("Time of Reservation: "))
                if time < 10 or time > 6:
                    break
                else:
                    print("Wrong Input Please Input Again!")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid integer for time.")
                continue

        try:
            row = input("Enter Row Number: ")
            seat = int(input("Enter Seat Number: "))
        except ValueError:
            print("Invalid input. Please enter valid values for row and seat.")
            exit()

        if 1 <= int(row) <= 10 and 1 <= seat <= 9:
            p = open("redr.txt", "w+")

            if row == "1" or row == "R1" or row == "r1":
                index1 = lines[0]

                if index1[seat - 1] == "X":
                    print("Already Booked!")
                    p.writelines(lines)
                    p.close()
                else:
                    a = index1.replace(str(seat), "X")
                    lines[0] = a
                    p.writelines(lines)
                    p.close()
                    print("Wait Processing...")
                    t.sleep(2)
                    print("RESERVATION SLIP")
                    print("----------------------")
                    print("Bus Service Karachi")
                    print("----------------------")
                    print("Status: Reserved")
                    now = datetime.now()
                    dt_string = now.strftime("%d/%m/%Y %H:%M %p")
                    print(dt_string)
                    re_string = now.strftime("/%m/%Y")
                    t_string = now.strftime("%p")
                    print("Row:", row)
                    print("Seat Number", seat)
                    print("Time of Reservation: ", str(time) + t_string)
                    print("Enjoy Your Ride And Please Comeback Again!")
                    print("----------------------")

            else:
                index2 = lines[int(row) - 1]

                if index2[seat - 1] == "X":
                    print("Already Booked!")
                    p.writelines(lines)
                    p.close()
                else:
                    b = index2.replace(str(seat), "X")
                    lines[int(row) - 1] = b
                    p.writelines(lines)
                    p.close()
                    print("Wait Processing...")
                    t.sleep(2)
                    print("----------------------")
                    print("RESERVATION SLIP")
                    print("----------------------")
                    print("Bus Service Karachi")
                    print("----------------------")
                    print("Status: Reserved")
                    now = datetime.now()
                    dt_string = now.strftime("%d/%m/%Y %H:%M %p")
                    print(dt_string)
                    t_string = now.strftime("%p")
                    print("Row:", row)
                    print("Seat Number", seat)
                    print("Time of Reservation: ", str(time) + t_string)
                    print("Enjoy Your Ride And Please Comeback Again!")
                    print("----------------------")

        else:
            print("You Have Pressed a Wrong Number Please Try Again!")

    except FileNotFoundError:
        print("File 'redr.txt' not found.")

    print()
#function for orange bus reservation
def orange_reser():
    try:
        o = open("oranger.txt", 'r')
        l1 = list(o.readline())
        l2 = list(o.readline())
        l3 = list(o.readline())
        l4 = list(o.readline())
        l5 = list(o.readline())
        l6 = list(o.readline())
        o.close()

        print("R1: ", l1[0:5])
        print("R2: ", l2[0:5])
        print("R3: ", l3[0:5])
        print("R4: ", l4[0:5])
        print("R5: ", l5[0:5])
        print("R6: ", l6[0:5])

        f = open("oranger.txt", "r")
        lines = f.readlines()
        rn = datetime.now()
        dt_string = rn.strftime("%H:%M %p")

        if dt_string[0:2] == "10" and dt_string[3:5] == "00" and dt_string[5:8] == "PM":
            linesreset = ['12345\n', '12345\n', '12345\n', '12345\n', '12345\n', '12345']
            k = open("oranger.txt", "w")
            k.writelines(linesreset)
            k.close()

        flag = False

        while flag==False:
            try:
                time = int(input("Time of Reservation: "))
                if time < 10 or time > 6:
                    break
                else:
                    print("Wrong Input Please Input Again!")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid integer for time.")
                continue

        try:
            row = input("Enter Row Number: ")
            seat = int(input("Enter Seat Number: "))
        except ValueError:
            print("Invalid input. Please enter valid values for row and seat.")
            exit()

        if 1 <= int(row) <= 6 and 1 <= seat <= 6:
            p = open("oranger.txt", "w+")

            if row == "1" or row == "R1" or row == "r1":
                index1 = lines[0]

                if index1[seat - 1] == "X":
                    print("Already Booked!")
                    p.writelines(lines)
                    p.close()
                else:
                    a = index1.replace(str(seat), "X")
                    lines[0] = a
                    p.writelines(lines)
                    p.close()
                    print("Wait Processing...")
                    t.sleep(2)
                    print("RESERVATION SLIP")
                    print("----------------------")
                    print("Bus Service Karachi")
                    print("----------------------")
                    print("Status: Reserved")
                    now = datetime.now()
                    dt_string = now.strftime("%d/%m/%Y %H:%M %p")
                    print(dt_string)
                    re_string = now.strftime("/%m/%Y")
                    t_string = now.strftime("%p")
                    print("Row:", row)
                    print("Seat Number", seat)
                    print("Time of Reservation: ", str(time) + t_string)
                    print("Enjoy Your Ride And Please Comeback Again!")
                    print("----------------------")

            else:
                index2 = lines[int(row) - 1]

                if index2[seat - 1] == "X":
                    print("Already Booked!")
                    p.writelines(lines)
                    p.close()
                else:
                    b = index2.replace(str(seat), "X")
                    lines[int(row) - 1] = b
                    p.writelines(lines)
                    p.close()
                    print("Wait Processing...")
                    t.sleep(2)
                    print("----------------------")
                    print("RESERVATION SLIP")
                    print("----------------------")
                    print("Bus Service Karachi")
                    print("----------------------")
                    print("Status: Reserved")
                    now = datetime.now()
                    dt_string = now.strftime("%d/%m/%Y %H:%M %p")
                    print(dt_string)
                    t_string = now.strftime("%p")
                    print("Row:", row)
                    print("Seat Number", seat)
                    print("Time of Reservation: ", str(time) + t_string)
                    print("Enjoy Your Ride And Please Comeback Again!")
                    print("----------------------")

        else:
            print("You Have Pressed a Wrong Number Please Try Again!")

    except FileNotFoundError:
        print("File 'oranger.txt' not found.")



    print()
#fucntion for green bus resservation
def green_reser():
    
    try:
        o = open("greenr.txt", 'r')
        l1 = list(o.readline())
        l2 = list(o.readline())
        l3 = list(o.readline())
        l4 = list(o.readline())
        l5 = list(o.readline())
        l6 = list(o.readline())
        o.close()

        print("R1: ", l1[0:5])
        print("R2: ", l2[0:5])
        print("R3: ", l3[0:5])
        print("R4: ", l4[0:5])
        print("R5: ", l5[0:5])
        print("R6: ", l6[0:5])

        f = open("greenr.txt", "r")
        lines = f.readlines()
        rn = datetime.now()
        dt_string = rn.strftime("%H:%M %p")

        if dt_string[0:2] == "10" and dt_string[3:5] == "00" and dt_string[5:8] == "PM":
            linesreset = ['12345\n', '12345\n', '12345\n', '12345\n', '12345\n', '12345']
            k = open("greenr.txt", "w")
            k.writelines(linesreset)
            k.close()

        flag = False

        while flag==False:
            try:
                time = int(input("Time of Reservation: "))
                if time < 10 or time > 6:
                    break
                else:
                    print("Wrong Input Please Input Again!")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid integer for time.")
                continue

        try:
            row = input("Enter Row Number: ")
            seat = int(input("Enter Seat Number: "))
        except ValueError:
            print("Invalid input. Please enter valid values for row and seat.")
            exit()

        if 1 <= int(row) <= 6 and 1 <= seat <= 6:
            p = open("greenr.txt", "w+")

            if row == "1" or row == "R1" or row == "r1":
                index1 = lines[0]

                if index1[seat - 1] == "X":
                    print("Already Booked!")
                    p.writelines(lines)
                    p.close()
                else:
                    a = index1.replace(str(seat), "X")
                    lines[0] = a
                    p.writelines(lines)
                    p.close()
                    print("Wait Processing...")
                    t.sleep(2)
                    print("RESERVATION SLIP")
                    print("----------------------")
                    print("Bus Service Karachi")
                    print("----------------------")
                    print("Status: Reserved")
                    now = datetime.now()
                    dt_string = now.strftime("%d/%m/%Y %H:%M %p")
                    print(dt_string)
                    re_string = now.strftime("/%m/%Y")
                    t_string = now.strftime("%p")
                    print("Row:", row)
                    print("Seat Number", seat)
                    print("Time of Reservation: ", str(time) + t_string)
                    print("Enjoy Your Ride And Please Comeback Again!")
                    print("----------------------")

            else:
                index2 = lines[int(row) - 1]

                if index2[seat - 1] == "X":
                    print("Already Booked!")
                    p.writelines(lines)
                    p.close()
                else:
                    b = index2.replace(str(seat), "X")
                    lines[int(row) - 1] = b
                    p.writelines(lines)
                    p.close()
                    print("Wait Processing...")
                    t.sleep(2)
                    print("----------------------")
                    print("RESERVATION SLIP")
                    print("----------------------")
                    print("Bus Service Karachi")
                    print("----------------------")
                    print("Status: Reserved")
                    now = datetime.now()
                    dt_string = now.strftime("%d/%m/%Y %H:%M %p")
                    print(dt_string)
                    t_string = now.strftime("%p")
                    print("Row:", row)
                    print("Seat Number", seat)
                    print("Time of Reservation: ", str(time) + t_string)
                    print("Enjoy Your Ride And Please Comeback Again!")
                    print("----------------------")

        else:
            print("You Have Pressed a Wrong Number Please Try Again!")

    except FileNotFoundError:
        print("File 'redr.txt' not found.")



    print()
#function for adding balance to card
def card():
    username = input("Enter Your Username: ")
    r = pd.read_excel('data_user.xlsx')
    selected_row = r.loc[r['username'] == username]
    if not selected_row.empty:
        card_balance = selected_row['card balance'].values[0]
        print(f"Card balance for Username {username}: {card_balance}")
        op =input("Do You Want To Add Balance? YES OR NO: ")
        if op == "yes" or op =="YES" or op == "Yes":
            add_amount=int(input("Enter The Amount You Want to Add in Card: "))
            r.loc[r['username'] == username, 'card balance'] += add_amount
            print("Wait...")
            t.sleep(2)
            print("RECIEPT")
            print("----------------------")
            print("Bus Service Karachi")
            print("----------------------")
            print("Old Amount : ",card_balance)
            print("Charged Amount : ",add_amount)
            print("Current Amount : ",add_amount+card_balance)
            print("Status:Paid")
            print("-----------------------")
            
            r.to_excel('data_user.xlsx', index=False)
        elif op == "no" or op =="NO" or op == "No":
            pass
    else:
        print(f"Username {username} not found. Please register yourself.")
def ticket():
    print("Please Submit 55PKR")
    print("Wait Ticket Processing...")
    t.sleep(2)
    print("RECIEPT")
    print("----------------------")
    print("Bus Service Karachi")
    print("----------------------")
    print("Price : 55RPS")
    print("Status:Paid")
    print("----------------------")
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M %p")
    print(dt_string)
    print("Enjoy Your Ride And Please Comeback Again!")
    print("----------------------")
#function for route details     
def route_details():
    flag=False
    timing = "6AM-10PM"
    days = "Monday-Sunday"
    while flag==False:
        print("Which Bus Route Would You Like To See?")
        print("1: Green Bus")
        print("2: Orange Bus")
        print("3: Red Bus")
        print("0: Exit")
        option = input("Enter Your Option Number:")  
        file = open("routes.txt","r")
        green = file.readline()
        orange = file.readline()
        red = file.readline()
        if option == "1":
            print(green)
            print(timing)
            print(days)
            flag=True
        elif option == "2":
            print(orange)
            print(timing)
            print(days)
            flag = True
        elif option == "3":
            print(red)
            print(timing)
            print(days)
            flag = True
        elif option == "0":
            flag = True
        else:
            print("Invalid Option! Please Enter Again.")
            continue
    print()
#function for cost information / fare from ticket and card
def costing():
    flag = False
    while flag == False:
        print("With Card The Cost Is 5Rs Per Station")
        print("With Ticket One Way Cost Is 55Rs")
        estimate = input("Would You Like To Estimate Cost For Card? Yes Or No: ")
        if estimate == "Yes" or estimate=="YES" or estimate=="yes":
            station_num=int(input("Enter Number Of Stations Passed: "))
            cost_card=station_num*5
            print(f"The Total Cost For Card Is For {station_num} stations is",cost_card,"Rs.")
            break
        elif estimate == "No" or estimate=="NO" or estimate=="no":
            pass
        else:
            print("Please Answer In Yes Or No! ")
            continue
    flag2 = False
    while flag2 == False:
        question = input("Would You Like To Register Yourself And Create Your Card? Yes Or No: ")
        if question == "Yes" or question=="YES" or question=="yes":
            add_user()
            break
        elif question == "No" or question=="NO" or question=="no":
            break
        else:
            print("Please Answer In Yes Or No! ")
            continue
    print()
#fucntion for regitering user
def add_user():
    
    username = input("Please Enter Your Username Must be at Least 6 Characters and Should Have Some Numbers and Symbols: ")
    low=username.lower()
    if len(low) >1 and len(low) <=30:
        r = pd.read_excel('data_user.xlsx')
        selected_row = r['username'] == low
        repl=selected_row.to_string().replace(" ","")
        if repl.find("True") >= 0:
            print("Already Taken!")
        else:    
            new_data = {'username': [low],'card balance':[100]   }
            new_df = pd.DataFrame(new_data)
            r = pd.concat([r,new_df], ignore_index=True)
            r.to_excel('data_user.xlsx', index=False)
            print("Successfully Added!")
    print()
    
#main starts here!
flag=False 
option=""
print("Welcome To Sadi Bus Service Karachi")
print("************************")
while flag==False:
    
    print("0: Exit")
    print("1: Register Yourself")
    print("2: Route Details")
    print("3: Ticket/Card")
    print("4: Reserve Seats")
    print("5: Costing Info")
    option = input("Choose Your Option Number:")
    if option =="1":
        add_user()
    elif option =="0":
        print("Thanks For Visiting Us!")
        flag=True
    elif option =="2":
        route_details()  
    elif option == "3":
        checker =False
        while checker == False: 
            prompt =""
            print("1: Ticket")
            print("2: Card")
            prompt = input("Do You Want To Buy A Ticket Or Check Your Card?")
            if prompt == "1":
                ticket()
                checker = True
            elif prompt == "2":
                card()
                checker = True
            else: 
                print("Wrong option please enter again!")
                continue 
    elif option == "4":
        flag2 = False
        while flag2 == False:
            print("1: Green")
            print("2: Orange")
            print("3: Red")
            print("0: Exit")
            opter = input("Enter Option Number Which Bus Seat You Want to Reserve: ")
            if opter == "1":
                    green_reser()
                    flag2=True
            elif opter == "2":
                    orange_reser()
                    flag2=True
            elif opter == "3":
                    red_reser()
                    flag2=True
            elif opter == "0":
                    flag2 = True
            else: 
                    print("Wrong option please enter again!")
                    continue 
    elif option=="5":
        costing()
    else:
        print("You Have Pressed The Wrong Option Number. Please Enter The Correct Option Number! ")
        print()
        continue
#main ends here!
        
        
    