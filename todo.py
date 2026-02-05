tasks = [
    {
        "title": "Buy groceries",
        "done": False,
        "date_creation": "2026-01-20",
        "deadline": "2026-02-07",
        "rappel": 60,
    },
    {
        "title": "Finish Python homework",
        "done": True,
        "date_creation": "2026-01-15",
        "deadline": "2026-01-25",
        "rappel": 120,
    },
    {
        "title": "Clean the room",
        "done": False,
        "date_creation": "2026-02-01",
        "deadline": "2026-02-05",
        "rappel": 30,
    },
    {
        "title": "Read 20 pages",
        "done": False,
        "date_creation": "2026-02-03",
        "deadline": "2026-02-10",
        "rappel": 15,
    },
    {
        "title": "Call mom",
        "done": True,
        "date_creation": "2026-01-28",
        "deadline": "2026-01-28",
        "rappel": 10,
    },
]

running = True
while running:
    print("What do you want to do?\n")
    choix = input("Add / Show / Quit")

    if choix == "Add":
        titre = input("quel est cette tache ? ")
        reponse = input("Terminé ? (y/n) : ")
        conv = reponse == "y"

        date_creation = input("Date de création (YYYY-MM-DD) : ")
        deadline = input("Deadline (YYYY-MM-DD) : ")
        rappel = int(input("Rappel en minutes : "))

        task = {
            "title": titre,
            "done": conv,
            "date_creation": date_creation,
            "deadline": deadline,
            "rappel": rappel,
        }
        tasks.append(task)

    elif choix == "Show":
        i = 1
        while i <= len(tasks):
            task = tasks[i - 1]
            status = "✔" if task["done"] else "✘"
            print(f"{i}. {task['title']} [{status}]")
            print(f"   Créée le : {task['date_creation']}")
            print(f"   Deadline : {task['deadline']}")
            print(f"   Rappel : {task['rappel']} minutes")
            i += 1

    elif choix == "Quit":
        running = False
