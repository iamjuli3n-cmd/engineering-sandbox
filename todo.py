tasks = [
    {"title": "Buy groceries", "done": False},
    {"title": "Finish Python homework", "done": True},
    {"title": "Clean the room", "done": False},
    {"title": "Read 20 pages", "done": False},
    {"title": "Call mom", "done": True},
]

running = True
while running:
    print("What do you want to do?\n")
    choix = input("Add / Show / Quit")
    if choix == "Add":
        titre = input("quel est cette tache ?")
        reponse = input("Terminé ? (y/n) : ")
        conv = reponse == "y"
        task = {"title": titre, "done": conv}
        tasks.append(task)
    elif choix == "Show":
        i = 1
        while i <= len(tasks):
            task = tasks[i - 1]
            status = "✔" if task["done"] else "✘"
            print(f"{i}. {task['title']} [{status}]")
            i += 1

    elif choix == "Quit":
        running = False
