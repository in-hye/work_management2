import datetime
import tkinter as tk
from tkcalendar import DateEntry
from employee_management import EmployeeDatabase
from attendance_management import AttendanceSystem

class AttendanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Management System")

        self.emp_db = EmployeeDatabase()
        self.attendance_system = AttendanceSystem()

        self.emp_id_var = tk.StringVar()
        #self.date_var = tk.StringVar()
        self.selected_date = tk.StringVar()

        self.status_var = tk.StringVar(value=" ")
        self.emp_name_var = tk.StringVar()
        self.attendance_time_var = tk.StringVar()

        self.create_widgets()

    #위젯추가
    def create_widgets(self):
        #사원번호 입력
        emp_label = tk.Label(self.root, text="사원번호:")
        emp_label.grid(row=0, column=0, padx=10, pady=5)

        emp_entry = tk.Entry(self.root, textvariable=self.emp_id_var)
        emp_entry.grid(row=0, column=1, padx=10, pady=5)

        #사원이름 입력
        emp_name_label = tk.Label(self.root, text="사원이름:")
        emp_name_label.grid(row=1, column=0, padx=10, pady=5)

        emp_name_entry = tk.Entry(self.root, textvariable=self.emp_name_var)
        emp_name_entry.grid(row=1, column=1, padx=10, pady=5)

        #출근날짜 입력
        date_label = tk.Label(self.root, text="출근날짜 (YYYY-MM-DD):")
        date_label.grid(row=2, column=0, padx=10, pady=5)

        date_entry = DateEntry(self.root, textvariable=self.selected_date, date_pattern="yyyy-mm-dd")
        date_entry.grid(row=2, column=1, padx=10, pady=5)

        date_entry = DateEntry(self.root, textvariable=self.selected_date, date_pattern="yyyy-mm-dd")
        date_entry.grid(row=2, column=1, padx=10, pady=5)
        
        #출근시간 스탬프
        attendance_time_label = tk.Label(self.root, text="출근 시간:")
        attendance_time_label.grid(row=4, column=0, padx=10, pady=5)

        self.attendance_time_value_label = tk.Label(self.root, textvariable=self.attendance_time_var)
        self.attendance_time_value_label.grid(row=4, column=1, padx=10, pady=5)

        #출근상태 입력
        status_label = tk.Label(self.root, text="출근상태:")
        status_label.grid(row=3, column=0, padx=10, pady=5)

        status_entry = tk.Entry(self.root, textvariable=self.status_var)
        status_entry.grid(row=3, column=1, padx=10, pady=5)

        #출근상태 표시창
        status_frame = tk.Frame(self.root)
        status_frame.grid(row=3, column=1, padx=10, pady=5)

        options = ["출근", "퇴근", "연차"]
        for idx, option in enumerate(options):
            tk.Radiobutton(status_frame, text=option, variable=self.status_var, value=option).grid(row=0, column=idx)
        
        #입력버튼
        mark_button = tk.Button(self.root, text="확인", command=self.mark_attendance)
        mark_button.grid(row=4, column=2, columnspan=2, padx=10, pady=5)

        get_attendance_button = tk.Button(self.root, text="근태 기록", command=self.get_attendance)
        get_attendance_button.grid(row=6, column=11, columnspan=2, padx=10, pady=5)

        add_employee_button = tk.Button(self.root, text="사원 추가", command=self.add_employee)
        add_employee_button.grid(row=1, column=2, columnspan=2, padx=10, pady=5)

        get_employee_button = tk.Button(self.root, text="사원 정보", command=self.get_employee_info)
        get_employee_button.grid(row=6, column=5, columnspan=2, padx=1, pady=1)


        attendance_label = tk.Label(self.root, text="근태기록장", font=("Helvetica", 12, "bold"))
        attendance_label.grid(row=1, column=10, padx=5, pady=2, sticky="w")

        #self.attendance_listbox = tk.Listbox(self.root)
        self.attendance_listbox = tk.Listbox(self.root, width=40)
        self.attendance_listbox.grid(row=2, column=10, rowspan=8, padx=5, pady=10)

        
        employee_label = tk.Label(self.root, text="사원목록", font=("Helvetica", 12, "bold"))
        employee_label.grid(row=1, column=4, padx=30, pady=10, sticky="w")

        self.employee_listbox = tk.Listbox(self.root)
        self.employee_listbox.grid(row=2, column=4, rowspan=8, padx=30, pady=10)

    def mark_attendance(self):
        emp_id = self.emp_id_var.get()
        status = self.status_var.get()
        
        current_time = datetime.datetime.now()
        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
        self.attendance_time_var.set(timestamp)

        self.attendance_system.mark_attendance(emp_id, timestamp, status)

    def get_attendance(self):
        emp_id = self.emp_id_var.get()

        emp_attendance = self.attendance_system.get_attendance(emp_id)

        self.attendance_listbox.delete(0, tk.END)

        if emp_attendance:
            for date, status in emp_attendance.items():
                self.attendance_listbox.insert(tk.END, f"Date: {date}, Status: {status}")
        else:
            self.attendance_listbox.insert(tk.END, "No attendance records found.")

    def add_employee(self):
        emp_id = self.emp_id_var.get()
        emp_name = self.emp_name_var.get()
        self.emp_db.add_employee(emp_id, emp_name)
        self.update_employee_list()

    def update_employee_list(self):
        self.employee_listbox.delete(0, tk.END)
        for emp_id in self.emp_db.employees.keys():
            self.employee_listbox.insert(tk.END, emp_id)

    def get_employee_info(self):
        selected_emp_index = self.employee_listbox.curselection()
        if selected_emp_index:
            selected_emp_id = self.employee_listbox.get(selected_emp_index[0])
            emp = self.emp_db.get_employee(selected_emp_id)
            if emp:
                self.emp_id_var.set(selected_emp_id)
                self.emp_name_var.set(emp.emp_name)

if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceApp(root)
    app.update_employee_list()
    root.mainloop()
