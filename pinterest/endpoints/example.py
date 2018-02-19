from flask import jsonify
from pinterest import pinterest_app, client

db = client.ejemplo  # Select the database
collection = db.notas


@pinterest_app.route("/example")
def example_select_all_queries():
    cursor = collection.find()
    vector = []
    for notas in cursor:
        print(notas)
        vector.append({
            'nota': notas['nota'],
            'materia': notas['materia']
        })
    return jsonify(vector)



@pinterest_app.route("/add")
def example_insert_query():
    cursor = collection.insert(
        {
            'nota': 100,
            'matera': 'cloud'
        }
    )
    return jsonify("added")