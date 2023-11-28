import sqlite3 as sql;
import sys;

c=sql.connect("testingggg_uh.db");
cursor=c.cursor()

class DOB:
    def __init__(self,Date,month,year):
        self.__Date=Date
        self.__month=month
        self.__year=year
    def getDOB(self):
        print("DOB: ")
        print(self.__Date+'/'+ self.__month +'/'+self.__year)

class Address:
    def __init__(self,Street,state,city,DoorNo):
         self.__Street=Street
         self.__state=state
         self.__city=city
         self.__DoorNo=DoorNo
    
    def getAddress(self):
        print("ADDRESS: \n")
        print(self.__DoorNo+','+self.__Street+',\n'+self.__city+',\n'+self.__state)

class wages:
    def __init__(self,PF,FA,BP,HRA,DA):
        self.__PF=PF
        self.__FA=FA
        self.__BP=BP
        self.__HRA=HRA
        self.__DA=DA
    def getwages(self):
        print("PF: ",self.__PF)
        print("FA: ",self.__FA)
        print("BP: ",self.__BP)
        print("HRA: ",self.__HRA)
        print("DA: ",self.__DA)

class clientInfo(Address):
    def __init__(self,CPhoneNo,CName,CClientID,Street,state,city,DoorNo):
        self.__CPhoneNo=CPhoneNo
        self.__CName=CName
        self.__CClientID=CClientID
        super(clientInfo,self).__init__(Street,state,city,DoorNo)

    def getclientInfo(self):
        print("Client ID: ",self.__CClientID)
        print("Client Name: ",self.__CName)
        print("Client Phone No: ",self.__CPhoneNo)
        super(clientInfo,self).getAddress()
        
class Project(clientInfo):
    def __init__(self,PID,Pduration,PName,PBudget,PDeptName,CPhoneNo,CName,CClientID,Street,state,city,DoorNo):
        self.__PID=PID
        self.__Pduration=Pduration
        self.__PName=PName
        self.__PBudget=PBudget
        self.__PDeptName=PDeptName
        super(Project,self).__init__(CPhoneNo,CName,CClientID,Street,state,city,DoorNo)
    def getProjectDetails(self):
        print("Project ID: ",self.__PID)
        print("Project Name: ",self.__PName)
        print("Project Depatment Name: ",self.__PDeptName)
        print("Project Duration: ",self.__Pduration)
        print("Project Budget: ",self.__PBudget)
        super(Project,self).getclientInfo()

class department(Project):
    def __init__(self,Dname,Dlocation,DHOD,PID,duration,PName,Budget,PhoneNo,CName,ClientID,Street,state,city,DoorNo,PDeptName):
        self.__Dname=Dname
        self.__Dlocation=Dlocation
        self.__DHOD=DHOD
        super(department,self).__init__(PID,duration,PName,Budget,PhoneNo,CName,ClientID,Street,state,city,DoorNo,PDeptName)
    def getDepartment(self):
        print("Dept Name: ",self.__Dname)
        print("Dept Location: ",self.__Dlocation)
        print("Dept HOD: ",self.__DHOD)
        super(department,self).getProjectDetails()

class Staff(department):
    def __init__(self,SID,SName,SQualification,SPhoneNumber,SDepartment,SAge,SGender,SDOJ,CStreet,Cstate,Ccity,CDoorNo,PID,duration,PName,Budget,PhoneNo,CName,
                 ClientID,Dname,Dlocation,DHOD,PDeptName):
        self.__SID=SID
        self.__SName=SName
        self.__SQualification=SQualification
        self.__SPhoneNumber=SPhoneNumber
        self.__SDepartment=SDepartment
        self.__SAge=SAge
        self.__SGender=SGender
        self.__SDOJ=SDOJ
        super(Staff,self).__init__(Dname,Dlocation,DHOD,PID,duration,PName,Budget,PhoneNo,CName,ClientID,CStreet,Cstate,Ccity,CDoorNo,PDeptName)

    def getStaffDetails(self):
        print("Staff ID: ",self.__SID)
        print("Staff Name: ",self.__SName)
        print("Staff Qualification: ",self.__SQualification)
        print("Staff PhoneNumber: ",self.__SPhoneNumber)
        print("Staff Department: ",self.__SDepartment)
        print("Staff Age: ",self.__SAge)
        print("Staff Gender: ",self.__SGender)
        print("Staff DOJ: ",self.__SDOJ)
        super(Staff,self).getDepartment()

class miin:
    ch='n'
    def options(self):
        print("\n**************************\n")
        print(" STAFF MANAGEMENT SYSTEM \n")
        print("**************************\n")
        print("1. Insert a New staff\n")
        print("2. Insert a New Project\n")
        print("3. Insert a New Department\n")
        print("4. Get all staff Details\n")
        print("5. Get all Project Details\n")
        print("6. Get all Department Details\n")
        print("7. Exit\n")
        n=int(input("Enter Your Choice :"))
        if(n==1):
            self.insertStaff();
        elif(n==2):
            self.insertProject();
        elif(n==3):
            self.insertDept();
        elif(n==4):
            self.getallstaff();
        elif(n==5):
            self.getallProjects();
        elif(n==6):
            self.getallDept();
        elif(n==7):
            print("Terminating.")
            sys.exit
    def insertStaff(self):
        try:
            #c.execute("DROP TABLE Project")
            #c.execute("DROP TABLE staff")
            #c.execute("DROP TABLE wages")
            #c.execute("DROP TABLE Department")
            #c.execute(''' create table Project(ProjectID Number(3) PRIMARY KEY,duration varchar2(25),pname varchar2(25),Budget varchar2(25),CPhoneNumber varchar2(12),CName varchar2(25),CID Number(3),Street varchar2(25),state varchar2(25),City varchar2(25),DoorNo varchar2(25));''')
            #c.execute(''' create table Department(DepartmentName varchar2(10) PRIMARY KEY,DeptLocation varchar2(25),depthod varchar2(25));''')
            #c.execute('''create table staff(staffID number(3) PRIMARY KEY,Name varchar2(25) NOT NULL,Qualifications varchar2(25),PhoneNumber varchar2(12),Department varchar2(10) references Department(DepartmentName),Age number(3),Gender varchar2(10),Datee number(2),Month number(2),Year number(4),DOJ date,Street varchar2(25),state varchar2(25),City varchar2(25),DoorNo varchar2(25),ProjectID NUMBER(3) references Project(ProjectID));''')
            #c.execute(''' create table wages(staffid number(3) references staff(staffID),pf number(10,2),fa number(10,2),bp number(10,2),hra number(10,2),da number(10,2));''')

    #35
            print("Enter Client & Project Details : \n")
            pid=int(input("Enter Project ID (<999): "))
            Pdura=input("Enter Project Duration: ")
            Pname=input("Enter Project Name: ")
            Pbudget=input("Enter Project Budget: ")
            CPhno=input("Enter Client Phone Number: (91)")
            Cname=input("Enter Client Name: ")
            CClientID=input("Enter Client ID: ")
            Cstreet=input("Enter Client Street: ")
            Cstate=input("Enter Client State: ")
            Ccity=input("Enter Client City: ")
            CDoorNo=input("Enter Client Door NO: ")
    
            if(CPhno.startswith("91")):
                cursor.execute("INSERT INTO PROJECT values (?,?,?,?,?,?,?,?,?,?,?)",(pid,Pdura,Pname,Pbudget,CPhno,Cname,CClientID,Cstreet,Cstate,Ccity,CDoorNo))
            else:
                print("Please Enter correct phone number");
                miin.getops(self)
            print("Enter Department Details: ")
            Dna=input("Enter Department Name: ")
            Dloc=input("Enter Department Location: ")
            Dhod=input("Enter Department HOD: ")
    
            cursor.execute("INSERT INTO DEPARTMENT VALUES(?,?,?)",(Dna,Dloc,Dhod))
    
            print("Enter Staff Details: ")
            SID=int(input("Enter Staff ID(<999) : "))
            SName=input("Enter Staff Name: ")
            SQua=input("Enter Staff Qualification: ")
            Sph=input("Enter Staff PhoneNumber: (91)")
            SDept=input("Enter Staff Department:(CASE SENSITIVE AND UNIQUE) ")
            Sage=input("Enter Staff Age: ")
            Sgen=input("Enter Staff Gender: ")
    
            Sdate=input("Enter Date (DD): ")
            Smon=input("Enter Month (MM): ")
            Syr=input("Enter Year (YYYY): ")
            Sdoj=input("Enter DOJ: (YYYY-MM-DD)")
    
            DOBobj=DOB(Sdate,Smon,Syr)
    
            print("Enter Staff Address: ")
            Sstre=input("Enter Staff Street: ")
            Sstat=input("Enter Staff State: ")
            Scity=input("Enter Staff city: ")
            Sdoor=input("Enter Door No: ")
        
            Addressobj=Address(Sstre,Sstat,Scity,Sdoor)
    
            Pdeptname=input("Enter the Project ID that the staff is allocated to: ")
    #16
            cursor.execute("insert into staff values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(SID,SName,SQua,Sph,SDept,Sage,Sgen,Sdate,Smon,Syr,Sdoj,Sstre,Sstat,Scity,Sdoor,Pdeptname));
    
            print("Enter Salary Details: ")
            pf=float(input("Enter PF: "))
            fa=float(input("Enter FA: "))
            bp=float(input("Enter BP: "))
            hra=float(input("Enter HRA: "))
            da=float(input("Enter DA: "))

            wagesobj=wages(pf,fa,bp,hra,da)
    
            cursor.execute("INSERT INTO WAGES VALUES(?,?,?,?,?,?)",(SID,pf,fa,bp,hra,da));
    
            x=Staff(SID,SName,SQua,Sph,SDept,Sage,Sgen,Sdoj,Cstreet,Cstate,Ccity,CDoorNo,pid,Pdura,Pname,Pbudget,CPhno,Cname,CClientID,Dna,Dloc,Dhod,Pdeptname)

            print("***************************************************************");
            '''x.getStaffDetails()
            print("Staff Date of Birth: ")
            DOBobj.getDOB()
            print("Staff Address & salary details: ")
            Addressobj.getAddress()
            wagesobj.getwages()'''
        except sql.DatabaseError as e:
            print("Error Details: ",e)
        finally:
            c.commit();
            miin.getops(self);

    def insertProject(self):
        try:
            print("Enter Project Details : \n")
            pid=int(input("Enter Project ID (<999): "))
            Pdura=input("Enter Project Duration: ")
            Pname=input("Enter Project Name: ")
            Pbudget=input("Enter Project Budget: ")
            CPhno=input("Enter Client Phone Number: (91)")
            Cname=input("Enter Client Name: ")
            CClientID=input("Enter Client ID: ")
            Cstreet=input("Enter Client Street: ")
            Cstate=input("Enter Client State: ")
            Ccity=input("Enter Client City: ")
            CDoorNo=input("Enter Client Door NO: ")
    
            if(CPhno.startswith("91")):
                cursor.execute("INSERT INTO PROJECT values (?,?,?,?,?,?,?,?,?,?,?)",(pid,Pdura,Pname,Pbudget,CPhno,Cname,CClientID,Cstreet,Cstate,Ccity,CDoorNo))
            else:
                print("Please enter correct Phone number");
                miin.getops(self)
        except sql.DatabaseError as e:
            print("Error at InsertProject()",end='\n');
            print("Error Details: ",e)
        finally:
            c.commit();
            miin.getops(self);

    def insertDept(self):
        try:
            print("Enter Department Details: ")
            Dna=input("Enter Department Name: ")
            Dloc=input("Enter Department Location: ")
            Dhod=input("Enter Department HOD: ")
    
            cursor.execute("INSERT INTO DEPARTMENT VALUES(?,?,?)",(Dna,Dloc,Dhod))
        except sql.DatabaseError as e:
            print("Error at InsertDept()",end='\n');
            print("Error Details: ",e)
        finally:
            c.commit();
            miin.getops(self);
        
    def getallstaff(self):
        cursor.execute("select * from Staff");
        for i in cursor.fetchall():
            print(i)
        miin.getops(self)

    def getallProjects(self):
        cursor.execute("select * from Project");
        for i in cursor.fetchall():
            print(i)
        miin.getops(self)

    def getallDept(self):
        cursor.execute("select * from Department");
        for i in cursor.fetchall():
            print(i)
        miin.getops(self)

    def getops(self):
        ch=input("Do you wish to continue(y/n)")
        if(ch=='y' or ch=='Y'):
            miin.options(self);
        else:
            print("Terminating.")
            sys.exit

#main code starts here
main=miin()
main.options()
#main.getops()
