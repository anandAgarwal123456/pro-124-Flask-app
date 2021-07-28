from flask import Flask,jsonify, request

app = Flask(__name__)

contacts = [
    {
        "contact": "9877663547",
        "Name": "Richard",
        "done": False,
        "id": 1
    },
    {
        "contact": "9986572812",
        "Name": "Jeff",
        "done": False,
        "id": 2
    },
    {
        "contact": "7872643871",
        "Name": "Mark",
        "done": False,
        "id": 3
    },
]

@app.route("/add-contact", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    tasks = {
        'id': contacts[-1]['id'] + 1,
        'Name': request.json['Name'],
        'contact': request.json.get('contact',""),
        'done' : False
    }
    contacts.append(tasks)
    return jsonify({
        "status": "Success",
        "message": "Contact added successfully"
    })

@app.route("/get-contacts")
def get_task():
    return jsonify({
        "data" : contacts
    }) 

if(__name__ == "__main__"):
    app.run(debug=True)