from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

# Configure MongoDB
app.config['MONGO_URI'] = 'mongodb://localhost:27017/institute_db'
mongo = PyMongo(app)

# Department collection in MongoDB
department_collection = mongo.db.department

# Faculty collection in MongoDB
faculty_collection = mongo.db.faculty

# Route for adding a new department
@app.route('/department/add', methods=['POST'])
def add_department():
    try:
        department_data = request.json
        department_collection.insert_one(department_data)
        return jsonify({'message': 'Department added successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for updating an existing department
@app.route('/department/<department_id>', methods=['PUT'])
def update_department(department_id):
    try:
        department_data = request.json
        result = department_collection.update_one({"department_id": department_id}, {"$set": department_data})
        if result.matched_count > 0:
            return jsonify({'message': 'Department updated successfully'}), 200
        else:
            return jsonify({'message': 'Department not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for deleting an existing department
@app.route('/department/<department_id>', methods=['DELETE'])
def delete_department(department_id):
    try:
        result = department_collection.delete_one({"department_id": department_id})
        if result.deleted_count > 0:
            return jsonify({'message': 'Department deleted successfully'}), 200
        else:
            return jsonify({'message': 'Department not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for retrieving all departments
@app.route('/department', methods=['GET'])
def get_all_departments():
    try:
        department_data = list(department_collection.find({}, {'_id': 0}))
        return jsonify(department_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for adding a new faculty
@app.route('/faculty', methods=['POST'])
def add_faculty():
    try:
        faculty_data = request.json
        faculty_collection.insert_one(faculty_data)
        return jsonify({'message': 'Faculty added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for updating an existing faculty
@app.route('/faculty/<faculty_id>', methods=['PUT'])
def update_faculty(faculty_id):
    try:
        faculty_data = request.json
        result = faculty_collection.update_one({"faculty_id": faculty_id}, {"$set": faculty_data})
        if result.matched_count > 0:
            return jsonify({'message': 'Faculty updated successfully'}), 200
        else:
            return jsonify({'message': 'Faculty not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for deleting an existing faculty
@app.route('/faculty/<faculty_id>', methods=['DELETE'])
def delete_faculty(faculty_id):
    try:
        result = faculty_collection.delete_one({"faculty_id": faculty_id})
        if result.deleted_count > 0:
            return jsonify({'message': 'Faculty deleted successfully'}), 200
        else:
            return jsonify({'message': 'Faculty not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for retrieving all faculty
@app.route('/faculty', methods=['GET'])
def get_all_faculty():
    try:
        faculty_data = list(faculty_collection.find({}, {'_id': 0}))
        return jsonify(faculty_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# All Campus Routes
# Route for adding a new campus
@app.route('/campus', methods=['POST'])
def add_campus():
    try:
        campus_data = request.json
        mongo.db.campus.insert_one(campus_data)
        return jsonify({'message': 'Campus added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for updating an existing campus
@app.route('/campus/<campus_id>', methods=['PUT'])
def update_campus(campus_id):
    try:
        campus_data = request.json
        result = mongo.db.campus.update_one({"campus_id": campus_id}, {"$set": campus_data})
        if result.matched_count > 0:
            return jsonify({'message': 'Campus updated successfully'}), 200
        else:
            return jsonify({'message': 'Campus not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for deleting an existing campus
@app.route('/campus/<campus_id>', methods=['DELETE'])
def delete_campus(campus_id):
    try:
        result = mongo.db.campus.delete_one({"campus_id": campus_id})
        if result.deleted_count > 0:
            return jsonify({'message': 'Campus deleted successfully'}), 200
        else:
            return jsonify({'message': 'Campus not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for retrieving all campuses
@app.route('/campus', methods=['GET'])
def get_all_campuses():
    try:
        campus_data = list(mongo.db.campus.find({}, {'_id': 0}))
        return jsonify(campus_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
