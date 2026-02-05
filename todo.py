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
    choix = input("Add / Show / Modify / Quit")

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

    elif choix == "Modify":
        i = 1
        while i <= len(tasks):
            print(f"{i}. {tasks[i - 1]['title']}")
            i += 1

        index = int(input("Numéro de la task à modifier : ")) - 1

        if 0 <= index < len(tasks):
            task = tasks[index]

            print("\nQue veux-tu modifier ?")
            print("1. Titre")
            print("2. Terminé")
            print("3. Date de création")
            print("4. Deadline")
            print("5. Rappel")

            choix_modif = input("Choix : ")

            if choix_modif == "1":
                task["title"] = input("Nouveau titre : ")

            elif choix_modif == "2":
                rep = input("Terminé ? (y/n) : ")
                task["done"] = rep == "y"

            elif choix_modif == "3":
                task["date_creation"] = input("Nouvelle date de création : ")

            elif choix_modif == "4":
                task["deadline"] = input("Nouvelle deadline : ")

            elif choix_modif == "5":
                task["rappel"] = int(input("Nouveau rappel (minutes) : "))

            else:
                print("Choix invalide.")

        else:
            print("Task inexistante.")

    elif choix == "Quit":
        running = False
