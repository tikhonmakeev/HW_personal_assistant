import json
import csv
from datetime import datetime

import json
import csv
from datetime import datetime


class Note:
    def __init__(self, id: int, title: str, content: str, timestamp: str):
        self.id = id
        self.title = title
        self.content = content
        self.timestamp = timestamp

    @staticmethod
    def menu():
        while True:
            print("Управление заметками:")
            print("1. Создать заметку")
            print("2. Просмотреть заметки")
            print("3. Просмотреть подробности заметки")
            print("4. Редактировать заметку")
            print("5. Удалить заметку")
            print("6. Назад")

            choice = input("Введите номер действия: ")

            if choice == '1':
                title = input("Введите заголовок заметки: ")
                content = input("Введите содержимое заметки: ")
                Note.create_note(title, content)
            elif choice == '2':
                Note.list_notes()
            elif choice == '3':
                note_id = int(input("Введите ID заметки: "))
                Note.view_note(note_id)
            elif choice == '4':
                note_id = int(input("Введите ID заметки для редактирования: "))
                new_title = input("Введите новый заголовок: ")
                new_content = input("Введите новое содержимое: ")
                Note.edit_note(note_id, new_title, new_content)
            elif choice == '5':
                note_id = int(input("Введите ID заметки для удаления: "))
                Note.delete_note(note_id)
            elif choice == '6':
                break
            else:
                print("Неверный выбор, попробуйте снова.")

    @staticmethod
    def load_notes():
        """Загружает список заметок из файла"""
        try:
            with open('notes.json', 'r') as file:
                notes = json.load(file)
            return notes
        except FileNotFoundError:
            return []

    @staticmethod
    def save_notes(notes):
        """Сохраняет список заметок в файл"""
        with open('notes.json', 'w') as file:
            json.dump(notes, file, indent=4)

    @staticmethod
    def create_note(title: str, content: str):
        """Создает заметку и добавляет её в список"""
        timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        notes = Note.load_notes()
        new_id = len(notes) + 1
        note = Note(new_id, title, content, timestamp)
        notes.append(note.__dict__)  # сохраняем как словарь
        Note.save_notes(notes)

    @staticmethod
    def list_notes():
        """Выводит список всех заметок"""
        notes = Note.load_notes()
        for note in notes:
            print(f"""ID: {note['id']}, Title: {
                  note['title']}, Timestamp: {note['timestamp']}""")

    @staticmethod
    def view_note(id: int):
        """Просмотр содержимого заметки по id"""
        notes = Note.load_notes()
        for note in notes:
            if note['id'] == id:
                print(f"""Title: {note['title']}\nContent: {
                      note['content']}\nTimestamp: {note['timestamp']}""")

    @staticmethod
    def edit_note(id: int, new_title: str, new_content: str):
        """Редактирование заметки"""
        notes = Note.load_notes()
        for note in notes:
            if note['id'] == id:
                note['title'] = new_title
                note['content'] = new_content
                note['timestamp'] = datetime.now().strftime(
                    '%d-%m-%Y %H:%M:%S')
        Note.save_notes(notes)

    @staticmethod
    def delete_note(id: int):
        """Удаление заметки по id"""
        notes = Note.load_notes()
        notes = [note for note in notes if note['id'] != id]
        Note.save_notes(notes)

    @staticmethod
    def import_notes_from_csv(filename: str):
        """Импортирует заметки из csv"""
        notes = Note.load_notes()
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                new_note = Note(int(row['id']), row['title'],
                                row['content'], row['timestamp'])
                notes.append(new_note.__dict__)
        Note.save_notes(notes)

    @staticmethod
    def export_notes_to_csv(filename: str):
        """Экспортирует заметки в csv."""
        notes = Note.load_notes()
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(
                file, fieldnames=['id', 'title', 'content', 'timestamp'])
            writer.writeheader()
            for note in notes:
                writer.writerow(note)


class Task:
    def __init__(self, id: int, title: str, description: str, done: bool, priority: str, due_date: str):
        self.id = id
        self.title = title
        self.description = description
        self.done = done
        self.priority = priority
        self.due_date = due_date

    @staticmethod
    def menu():
        pass


class Contact:
    def __init__(self, id: int, name: str, phone: str, email: str):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email

    @staticmethod
    def menu():
        pass


class FinanceRecord:
    def __init__(self, id: int, amount: float, category: str, date: str, description: str):
        self.id = id
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    @staticmethod
    def menu():
        pass


def calculator():
    while True:
        print("\nКалькулятор:")
        print("Введите арифметическое выражение или 'q' для выхода.")
        expression = input("Введите выражение: ")

        if expression.lower() == 'q':
            break

        try:
            result = eval(expression)
            print(f"Результат: {result}")
        except Exception as e:
            print(f"Ошибка: {e}")


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


if __name__ == "__main__":
    main_menu()
