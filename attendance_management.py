class AttendanceSystem:
    def __init__(self):
        self.attendance_records = {}

    def mark_attendance(self, emp_id, date, status):
        if emp_id not in self.attendance_records:
            self.attendance_records[emp_id] = {}
        self.attendance_records[emp_id][date] = status

    def get_attendance(self, emp_id):
        return self.attendance_records.get(emp_id, {})


if __name__ == "__main__":
    attendance_system = AttendanceSystem()

    attendance_system.mark_attendance("E001", "2023-08-29", "Present")
    attendance_system.mark_attendance("E002", "2023-08-29", "Absent")

    emp_attendance = attendance_system.get_attendance("E001")
    if emp_attendance:
        for date, status in emp_attendance.items():
            print(f"Date: {date}, Status: {status}")
