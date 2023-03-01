from PrintData import *
from Note import *
import os
import datetime
os.system('cls')


def inputData(notes):
    idarg = len(notes)
    title = input("Заголовок: ")
    body = input("Текст заметки: ")
    now = datetime.datetime.now()
    return [title, body, now.strftime("%d-%m-%Y %H:%M"), idarg]


def addNote(notes):
    noteinfo = inputData(notes)
    return Note(noteinfo[0], noteinfo[1], noteinfo[2], noteinfo[3])



def editNote(notes):
    if (len(notes) > 0):
        index = input("Введите ID заметки для изменения: ")
        try:
            i = int(index)
            if (i < len(notes)):
                notes[i] = addNote(notes)
                print("Заметка отредактирована!")
            else:
                print(
                    "Неверный ввод!")
        except ValueError:
            print("Неверный ввод, введите число!")
    else:
        print("Нет заметок!")


def deleteNote(notes):
    if (len(notes) > 0):
        index = input("Введите Id для удаления: ")
        try:
            i = int(index)
            if (i < len(notes)):
                notes.pop(i)
                print("Заметка удалена!")
            else:
                print(
                    "Неверный ввод!")
        except ValueError:
            print("Неверный ввод, введите число!")
    else:
        print("Нет заметок!")


def main():
    notes = []
    done = False
    while (done == False):
        print("Мои заметки--\n\
        Выберете команду:\n\
        1 - Добавить заметку;\n\
        2 - Смотреть все заметки;\n\
        3 - Редактировать заметку;\n\
        4 - Удалить заметку;\n\
        0 - Выход.")
        command = input("Введите команду: ")
        match command:
            case "1":
                notes.append(addNote(notes))
                print("Заметка добавлена!")
            case "2":
                printAllData(notes)
            case "3":
                editNote(notes)
            case "4":
                deleteNote(notes)
            case "0":
                print("До встречи!")
                done = True
            case _:
                print("Неправильный ввод")
