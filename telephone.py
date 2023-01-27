"""*****************************************************************************
                            MODULES USED IN PROJECT
*****************************************************************************"""

import pickle
import os


"""*****************************************************************************
                            CLASS USED IN PROJECT
*****************************************************************************"""
class telephone(object):
    def __init__(s):
        s.name=""
        s.address=""
        s.tele_no=0
    def new_cust(s):
        name=input("Enter the name of the new Customer : ")
        s.name=name.capitalize()
        addr=input("Enter the Adderss : ")
        s.address=addr.capitalize()
        s.tele_no =int(input("Enter the Telephone No "))                       
        print s.name
    def show_all(s):
        print ("\nName : ",s.name)
        print ("\nAddress : ",s.address)
        print ("\nTelephone No : ",s.tele_no)
    def modify(s):
        print ("\nName : ",s.name)
        s.tele_no=int(input("New Telephone No "))
    

    def report(s):          #function to show data in tabular format
        print ("%-10s"%s.name,"%-20s"%s.address,"%-10s"%s.tele_no)

    def ret_nm(s):         #function to return name
        return s.name

   

def write_tele():
    try:
        tn=telephone()
        outFile=open("tele.dat","ab")
        
        tn.new_cust()
        pickle.dump(tn,outFile)
        outFile.close()
        print ("\n\n New Telephone Number Generated  Successfully")
    except:
        pass


"""*****************************************************************************
                FUNCTION TO DISPLAY ACCOUNT DETAILS GIVEN BY USER
*****************************************************************************"""

def search_nm(n):
    flag=0
    try:
        inFile=open("tele.dat","rb")
        print ("\nCUSTOMER DETAILS\n")
        while True:
            ac=pickle.load(inFile)

            if ac.ret_nm()==n:
                ac.show_all()
                flag=1
                
    except EOFError:
        inFile.close()
        if flag==0:
            print ("\n\nTelephone number not exist")

    except IOError:
        print ("File could not be open !! Press any Key...")


"""*****************************************************************************
                        FUNCTION TO MODIFY RECORD OF FILE
*****************************************************************************"""

def modify_tele(n):
    found=0
    try:
        inFile=open("tele.dat","rb")
        outFile=open("temp.dat","wb")
        while True:
            ac=pickle.load(inFile)
            if ac.ret_nm()==n:
                print (30*"-")
                ac.show_all()
                print (30*"-")
                print ("\n\nEnter The New Telephone : ")
                ac.modify()
                pickle.dump(ac,outFile)
                print ("\n\n\tRecord Updated")
                found=1
            else:
                pickle.dump(ac,outFile)
             
    except EOFError:
        inFile.close()
        outFile.close()
        if found==0:
            print ("\n\nRecord Not Found ")

    except IOError:
        print ("File could not be open !! Press any Key...")

    os.remove("tele.dat")
    os.rename("temp.dat","tele.dat")


"""*****************************************************************************
                    FUNCTION TO DELETE RECORD OF FILE
*****************************************************************************"""

def delete_account(n):
    found=0

    try:
        inFile=open("tele.dat","rb")
        outFile=open("temp.dat","wb")
        while True:
            ac=pickle.load(inFile)
            if ac.ret_nm()==n:
                found=1
                print ("\n\n\tRecord Deleted ..")
            else:
                pickle.dump(ac,outFile)

    except EOFError:
        inFile.close()
        outFile.close()
        if found==0:
            print ("\n\nRecord Not Found")

    except IOError:
        print ("File could not be open !! Press any Key...")

    os.remove("tele.dat")
    os.rename("temp.dat","tele.dat")


"""*****************************************************************************
                    FUNCTION TO DISPLAY ALL ACCOUNT DETAILS
*****************************************************************************"""

def display_all():
    print ("\n\n\tCUSTOMER LIST\n\n")
    print (60*"=")
    print ("%-10s"%"NAME","%-20s"%"ADDRESS","%-10s"%"TELEPHONE NO")
    print (60*"=","\n")
    try:
        inFile=open("tele.dat","rb")
        while True:
            ac=pickle.load(inFile)
            ac.report()
            
    except EOFError:
        inFile.close()
        
    except IOError:
        print ("File could not be open !! Press any Key...")



"""*****************************************************************************
                        INTRODUCTORY FUNCTION
*****************************************************************************"""

def intro():
    print ("\n\n\tTELEPHONE DIRECTORY")
    print ("\n\tMANAGEMENT")
    print ("\n\n\nMADE BY : Enter your name")
    print ("\nSCHOOL : Enter your school name")


"""*****************************************************************************
                        THE MAIN FUNCTION OF PROGRAM
*****************************************************************************"""

intro()

while True:
    print ("\n\n",60*"=")
    print ("""\n\nMAIN MENU

    1. New Customer
    2. Display all 
    3. Search a telephone No.Withdraw Amount
    4. Modify Telephone No. 
    5. Delete Telphone No.
    6. Exit
    """)

    try:
        ch=int(input("Enter Your Choice(1~8): "))
        if ch==1:
            write_tele()
        
        elif ch==2:
            display_all()
            
        elif ch==3:
            nm=input("\n\nEnter Name to search : ")
            search_nm(nm)

        elif ch==4:
            nm=input("\n\nEnter Name to modify : ")
            modify_tele(nm)

        elif ch==5:
            nm=input("Enter Name to delete ")
            delete_account(nm)

        elif ch==6:
            break

        else:
            print ("Input correcr choice...(1-8)")

    except NameError:
        print ("Input correct choice...(1-6)")



 input("\n\n\n\n\nTHANK YOU\n\nPress any key to exit...")

"""*****************************************************************************
				END OF PROJECT
*****************************************************************************"""
