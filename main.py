import Read_Hospital_Excel_Sheet
import Write_Hospital_Excel_Sheet


print("****************************************************************************")
print("*                                                                          *")
print("*                   Welcome Hospital Management System                     *")
print("*                                                                          *")
print("****************************************************************************")
    
    
tries = 0
tries_flag = ""
while tries_flag != "Close the program" :
        Pateints_DataBase = Read_Hospital_Excel_Sheet.Read_Patients_DataBase()
        Doctors_DataBase  = Read_Hospital_Excel_Sheet.Read_Doctors_DataBase()
                
        print("-----------------------------------------")
        print("|Enter 1 for Admin mode          |\n|Enter 2 for user mode           |")
        print("-----------------------------------------")
        Admin_user_mode = input("Enter your mode : ") 
        

        if Admin_user_mode == "1" :
                print("*****************************************\n|         Welcome to admin mode         |\n*****************************************")
                Password = input("enter your password : ")
                while True :
                    
                    if Password == "SRMAP123" :
                        print("-----------------------------------------")
                        print("|To edit patients Enter 1      |\n|To edit docotrs Enter 2       |\n|To be back Enter B            |")
                        print("-----------------------------------------")
                        Admin_Options = input ("Enter your choice : ")
                        Admin_Options = Admin_Options.upper()
                        
                        if Admin_Options == "1" :
                                print("-----------------------------------------")
                                print("1)|To add new patient           |")
                                print("2)|To display patient           |")
                                print("3)|To delete patient DataBase   |")
                                print("4)|To edit patient DataBase     |")
                                print("5)|To Back enter B              |")
                                print("-----------------------------------------")
                                Admin_choice = input ("Enter your choice : ")
                                Admin_choice = Admin_choice.upper()
                                
                                if Admin_choice == "1" :
                                            try :       
                                                patient_ID = int(input("Enter patient ID : "))
                                                while patient_ID in Pateints_DataBase :     
                                                    patient_ID = int(input("This ID is available, please try another ID : "))                 
                                                Department=input("Enter patient department                : ")
                                                DoctorName=input("Enter name of doctor following the case : ")
                                                Name      =input("Enter patient name                      : ")
                                                Age       =input("Enter patient age                       : ")
                                                Gender    =input("Enter patient gender                    : ")
                                                phone     =input("Enter patient phone no                  : ")
                                                RoomNumber=input("Enter patient room number               : ")
                                                Pateints_DataBase[patient_ID]=[Department,DoctorName,Name,Age,Gender,phone,RoomNumber]
                                                print("----------------------Patient added successfully----------------------")
                                            except :
                                                print("ENETR VALID INPUT")
                                        
                                elif Admin_choice == "2" :
                                            try :       
                                                patient_ID = int(input("Enter patient ID : "))
                                                while patient_ID not in Pateints_DataBase :
                                                    patient_ID = int(input("Incorrect ID, Please Enter patient ID : "))
                                                print(patient_ID)
                                                print("\npatient name        : ",Pateints_DataBase[patient_ID][2])
                                                print("patient age         : ",Pateints_DataBase[patient_ID][3])
                                                print("patient gender      : ",Pateints_DataBase[patient_ID][4])
                                                print("patient phone no    : ",Pateints_DataBase[patient_ID][5])
                                                print("patient room number : ",Pateints_DataBase[patient_ID][6])
                                                print("patient is in "+Pateints_DataBase[patient_ID][0]+" department")
                                                print("patient is followed by doctor : "+Pateints_DataBase[patient_ID][1])
                                            except :
                                                print("ENTER VALID INPUT")
                                
                                elif Admin_choice == "3" :                                      
                                            try :       
                                                patient_ID = int(input("Enter patient ID : "))
                                                while patient_ID not in Pateints_DataBase :
                                                    patient_ID = int(input("Incorrect ID, Please Enter patient ID : "))
                                                Pateints_DataBase.pop(patient_ID)
                                                print("----------------------Patient DataBase deleted successfully----------------------")
                                            except :
                                                print("ENTER VALID INPUT")
                                        
                                elif Admin_choice == "4" :                                      
                                            try :       
                                                patient_ID=int(input("Enter patient ID : "))
                                                while patient_ID not in Pateints_DataBase :
                                                    patient_ID = int(input("Incorrect ID, Please Enter patient ID : "))
                                                while True :
                                                    print("------------------------------------------")
                                                    print("1)|To Edit pateint Department :    |")
                                                    print("2)|To Edit Doctor following case : |")
                                                    print("3)|To Edit pateint Name :          |")
                                                    print("4)|To Edit pateint Age :           |")
                                                    print("5)|To Edit pateint Gender :        |")
                                                    print("6)|To Edit pateint phone no :      |")
                                                    print("7)|To Edit pateint RoomNumber :    |")
                                                    print("8)|To be Back Enter B                      |")
                                                    print("-----------------------------------------")
                                                    Admin_choice = input("Enter your choice : ")
                                                    Admin_choice = Admin_choice.upper()
                                                    if Admin_choice == "1" :
                                                        Pateints_DataBase[patient_ID][0]=input("\nEnter patient department : ")
                                                        print("----------------------Patient Department edited successfully----------------------")
                                                        
                                                    elif Admin_choice == "2" :
                                                        Pateints_DataBase[patient_ID][1]=input("\nEnter Doctor follouing case : ")
                                                        print("----------------------Doctor follouing case edited successfully----------------------")
                                        
                                                    elif Admin_choice == "3" :
                                                        Pateints_DataBase[patient_ID][2]=input("\nEnter patient name : ")
                                                        print("----------------------Patient name edited successfully----------------------")
                                                    
                                                    elif Admin_choice == "4" :
                                                        Pateints_DataBase[patient_ID][3]=input("\nEnter patient Age : ")
                                                        print("----------------------Patient age edited successfully----------------------")
                                                
                                                    elif Admin_choice == "5" :
                                                        Pateints_DataBase[patient_ID][4]=input("\nEnter patient gender : ")
                                                        print("----------------------Patient address gender successfully----------------------")
                                                        
                                                    elif Admin_choice == "6" :
                                                        Pateints_DataBase[patient_ID][5]=input("\nEnter patient phone no : ")
                                                        print("----------------------Patient phone no edited successfully----------------------")
                                                        
                                                    elif Admin_choice == "7" :
                                                        Pateints_DataBase[patient_ID][6]=input("\nEnter patient RoomNumber : ")
                                                        print("----------------------Patient RoomNumber edited successfully----------------------")
                                                
                                                    elif Admin_choice == "B" :
                                                        break
                                                        
                                                    else :
                                                        print("Please Enter a correct choice")
                                            except :
                                                print("Patient ID should be an integer number")
                                                                             
                                else :
                                            print("Please enter a correct choice\n")
                                            
                        elif Admin_Options == "2" :                                                          
                            print("-----------------------------------------")
                            print("1)|To add new doctor              |")
                            print("2)|To display doctor              |")
                            print("3)|To delete doctor DataBase      |")
                            print("4)|To edit doctor DataBase        |")
                            print("5)|To be back enter B             |")
                            print("-----------------------------------------")
                            Admin_choice = input ("Enter your choice : ")
                            Admin_choice = Admin_choice.upper()
                            
                            if Admin_choice == "1" :                                            
                                    try :       
                                        Doctor_ID = int(input("Enter doctor ID : "))
                                        while Doctor_ID in Doctors_DataBase :           
                                            Doctor_ID = int(input("This ID is unavailable, please try another ID : "))
                                        
                                        Department=input("Enter Doctor department : ")
                                        Name      =input("Enter Doctor name       : ")
                                        phone     =input("Enter Doctor phone no   : ")
                                        Doctors_DataBase[Doctor_ID]=[[Department,Name,phone]]
                                        print("----------------------Doctor added successfully----------------------")
                                    except :
                                        print("ENTER VALID INPUT")
                                
                            elif Admin_choice == "2" :                                          
                                    try :       
                                        Doctor_ID = int(input("Enter doctor ID : "))
                                        while Doctor_ID not in Doctors_DataBase :
                                            Doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
                                        print("Doctor name    : ",Doctors_DataBase[Doctor_ID][0][1])
                                        print("Doctor phone no : ",Doctors_DataBase[Doctor_ID][0][2])
                                        print("Doctor is in "+Doctors_DataBase[Doctor_ID][0][0]+" department")
                                    except :
                                        print("ENTER VALID INPUT")
                            
                            elif Admin_choice == "3" :                                          
                                    try :      
                                        Doctor_ID = int(input("Enter doctor ID : "))
                                        while Doctor_ID not in Doctors_DataBase :
                                            Doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
                                        Doctors_DataBase.pop(Doctor_ID)
                                        print("/----------------------Doctor DataBase deleted successfully----------------------/")
                                    except :
                                        print("ENTER VALID INPUT")

                            elif Admin_choice == "4" :                                          
                                    try :       
                                        Doctor_ID=input("Enter doctor ID : ")
                                        while Doctor_ID not in Doctors_DataBase :
                                            Doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
                                        print("-----------------------------------------")
                                        print("1)|To Edit doctor's department    |")
                                        print("2)|To Edit doctor's name          |")
                                        print("3)|To Edit doctor's phone no      |")
                                        print("4)To be Back Enter B              |")
                                        print("-----------------------------------------")
                                        Admin_choice=input("Enter your choice : ")
                                        Admin_choice = Admin_choice.upper()
                                        if Admin_choice == "1" :
                                            Doctors_DataBase[Doctor_ID][0][0]=input("Enter Doctor's Department : ")
                                            print("/----------------------Doctor's department edited successfully----------------------/")
                                            
                                        elif Admin_choice == "2" :
                                            Doctors_DataBase[Doctor_ID][0][1]=input("Enter Doctor's Name : ")
                                            print("----------------------Doctor's name edited successfully----------------------")
                                            
                                        elif Admin_choice == "3" :
                                            Doctors_DataBase[Doctor_ID][0][2]=input("Enter Doctor's phone no : ")
                                            print("----------------------Doctor's phone no edited successfully----------------------")
                                        
                                        elif Admin_choice == "B" :
                                            break
                                        
                                        else :
                                            print("\nPlease enter a correct choice\n")
                                            
                                    except :
                                        print("Doctor ID should be an integer number")
                                            
                            elif Admin_choice == "B" :                                          
                                        break
                                    
                            else :
                                print("\nPlease enter a correct choice\n")
                        elif Admin_Options == "B":
                                break;
                    elif Password != "SRMAP123" :
                        if tries < 2 :
                            Password = input("Password incorrect, please try again : ")
                            tries += 1
                        else :
                            print("Incorrect password, no more tries")
                            tries_flag = "Close the program"
                            break
                
                    Write_Hospital_Excel_Sheet.Write_Patients_DataBase(Pateints_DataBase)
                    Write_Hospital_Excel_Sheet.Write_Doctors_DataBase(Doctors_DataBase)
                    
                    
        elif Admin_user_mode == "2" :                                                                      
            print("****************************************\n|         Welcome to user mode         |\n****************************************")
            while True :
                print("\n-----------------------------------------")
                print("1)|To view hospital's departments |")
                print("2)|To view hospital's docotrs     |")
                print("3)|To view patients' residents    |")
                print("4)|To view patient's details      |")
                print("5)|To be Back Enter B             |")
                print("-----------------------------------------")
                User_Options = input("Enter your choice : ")
                User_Options = User_Options.upper()
                if User_Options == "1" :
                            print("Hospital's departments :")
                            for i in Doctors_DataBase :
                                print(" "+Doctors_DataBase[i][0][0])
                    
                elif User_Options == "2" :                                           
                            print("Hospital's doctors :")
                            for i in Doctors_DataBase :
                                print(" ",Doctors_DataBase[i][0][1]," in ",Doctors_DataBase[i][0][0]," department, ",Doctors_DataBase[i][0][2])
                                
                elif User_Options == "3" :                                           
                    for i in Pateints_DataBase :
                        print(" name        : ",Pateints_DataBase[i][2])
                        print(" age         : ",Pateints_DataBase[i][3])
                        print(" gender      : ",Pateints_DataBase[i][4])
                        print(" phone no    : ",Pateints_DataBase[i][5])
                        print(" room number : ",Pateints_DataBase[i][6])
                        print(" patient is in ",Pateints_DataBase[i][0]," department")
                        print(" patient is followed by doctor : ",Pateints_DataBase[i][1])
                        print("-----------------------------------------")
                elif User_Options == "4" :                                           
                    try :               
                        patient_ID = int(input("Enter patient's ID : "))
                        while patient_ID not in Pateints_DataBase :
                            patient_ID = int(input("Incorrect Id, Please enter patient ID : "))
                        print(" name        : ",Pateints_DataBase[patient_ID][2])
                        print(" age         : ",Pateints_DataBase[patient_ID][3])
                        print(" gender      : ",Pateints_DataBase[patient_ID][4])
                        print(" phone no    : ",Pateints_DataBase[patient_ID][5])
                        print(" room number : ",Pateints_DataBase[patient_ID][6])
                        print(" department  : "+Pateints_DataBase[patient_ID][0])
                        print(" doctor      : "+Pateints_DataBase[patient_ID][1])
                    except :
                        print("Patient ID should be an integer number")
                elif User_Options == "B":
                        break
        elif Admin_user_mode=="B":
                break
        else :
            print("Please choice just 1 or 2")
