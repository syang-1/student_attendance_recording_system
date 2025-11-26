import getpass
from datetime import datetime

attendance_record = {}
monthly_record = {}

current_date = datetime.now().strftime("%B %d, %Y")
current_day = datetime.now().strftime("%d")

USERNAME = "teacher"
PASSWORD = "12345"

SECTIONS = {
    "FB2-BSIT1-01": sorted([
        "CASUMPANG, PRINCESS DIVINE C.", "OCO, HERSHEY GABRIELLE C.",
        "CABANES, PHOEBE JADE M.", "BELTRAN, ANDRIE JAY A. "
    ]),
    "FB2-BSIT1-02": sorted([
        "CIELO, ELIZA NIÑA MARIE P. ", "DIMAL, SAANODIN M.", 
        "JAMAR, JOHN CLINT A.", "HAMILI, MARCJHON A.",
        "CAGATIN, FRITZ DENVER JOHN", "BACORNAY, VERHEL", 
        "CABEÑEROS, CARLO JOHN L.", "CABASON, ZOE BLESS M.", 
        "PAYOT, LEEPRIL"
        ]),
    "FB2-BSIT1-03": sorted([
        "SACAY, APRIL MAE M. ", "CUYNO, DEXTER P.", 
        "ASANULLA, AMINA M.", "LONGOS, EZEQUEL KHAEL KASHMER", 
        "BERNALES, JOHN MARK P.", "RANAO, CLYDE MARK D.", 
        "JUMAWAN, ANGELOU D. ", "MORALES, HERCIE JEAN Y.", 
        "PAGTALUNAN. VINCENT DAVE E. "
    ]),
    "FB2-BSIT1-04": sorted([
        "GO, EZEKEIL LEO P.", "CABAHUG, BENCH M.", 
        "LUSTERIO, KERBY ADRIENE H.", "PADILLA, NICOLE", 
        "LLABAN, ALLISON KYLE B.", "UY, PRINCE RUSSEL D.", 
        "FLORENDO, JOSUA E.", "SALVALEON, FELY", 
        "JEMENIA, MELVIN L.", "TAN, ANDREW L.", 
        "GUBAT, MEL ANJELO L.", "LOPENA, NOEL JOHN B."
    ])
}

def login(): 
    print("\n--- TEACHER LOGIN ---")
    while True:
        user = input("Enter Username: ").strip()
        pw = getpass.getpass("Enter Password: ").strip()
        if user == USERNAME and pw == PASSWORD:
            print("\nLogin Successful! Welcome Teacher! \n")
            return True
        else:
            print("Invalid username or password! Try again.\n")
        
def select_section():
    print ("\nSELECT SECTION")
    keys = list(SECTIONS.keys())
    for i, section in enumerate(keys, 1): 
        print (f"{i}. {section}")
    print (f"{len (keys) +1}. BACK")
    
    choice = input("Enter choice: ").strip()
    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(keys):
            return keys[choice-1]
        elif choice == len(keys)+1:
            return None

    print("Invalid choice!")
    return None
    
def mark_attendance(section_name):
    section = SECTIONS[section_name]
    print (f"\n*** Marking Attendance for {section_name} ***")
    print ("\nFULL NAME | ATTENDANCE (P/A) ")
    print ("-" * 50)
    
    attendance_record.clear()
    
    for student in section:
        while True:
            status = input(f"{student} - ").strip().upper()
            if status in ['P', 'A']:
                attendance_record[student] = "Present" if status == "P" else "Absent"
                break
            print("Invalid! Only P or A accepted.")
            
    monthly_record[current_day] = attendance_record.copy()
    print("\nAttendance recorded successfullt!\n")

def view_summary_student ():
    print ("\n--- Summary Per Student --_")
    name_input = input("Enter FULL student name: ").strip().upper()
    
    found_name = None
    for section in SECTIONS.values():
        for student in section:
            if student.upper() == name_input:
                found_name = student
                break
        if not found_name:
            print("Student not found.")
            return
            
        present = sum(1 for d in monthly_record.values() if d.get(found_name) == "Present")
        absent = sum(1 for d in monthly_record.values() if d.get (found_name) == "Absent")
        
        print ("\nFULL NAME | PRESENT | ABSENT")
        print("_" * 40)
        print(f"{found_name} | {present} | {absent}")
        
def generate_monthly():
    print("\n--- Monthly Attendance Report ---")
    if not monthly_record:
        print("No records for this month yet.")
        return
    
    summary = {}
    for daily in monthly_record.values():
        for student, status in daily.items():
            if student not in summary:
                summary [student] = {"Present": 0, "Absent": 0}
            summary [student][status] += 1
    
    print ("\nFULL NAME | PRESENT | ABSENT")
    print ("_" * 45) 
    for student, count in summary.items():
        print(f"{student} | {count[ 'Present' ]} | {count['Absent' ]}")
        
def teacher_menu() :
    while True:
        print("\n=== TEACHER MENU ===")
        print("1. SECTION (Take Attendance)")
        print("2. VIEW SUMMARY PER STUDENT")
        print("3. GENERATE REPORT")
        print("4. LOG OUT")
        print("5. EXIT SYSTEM")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            section = select_section()
            if section:
                mark_attendance(section)
        elif choice == "2":
            view_summary_student()
        elif choice == "3":
            generate_monthly()
        elif choice == "4":
            print("\nLogged Out. Returning Welcome Teacher\n")
            return 'LOGOUT'
        elif choice == "5":
            return 'EXIT'
        else:
            print("Invalid choice!")
            
def post_login_menu():
    while True:
        print("\n=== WELCOME TEACHER ===")
        print("1. Teacher ")
        print("2. Exit")
        
        menu_choice = input("Enter choice: ").strip()
        
        if menu_choice == '1': 
            teacher_status = teacher_menu()
            if teacher_status == 'EXIT':
                return 'EXIT'
        elif menu_choice == '2':
            return 'EXIT'
        else:
            print ("Invalid choicel Please enter 1 or 2.")

print ("STUDENT ATTENDANCE RECORDING SYSTEM")
print("Date:", current_date)
print("=" * 50)




if login():
    while True:
        system_status = post_login_menu()
        if system_status == 'EXIT':
            print("\nThank you for Using Our System! God Bless")
            break