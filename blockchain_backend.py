import hashlib
import secrets
import datetime
import logging
import time


class block:
    def __init__(self, U_ID, index, previous_hash, data_name, data_car_number, data_DS_detail, data_DOP, data_licence_no, data_DOB, data_DOR, data_add, current_hash):
        self.index = index
        self.previous_hash = previous_hash
        self.data_name = data_name
        self.data_car_number = data_car_number
        self.data_DS_detail = data_DS_detail
        self.data_DOP = data_DOP
        self.data_licence_no = data_licence_no
        self.data_DOB = data_DOB
        self.data_DOR = data_DOR
        self.data_add = data_add
        self.current_hash = current_hash
        self.U_ID = U_ID

def calculate_hash(U_ID,index,previous_hash,data_name,data_car_number,data_DS_detail,data_DOP,data_licence_no,data_DOB,data_DOR,data_add):
    value = str(U_ID)+str(index)+str(previous_hash)+str(data_name)+str(data_car_number)+str(data_DS_detail)+str(data_DOP)+str(data_licence_no)+str(data_DOB)+str(data_DOR)+str(data_add)
    return hashlib.sha256(value.encode()).hexdigest()

def create_first_block():
    format = '%d/%m/%Y'
    a = '11/11/1111'
    b=datetime.datetime.strptime(a, format)
    return block(0, 0, "NULL", "this is a empty block", "NULL", "NULL", b, "NULL", b, b, "NULL", calculate_hash(0, 0, "NULL", "NULL", "NULL", "NULL", b, "NULL", b, b, "NULL"))

def create_main_block(U_ID, previous_block, data_name, data_car_number, data_DS_detail, data_DOP, data_licence_no, data_DOB, data_DOR, data_add):
    index = previous_block.index+1
    current_hash = calculate_hash(U_ID,index,previous_block.current_hash,data_name,data_car_number,data_DS_detail,data_DOP,data_licence_no,data_DOB,data_DOR,data_add)
    return block(U_ID, index, previous_block.current_hash, data_name, data_car_number, data_DS_detail, data_DOP, data_licence_no, data_DOB,data_DOR,data_add,current_hash)

def print_data(blockchain):
    for block in blockchain:
        print("\n" + "-" * 40 + "\n")
        print(f"UNIQUE ID: {block.U_ID}")
        print("\n")
        print(f"INDEX: {block.index}")
        print(f"PREVIOUS HASH: {block.previous_hash}")
        print(f"CURRENT HASH: {block.current_hash}")
        print("\n\n")
        print(f"NAME: {block.data_name}")
        print(f"CAR NUMBER: {block.data_car_number}")
        print(f"DETAIL OF DELEARSHIP: {block.data_DS_detail}")
        print(f"DATE OF PURCHASE: {block.data_DOP.date()}")
        print(f"LICENCE NUMBER: {block.data_licence_no}")
        print(f"DATE OF BIRTH: {block.data_DOB.date()}")
        print(f"DATE OF REGISTRATION: {block.data_DOR.date()}")
        print(f"ADDRESS: {block.data_add}")
        print("\n"+"-"*40+"\n")

blockchain=[create_first_block()]

def add_block():
        print("\n" + "-" * 40 + "\n")
        format = '%d-%m-%Y'

        block1_data_name = input("Enter the name of customer: ")

        block1_data_car_number = input("Enter the vehicle number: ")

        block1_data_DS_detail = input("Enter the detail of dealership: ")

        DOP = input("Enter the date of purchase (DD-MM-YYYY): ")
        block1_data_DOP = datetime.datetime.strptime(DOP, format)

        block1_data_licence_no = input("Enter the licence number of customer: ")

        DOB = input("Enter the date of birth of the customer (DD-MM-YYYY): ")
        block1_data_DOB = datetime.datetime.strptime(DOB, format)

        DOR = input("Enter the date of registration (DD-MM-YYYY): ")
        block1_data_DOR = datetime.datetime.strptime(DOR, format)


        block1_data_add = input("Enter the address of the customer: ")
        block1_U_ID = secrets.token_hex(10)

        block1 = create_main_block(block1_U_ID, blockchain[-1], block1_data_name, block1_data_car_number,block1_data_DS_detail, block1_data_DOP, block1_data_licence_no, block1_data_DOB,block1_data_DOR, block1_data_add)
        blockchain.append(block1)
        print("\n" + "-" * 40 + "\n")
        print(f"YOUR DATA IS UPLOADED\nYour Unique ID is: {block1_U_ID}")
        print("\n" + "-" * 40 + "\n")


def search_uid():
    print("\n" + "-" * 40 + "\n")
    unique = str(input("Enter your unique ID: "))
    flag = 0
    for block in blockchain:
        if block.U_ID == unique:
            print("\n" + "-" * 40 + "\n")
            print(f"UNIQUE ID: {block.U_ID}")
            print("\n")
            print(f"INDEX: {block.index}")
            print(f"PREVIOUS HASH: {block.previous_hash}")
            print(f"CURRENT HASH: {block.current_hash}")
            print("\n\n")
            print(f"NAME: {block.data_name}")
            print(f"VEHICLE NUMBER: {block.data_car_number}")
            print(f"DETAIL OF DEALERSHIP: {block.data_DS_detail}")
            print(f"DATE OF PURCHASE: {block.data_DOP.date()}")
            print(f"LICENCE NUMBER: {block.data_licence_no}")
            print(f"DATE OF BIRTH: {block.data_DOB.date()}")
            print(f"DATE OF REGISTRATION: {block.data_DOR.date()}")
            print(f"ADDRESS: {block.data_add}")
            print("\n" + "-" * 40 + "\n")
            flag = 1
            break
    if flag == 0:
        print("\n" + "-" * 40 + "\n")
        print("Invalid Unique ID")




#menu driven

def op2():
        print("\n" + "-" * 40 + "\n")
        print("1.Print all \n2.Print Data by Unique ID\n3.Back\n")
        a = int(input("ENTER YOUR CHOICE: "))

        if a == 1:
            print_data(blockchain)
        elif a == 2:
            search_uid()
        elif a == 3:
            startup()
        else:
            op_default()

def op_default():
    print("\n" + "-" * 40 + "\n")
    print("Invalid Selection")

options = {2:op2}



def startup():
    try:
        while True:
            print("\n" + "-" * 40 + "\n")
            print("1.Add a new Registration\n2.Print Data\n3.EXIT\n")
            a = int(input("ENTER YOU YOUR OPERATION: "))

            if a == 1:
                try:
                    add_block()
                except ValueError:
                    logging.error("PLEASE ENTER THE DATE AS THE FORMAT IS PROVIDED USE '-' ")
                    time.sleep(1)

            elif a == 2:
                op2()
            elif a == 3:
                print("\n" + "-" * 40 + "\n")
                print("ENDING THE PROGRAM")
                print("\n" + "-" * 40 + "\n")
                break
            elif a != int:
                op_default()
    except ValueError:
        logging.error("PLEASE ENTER A NUMBER (1,2,3) AS PER PREFERENCE")
        time.sleep(1)
        startup()
startup()