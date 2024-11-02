from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Contoh data karyawan untuk keperluan pengujian
employees = [
    {"id": 1, "name": "Alice Johnson", "position": "Software Engineer", "salary": 6000},
    {"id": 2, "name": "Bob Smith", "position": "Product Manager", "salary": 7500},
    {"id": 3, "name": "Carol White", "position": "Data Analyst", "salary": 5800},
    {"id": 4, "name": "David Brown", "position": "UX Designer", "salary": 5400},
    {"id": 5, "name": "Emma Davis", "position": "Marketing Specialist", "salary": 5100},
    {"id": 6, "name": "Frank Wilson", "position": "DevOps Engineer", "salary": 6700},
    {"id": 7, "name": "Grace Lee", "position": "QA Engineer", "salary": 5000},
    {"id": 8, "name": "Henry Thompson", "position": "Frontend Developer", "salary": 6300},
    {"id": 9, "name": "Isla Martin", "position": "HR Manager", "salary": 6200},
    {"id": 10, "name": "Jack Garcia", "position": "Backend Developer", "salary": 6500},
    {"id": 11, "name": "Karen Martinez", "position": "Project Manager", "salary": 7000},
    {"id": 12, "name": "Liam Robinson", "position": "Cloud Architect", "salary": 8000},
    {"id": 13, "name": "Mia Clark", "position": "Business Analyst", "salary": 5500},
    {"id": 14, "name": "Noah Rodriguez", "position": "Network Engineer", "salary": 6100},
    {"id": 15, "name": "Olivia Lewis", "position": "Full Stack Developer", "salary": 6900}
]

class EmployeeList(Resource):
    def get(self):
        return {
            "error": False,
            "message": "success",
            "count": len(employees),
            "employees": employees
        }

    def post(self):
        data = request.get_json()
        new_employee = {
            "id": len(employees) + 1,
            "name": data["name"],
            "position": data["position"],
            "salary": data["salary"]
        }
        employees.append(new_employee)
        return {"error": False, "message": "Employee added successfully", "employee": new_employee}, 201

class EmployeeDetail(Resource):
    def get(self, employee_id):
        employee = next((emp for emp in employees if emp["id"] == employee_id), None)
        if employee:
            return {"error": False, "message": "success", "employee": employee}
        return {"error": True, "message": "Employee not found"}, 404

    def put(self, employee_id):
        data = request.get_json()
        employee = next((emp for emp in employees if emp["id"] == employee_id), None)
        if employee:
            employee.update(data)
            return {"error": False, "message": "Employee updated successfully", "employee": employee}
        return {"error": True, "message": "Employee not found"}, 404

    def delete(self, employee_id):
        global employees
        employees = [emp for emp in employees if emp["id"] != employee_id]
        return {"error": False, "message": "Employee deleted successfully"}, 200

# Tambahkan resources ke API
api.add_resource(EmployeeList, '/employees')
api.add_resource(EmployeeDetail, '/employees/<int:employee_id>')

if __name__ == "__main__":
    app.run(debug=True)
