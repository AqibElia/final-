from flask import Flask, jsonify,request
app= Flask(__name__)
courses = [
{"id": 1, "title": "Devops Engineering" , "instructor": "Memoona Amjad"},
{"id": 21, "title": "software  Design " , "instructor": "Dr. Adnan"} ]
@app.route('/api/course' , methods=['GET'])
def get_data():
    return jsonify(courses)

# @app.route('/api/course<int:id>' , methods=['GET'])
# def get_data(s):
#     course= Next((s for s in['id'] == id),None)
#     return jsonify(course)
# @app.route('/api/course' , method['POST'])
# def get_data():
from flask import Flask, jsonify,request
app= Flask(__name__)
courses = [
{"id": 1, "title": "Devops Engineering" , "instructor": "Memoona Amjad"},
{"id": 21, "title": "software  Design " , "instructor": "Dr. Adnan"} ]
@app.route('/api/course' , methods=['GET'])
def get_data():
    return jsonify(courses)

# @app.route('/api/course<int:id>' , methods=['GET'])
# def get_data(s):
#     course= Next((s for s in['id'] == id),None)
#     return jsonify(course)
# @app.route('/api/course' , method['POST'])
# def get_data():
#     data= request.get.json()
#     new_course={
#         "id":len(courses)+1 
#         "title": data.get['title'] 
#         "instructor": data.get['instructor']
#     }
#     return jsonify(courses)

# @app.route('/api/course' , methods=['PUT'])
# def get_data():
#     course= Next((s for s in['id'] == id),None)
#     data=request.get_json()
#     courses['name']=data.get['title']
#     courses['instructor']=data.get['instructor']
#     return jsonify(course)
if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)



#     data= request.get.json()
#     new_course={
#         "id":len(courses)+1 
#         "title": data.get['title'] 
#         "instructor": data.get['instructor']
#     }
#     return jsonify(courses)

# @app.route('/api/course' , methods=['PUT'])
# def get_data():
#     course= Next((s for s in['id'] == id),None)
#     data=request.get_json()
#     courses['name']=data.get['title']
#     courses['instructor']=data.get['instructor']
#     return jsonify(course)
if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)







