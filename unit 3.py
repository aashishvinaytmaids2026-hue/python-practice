#menu-driven Student Information System 
students={}
def add_student():
    roll=input("Enter Roll No")
    name=input("enter name:")
    dept=input("enter department:")
    students[roll]={"name":name,"department":dept}
    print("student added successfully")
def view_student():
    if not students:
        print("no students record found")
        return
    print("\n--student records--")
    for roll,data in students.items():
        print("roll noo:",roll,
              "| name:",data["name"],
              "| department:",data["department"])
def search_student():
    roll=input("enter roll no to search")
    if roll in students:
        print(students[roll])
    else:
        print("student not found")
def delete_student():
    roll=input("enter roll no to delete:")
    if roll in students:
        del students[roll]
        print("student deleted successfully:")
    else:
        print("student not found")
while True:
    print("\n1.Add Student")
    print("2.View Student:")
    print("3.Search Student")
    print("4.Delete Student")
    print("5.exit")
    choice=input("Enter your choice:")
    if choice=="1":
        add_student()
    elif choice=="2":
        view_student()
    elif choice=="3":
        search_student()
    elif choice=="4":
        delete_student()
    elif choice=="5":
        print("Exiting..")
        break 
    else:
        print("invalid choice:")
    