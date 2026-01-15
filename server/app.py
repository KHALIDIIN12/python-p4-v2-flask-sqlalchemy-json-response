from flask import Flask, make_response
from flask_migrate import Migrate
from models import db, Employee, Department

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# This makes the JSON look "pretty" in your browser
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    return make_response({"message": "Welcome to the Company API!"}, 200)

@app.route('/employees/<int:id>')
def employee_by_id(id):
    # Query the database for the specific employee
    emp = Employee.query.filter_by(id=id).first()

    if emp:
        # Create a dictionary (JSON-friendly)
        emp_dict = {
            "id": emp.id,
            "name": emp.name,
            "salary": emp.salary,
            "department": emp.department.name # Accessing the relationship!
        }
        return make_response(emp_dict, 200)
    else:
        return make_response({"error": "Employee not found"}, 404)

if __name__ == '__main__':
    app.run(port=5555, debug=True)