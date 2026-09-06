employees = {
    "E101": {
        "name": "Arun",
        "department": "IT",
        "salary": 45000
    },
    "E102": {
        "name": "Ravi",
        "department": "HR",
        "salary": 60000
    },
    "E103": {
        "name": "Priya",
        "department": "IT",
        "salary": 75000
    }
}

print(employees)
print(employees.get("E102").get("name"))

for emp_id,emp_det in employees.items():
    if(emp_det.get("salary")>50000):
        print(f"Employee ID: {emp_id}, Name: {emp_det.get('name')}")