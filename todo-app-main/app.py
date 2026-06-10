from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []
next_id = 1

@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    global next_id
    t = request.form["task"]
    if t != "":
        tasks.append({"id": next_id, "title": t, "done": False})
        next_id += 1
    return redirect("/")

@app.route("/check/<id>")
def check(id):
    for task in tasks:
        if task["id"] == int(id):
            if task["done"] == True:
                task["done"] = False
            else:
                task["done"] = True
    return redirect("/")

@app.route("/remove/<id>")
def remove(id):
    global tasks
    new_list = []
    for task in tasks:
        if task["id"] != int(id):
            new_list.append(task)
    tasks = new_list
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
