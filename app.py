from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from datetime import datetime

app = Flask(__name__)
api = Api(app)

# Data awal karyawan
employees = {
    "1": {
        "name": "John Doe",
        "position": "Software Engineer",
        "salary": 8000000,
        "hire_date": "2021-05-01",
        "department": "IT",
        "email": "john.doe@example.com"
    },
    "2": {
        "name": "Jane Smith",
        "position": "Product Manager",
        "salary": 10000000,
        "hire_date": "2020-03-15",
        "department": "Product",
        "email": "jane.smith@example.com"
    },
    "3": {
        "name": "Alice Johnson",
        "position": "Data Scientist",
        "salary": 9500000,
        "hire_date": "2019-11-25",
        "department": "Data",
        "email": "alice.johnson@example.com"
    },
    "4": {
        "name": "Robert Brown",
        "position": "Backend Developer",
        "salary": 7500000,
        "hire_date": "2022-01-10",
        "department": "IT",
        "email": "robert.brown@example.com"
    },
    "5": {
        "name": "Linda Wilson",
        "position": "UX Designer",
        "salary": 7200000,
        "hire_date": "2021-07-20",
        "department": "Design",
        "email": "linda.wilson@example.com"
    },
    "6": {
        "name": "Michael Taylor",
        "position": "Sales Manager",
        "salary": 9000000,
        "hire_date": "2018-06-12",
        "department": "Sales",
        "email": "michael.taylor@example.com"
    },
    "7": {
        "name": "Emily Davis",
        "position": "Frontend Developer",
        "salary": 7300000,
        "hire_date": "2022-03-05",
        "department": "IT",
        "email": "emily.davis@example.com"
    },
    "8": {
        "name": "David Anderson",
        "position": "Marketing Specialist",
        "salary": 6800000,
        "hire_date": "2019-10-22",
        "department": "Marketing",
        "email": "david.anderson@example.com"
    },
    "9": {
        "name": "Susan Thomas",
        "position": "HR Manager",
        "salary": 8500000,
        "hire_date": "2017-09-14",
        "department": "Human Resources",
        "email": "susan.thomas@example.com"
    },
    "10": {
        "name": "James Jackson",
        "position": "Quality Assurance",
        "salary": 7000000,
        "hire_date": "2020-05-27",
        "department": "QA",
        "email": "james.jackson@example.com"
    },
    "11": {
        "name": "Patricia Martinez",
        "position": "Data Analyst",
        "salary": 8000000,
        "hire_date": "2021-02-14",
        "department": "Data",
        "email": "patricia.martinez@example.com"
    },
    "12": {
        "name": "Charles Wilson",
        "position": "DevOps Engineer",
        "salary": 9000000,
        "hire_date": "2019-08-30",
        "department": "IT",
        "email": "charles.wilson@example.com"
    },
    "13": {
        "name": "Barbara Hernandez",
        "position": "Project Manager",
        "salary": 11000000,
        "hire_date": "2018-04-05",
        "department": "Project Management",
        "email": "barbara.hernandez@example.com"
    },
    "14": {
        "name": "Christopher Lewis",
        "position": "Security Analyst",
        "salary": 8800000,
        "hire_date": "2020-11-18",
        "department": "Security",
        "email": "christopher.lewis@example.com"
    },
    "15": {
        "name": "Jennifer Clark",
        "position": "Content Writer",
        "salary": 6500000,
        "hire_date": "2021-09-03",
        "department": "Content",
        "email": "jennifer.clark@example.com"
    }
}

# Class untuk menampilkan semua data karyawan
class EmployeeList(Resource):
    def get(self):
        return {
            "error": False,
            "message": "Success",
            "count": len(employees),
            "employees": employees
        }

# Class untuk menampilkan detail karyawan berdasarkan ID
class EmployeeDetail(Resource):
    def get(self, employee_id):
        if employee_id in employees:
            return {
                "error": False,
                "message": "Success",
                "employee": employees[employee_id]
            }
        return {"error": True, "message": "Employee not found"}, 404

# Class untuk menambahkan data karyawan baru
class AddEmployee(Resource):
    def post(self):
        data = request.get_json()
        employee_id = str(len(employees) + 1)
        new_employee = {
            "name": data.get("name"),
            "position": data.get("position"),
            "salary": data.get("salary"),
            "hire_date": data.get("hire_date"),
            "department": data.get("department"),
            "email": data.get("email")
        }
        employees[employee_id] = new_employee
        return {
            "error": False,
            "message": "Employee added successfully",
            "employee": new_employee
        }, 201

# Class untuk memperbarui data karyawan berdasarkan ID
class UpdateEmployee(Resource):
    def put(self, employee_id):
        if employee_id in employees:
            data = request.get_json()
            employee = employees[employee_id]
            employee["name"] = data.get("name", employee["name"])
            employee["position"] = data.get("position", employee["position"])
            employee["salary"] = data.get("salary", employee["salary"])
            employee["hire_date"] = data.get("hire_date", employee["hire_date"])
            employee["department"] = data.get("department", employee["department"])
            employee["email"] = data.get("email", employee["email"])
            return {
                "error": False,
                "message": "Employee updated successfully",
                "employee": employee
            }
        return {"error": True, "message": "Employee not found"}, 404

# Class untuk menghapus data karyawan berdasarkan ID
class DeleteEmployee(Resource):
    def delete(self, employee_id):
        if employee_id in employees:
            deleted_employee = employees.pop(employee_id)
            return {
                "error": False,
                "message": "Employee deleted successfully",
                "employee": deleted_employee
            }
        return {"error": True, "message": "Employee not found"}, 404

# Menambahkan endpoint untuk setiap resource
api.add_resource(EmployeeList, '/employees')
api.add_resource(EmployeeDetail, '/employees/<string:employee_id>')
api.add_resource(AddEmployee, '/employees/add')
api.add_resource(UpdateEmployee, '/employees/update/<string:employee_id>')
api.add_resource(DeleteEmployee, '/employees/delete/<string:employee_id>')

if __name__ == '__main__':
    app.run(debug=True)
