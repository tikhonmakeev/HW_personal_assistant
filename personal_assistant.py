class Note:
    def __init__(self, id: int, title: str, content: str, timestamp: str):
        self.id = id
        self.title = title
        self.content = content
        self.timestamp = timestamp

    @staticmethod
    def menu(self):
        pass


class Task:
    def __init__(self, id: int, title: str, description: str, done: bool, priority: str, due_date: str):
        self.id = id
        self.title = title
        self.description = description
        self.done = done
        self.priority = priority
        self.due_date = due_date

    @staticmethod
    def menu(self):
        pass


class Contact:
    def __init__(self, id: int, name: str, phone: str, email: str):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email

    @staticmethod
    def menu(self):
        pass


class FinanceRecord:
    def __init__(self, id: int, amount: float, category: str, date: str, description: str):
        self.id = id
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    @staticmethod
    def menu(self):
        pass


def calculator():
    pass


def main_menu():
    while True:
        print("Добро пожаловать в Персональный помощник!")
        print("Выберите действие:")
        print("1. Управление заметками")
        print("2. Управление задачами")
        print("3. Управление контактами")
        print("4. Управление финансовыми записями")
        print("5. Калькулятор")
        print("6. Выход")

        choice = input("Введите номер действия: ")

        if choice == '1':
            Note.menu()
        elif choice == '2':
            Task.menu()
        elif choice == '3':
            Contact.menu()
        elif choice == '4':
            FinanceRecord.menu()
        elif choice == '5':
            calculator()
        elif choice == '6':
            print("Завершил работу")
            break
        else:
            print("Неверный выбор, попробуйте снова.")


main_menu()
