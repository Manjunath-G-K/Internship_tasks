# Task 5: Task Manager with File I/O
# Student: Manjunath G K
# Date: 11/09/2025

class Task:
    def __init__(self, task_id, title, desc):
        self.task_id = task_id
        self.title = title
        self.desc = desc

    def __str__(self):
        return f"{self.task_id}. {self.title} - {self.desc}"


class TaskManager:
    def __init__(self, filename="tasks.txt"):
        self.tasks = []
        self.filename = filename
        self.next_id = 1
        self.load()

    def save(self):
        f = open(self.filename, "w")
        for t in self.tasks:
            f.write(f"  {t.task_id}  | {t.title} | {t.desc}\n")
        f.close()

    def load(self):
        f = open(self.filename, "r")
        for line in f:
            tid, title, desc = line.strip().split("|")
            self.tasks.append(Task(int(tid), title, desc))
        f.close()
        if self.tasks:
            self.next_id = max(t.task_id for t in self.tasks) + 1

    def create_task(self, title, desc):
        t = Task(self.next_id, title, desc)
        self.tasks.append(t)
        self.next_id += 1
        self.save()
        print("Task added!")

    def read_tasks(self):
        if not self.tasks:
            print("No tasks found")
        else:
            for t in self.tasks:
                print(t)

    def update_task(self, tid, new_title, new_desc):
        for t in self.tasks:
            if t.task_id == tid:
                t.title = new_title
                t.desc = new_desc
                self.save()
                print("Task updated")
                return
        print("Task not found")

    def delete_task(self, tid):
        for t in self.tasks:
            if t.task_id == tid:
                self.tasks.remove(t)
                self.save()
                print("Task deleted")
                return
        print("Task not found")


def main():
    m = TaskManager()
    while True:
        print("\n 1.Create  2.View  3.Update  4.Delete  5.Exit")
        ch = input("Enter choice: ")

        if ch == "1":
            title = input("Title: ")
            desc = input("Description: ")
            m.create_task(title, desc)
        elif ch == "2":
            m.read_tasks()
        elif ch == "3":
            tid = int(input("Enter your task id: "))
            title = input("New title: ")
            desc = input("New description: ")
            m.update_task(tid, title, desc)
        elif ch == "4":
            tid = int(input("Enter task id: "))
            m.delete_task(tid)
        elif ch == "5":
            exit(0)
        else:
            print("Wrong choice!")


if __name__ == "__main__":
    main()
