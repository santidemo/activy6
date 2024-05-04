from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Hacer compras", "description": "Comprar leche y huevos", "done": False},
    {"id": 2, "title": "Llamar al médico", "description": "Hacer una cita con el médico", "done": False}
]


# Obtener todas las tareas
@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


# Obtener una tarea por su ID
@app.route("/api/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return jsonify(task), 200
    return jsonify(message="Tarea no encontrada"), 404


# Actualizar una tarea por su ID
@app.route("/api/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = request.json["title"]
            task["description"] = request.json.get("description", "")
            task["done"] = request.json.get("done", False)
            return jsonify(message="Tarea actualizada exitosamente"), 200
    return jsonify(message="Tarea no encontrada"), 404


# Eliminar una tarea por su ID
@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return jsonify(message="Tarea eliminada exitosamente"), 200
    return jsonify(message="Tarea no encontrada"), 404


if __name__ == "__main__":
    app.run()