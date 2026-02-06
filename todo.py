from datetime import datetime
from functions import add_task, show_tasks, modify_task

today = datetime.today()

tasks = [
    {
        "title": "Buy groceries",
        "done": False,
        "date_creation": "2026-01-20",
        "deadline": "2026-02-07",
        "rappel": 60,
    }
]

running = True

for task in tasks:
    deadline_date = datetime.strptime(task["deadline"], "%Y-%m-%d")
    jours_restants = (deadline_date - today).days

    if jours_restants >= 0:
        print(
            f"🔔 Rappel : '{task['title']}' → "
            f"{jours_restants} jour(s) restant(s) avant la deadline"
        )
    else:
        print(
            f"⚠️  Deadline dépassée pour '{task['title']}' "
            f"({abs(jours_restants)} jour(s) de retard)"
        )

while running:
    print("What do you want to do?\n")
    choix = input("Add / Show / Modify / Quit")

    if choix == "Add":
        add_task(tasks)

    elif choix == "Show":
        show_tasks(tasks)

    elif choix == "Modify":
        modify_task(tasks)

    elif choix == "Quit":
        running = False
