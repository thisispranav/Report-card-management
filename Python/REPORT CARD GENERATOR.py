import mysql.connector


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='1234',
    database='REPORTCARD'
)


mycursor = mydb.cursor()


def adno():
    sql = 'SELECT MAX(ADNO) FROM DETAILS'
    mycursor.execute(sql)
    a = mycursor.fetchall()
    if a[0][0] == None:
        return 0
    else:
        return a[0][0]


def getadno():
    while True:
        no = input(f'Enter Admission Number: ')
        if no.isnumeric():
            return int(no)
        else:
            print('Invalid Number !!TRY AGAIN!!')


def name(sorf):
    while True:
        Name = input(f'Enter {sorf} Name: ').upper()
        if Name.isalpha() and len(Name) <= 25:
            return Name
        elif len(Name) >= 25:
            print('The character Exits 25 !!TRY AGAIN!!')
        else:
            print('Invalid Name !!TRY AGAIN!!')


def mobno(noro):
    while True:
        no = input(f'Enter {noro}: ')
        if no.isnumeric():
            c = len(no)
            if c == 10:
                no = int(no)
                return no
            else:
                print('Number is less or more than 10 !!TRY AGAIN!!')
        else:
            print('Invalid Number !!TRY AGAIN!!')


def Class(noro):
    while True:
        cla = input(f'Enter student {noro}: ')
        if cla.isnumeric():
            cla = int(cla)
            if cla >= 1 and cla <= 12:
                return cla
            else:
                print('invalid class !Try entering a class from 1 to 12!')
        else:
            print('invalid class !Try entering a class from 1 to 12!')


def sec(noro):
    s = ['A', 'B', 'C', 'D']
    while True:
        cla = input(f'Enter student {noro}(A or B or C): ').upper()
        if cla.isalpha():
            l = len(cla)
            if l == 1 and cla in s:
                return cla
            else:
                print('invalid class !Try entering a section A or B or C')
        else:
            print('invalid class !Try entering a secction A or B or C')


def addstudent():
    N = True
    while N:
        print('----------------Form----------------')
        a = adno()+1
        print(f"Addmission Number {a}")
        b = name('Student')
        sql = f"INSERT INTO DETAILS VALUES({a},'{b}','{name('Father')}',{Class('Class')},'{sec('Section')}',{mobno('Mobile Number')})"
        mycursor.execute(sql)
        mydb.commit()
        for i in range(3):
            sql1 = f"INSERT INTO UT{i+1} (ADNO) VALUES({a})"
            mycursor.execute(sql1)
            mydb.commit()
        sql2 = f"INSERT INTO F (ADNO) VALUES({a})"
        mycursor.execute(sql2)
        mydb.commit()
        print(f'Student {b} added successfully')
        while True:
            yorn = input(
                'To add another student enter y and n to go back: ').upper()
            if yorn == 'N':
                N = False
                break
            elif yorn == 'Y':
                N = True
                break
            else:
                print('Invalid input !Try again!')


def mod1(no, where):
    print('''
    What you want to modify;
    1.Student Name
    2.Father Name
    3.Class
    4.Section
    5.Mobile Number
    6.Update all
    ''')
    while True:
        a = input('=>>')
        if a.isnumeric():
            a = int(a)
            if a == 1:
                mycursor.execute(
                    f"""update details set stuname ='{name("student's new")}' where {where} = {no} """)
                mydb.commit()
                print('Student name updated')
                break
            elif a == 2:
                mycursor.execute(
                    f"""update details set fname ='{name("Father's new")}' where {where} = {no} """)
                mydb.commit()
                print('father name updated')
                break
            elif a == 3:
                mycursor.execute(
                    f"""update details set class ={Class('new class')} where {where} = {no} """)
                mydb.commit()
                print('new class updated')
                break
            elif a == 4:
                mycursor.execute(
                    f"""update details set sec ='{sec('new section')}' where {where} = {no} """)
                mydb.commit()
                print('new section updated')
                break
            elif a == 5:
                mycursor.execute(
                    f"""update details set mobno ={mobno('new mobile number')} where {where} = {no} """)
                mydb.commit()
                print('new mobile number updated')
                break
            elif a == 6:
                print('-------update all-------')
                mycursor.execute(
                    f"""update details set stuname ='{name("student's new")}' where {where} = {no} """)
                mycursor.execute(
                    f"""update details set fname ='{name("Father's new")}' where {where} = {no} """)
                mycursor.execute(
                    f"""update details set class ={Class('new class')} where {where} = {no} """)
                mycursor.execute(
                    f"""update details set sec ='{sec('new section')}' where {where} = {no} """)
                mycursor.execute(
                    f"""update details set mobno ={mobno('new mobile number')} where {where} = {no} """)
                mydb.commit()
                print('Everything is updated')
                break
            else:
                print('choose right option !Try again!')
        else:
            print('Invalid input Try again')


def modifystudent():
    mod1(getadno(), 'adno')


def selectstudent(s):
    while True:
        print(f"""
        {s}
        1.Admission number
        2.Number
        """)
        key = input("=>")
        if key.isnumeric():
            key = int(key)
            if key == 2:
                no = mobno("Mobile Number")
                mycursor.execute(
                    f"select ADNO,STUNAME,FNAME,CLASS,SEC from details where mobno={no}")
                d = mycursor.fetchall()
                if len(d) == None or len(d) < 1:
                    print("No student was found in this number")
                    print("Try entering another number or proper admission number")
                    print()
                elif len(d) > 1:
                    x = 0
                    for i in d:
                        print()
                        x += 1
                        print(f"""
                Admission Number:{i[0]}
                Name:{i[1]}
          ({x})   Father Name:{i[2]}
                Class:{i[3]}
                Section:{i[4]}
                        """)
                    while True:
                        c = input("==>")
                        if c.isnumeric():
                            c = int(c)
                            if c > len(d) and c < len(d):
                                print("Choose a valid number try again")
                                print()
                            else:
                                return (d[c-1][0])
                        else:
                            print("Invalid Input Try again")
                            print()
                else:
                    mycursor.execute(
                        f"select ADNO from details where mobno={no}")
                    return ((mycursor.fetchall())[0][0])
            elif key == 1:
                no = getadno()
                mycursor.execute(f"select * from details where adno={no}")
                v = mycursor.fetchall()
                if len(v) != 0:
                    return no
                else:
                    print(
                        "Student Not found Try entering a Correct addmission number or mobile number")
                    print()
            else:
                print("Invalid Input Try again")
                print()
        else:
            print("Invalid input Try again")
            print()


def checkmark(sub):
    while True:
        mark = input(f"{sub}:")
        if mark.isnumeric():
            mark = int(mark)
            if mark <= 100 and mark >= 0:
                return mark
            else:
                print("Try again.... Enter a valid mark")
        elif mark.upper() == "A":
            return "A"
        else:
            print("Invalid Input.... Try again ")


def chooseterm():
    while True:
        print("""
        1) Unit test 1
        2) Unit test 2
        3) Unit test 3
        4) Final Exam
        """)
        e = [1, 2, 3]
        exam = input("=>")
        if exam.isnumeric():
            exam = int(exam)
            if exam in e:
                return f"ut{exam}"
            elif exam == 4:
                return "f"
            else:
                print("Enter a valid Input")
        else:
            print("Enter a valid input")


def enternew(adno, term):
    mycursor.execute(
        f"select sub1,sub2,SUB3,SUB4,SUB5 from {term} where adno={adno}")
    if mycursor.fetchall()[0][0] == None:
        return True
    else:
        return False


def subjects(adno):
    mycursor.execute(f"select class,sec from details where adno={adno}")
    x = mycursor.fetchall()
    if x[0][0] < 11:
        return ["English", "Tamil", "Maths", "Science", "Social"]
    else:
        if x[0][1] == 'A':
            return ["English", "Maths", "Physics", "Chemistry", "Biology"]
        elif x[0][1] == 'B':
            return ["English", "Maths", "Physics", "Chemistry", "Computer Science"]
        else:
            return ["English", "Accountancy", "Business", "Economics", "Computer Science"]


def addmark():
    while True:
        adno = selectstudent("Select student by")
        term = chooseterm()
        sub = subjects(adno)
        if enternew(adno, term):
            mycursor.execute(
                f"update {term} set sub1={checkmark(sub[0])},sub2={checkmark(sub[1])},SUB3={checkmark(sub[2])},SUB4={checkmark(sub[3])},SUB5={checkmark(sub[4])} where adno={adno}")
            mydb.commit()
            print("Marks Successfully added")
            return True
        else:
            print("Marks are already entered. Try modifying")
            return False


def modifymark():
    adno = selectstudent("Select student by")
    term = chooseterm()
    sub = subjects(adno)
    while True:
        if not enternew(adno, term):
            print(f"""
            Modify:
            1) {sub[0]}
            2) {sub[1]}
            3) {sub[2]}
            4) {sub[3]}
            5) {sub[4]}
            6) All subjects
            """)
            i = input("=>")
            e = [1, 2, 3, 4, 5]
            if i.isnumeric():
                i = int(i)
                if i in e:
                    mycursor.execute(
                        f"update {term} set sub{i}={checkmark(sub[i-1])} where adno={adno}")
                    mydb.commit()
                    print(f"{sub[i-1]} Mark is scuccessfully modified")
                    return True
                elif i == 6:
                    mycursor.execute(
                        f"update {term} set sub1={checkmark(sub[0])},sub2={checkmark(sub[1])},SUB3={checkmark(sub[2])},SUB4={checkmark(sub[3])},SUB5={checkmark(sub[4])} where adno={adno}")
                    mydb.commit()
                    return True
                else:
                    print("Choose a correct subject")
            else:
                print("Enter a valid input...Try again")
        else:
            print("Still Marks Are not Entered Try adding Marks")
            return False


def searchstudent():
    n = selectstudent("Search student by:")
    x = 0
    mycursor.execute(
        f"select ADNO,STUNAME,FNAME,CLASS,SEC from details where adno={n}")
    d = mycursor.fetchall()
    for i in d:
        print()
        x += 1
        print(f"""
                Admission Number: {i[0]}
                Name: {i[1]}
                Father Name: {i[2]}
                Class: {i[3]}
                Section: {i[4]}
                        """)


def reportcard():
    g = selectstudent("Search student by:")
    term = chooseterm()
    sub = subjects(g)
    if not enternew(g, term):
        mycursor.execute(
            f"select sub1,sub2,SUB3,SUB4,SUB5 from {term} where adno={g}")
        x = mycursor.fetchall()
        x = x[0]
        ut1, ut2, ut3, f = "Unit test 1", "Unit test 2", "unit test 3", "Final Exam"
        exam = term
        if exam == "ut1":
            n = ut1
        elif exam == "ut2":
            n = ut2
        elif exam == "ut3":
            n = ut3
        else:
            n = f
        for i in x:
            if i == "A":
                i = 0
        r = x[0]+x[1]+x[2]+x[3]+x[4]
        print(f"""
        ::::::::::::::{n}::::::::::::::
        {sub[0]}:{x[0]}
        {sub[1]}:{x[1]}
        {sub[2]}:{x[2]}
        {sub[3]}:{x[3]}
        {sub[4]}:{x[4]}
        Average Marks={r/5}
        Total Marks={r}/500
        """)
    else:
        print("Marks are not Entered yet!!")


def removestudent():
    x = selectstudent("Select Student By")
    lis = ["details", "ut1", "ut2", "ut3", "f"]
    i = input("Enter Confirm to Delete or enter anything to skip: ")
    if i.lower() == "confirm":
        for z in lis:
            mycursor.execute(f"delete from {z} where adno={x}")
            mydb.commit()
        print("Deleted Successfully !")
    else:
        print("The student is not delete")
        return


def main():
    while True:
        print("""
        1. Report card
        2. Add Marks
        3. Modify Marks
        4. Search Student
        5. Add Students
        6. Modify Student Details
        7. Remove Student
        Enter exit() to Exit
        """)
        i = input("=>")
        if i.isnumeric():
            i = int(i)
            if i == 1:
                reportcard()
            elif i == 2:
                addmark()
            elif i == 3:
                modifymark()
            elif i == 4:
                searchstudent()
            elif i == 5:
                addstudent()
            elif i == 6:
                modifystudent()
            elif i == 7:
                removestudent()
            else:
                print("Invalid Input.... Choose a Proper Option")
        elif i.lower() == "exit()":
            return
        else:
            print("Invalid Input.... Choose a Proper Option")


main()
