import operations
import note
import ui

number = 6  # сколько знаков МИНИМУМ может быть в тексте заметки


def add():
    note = ui.create_note(number)
    array = operations.read_file()
    for notes in array:
        if note.note.get_id(note) == note.note.get_id(notes):
            note.note.set_id(note)
    array.append(note)
    operations.write_file(array, 'a')
    print('Заметка добавлена...')


def show(text):
    logic = True
    array = operations.read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(note.note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + note.note.get_id(notes))
        if text == 'date':
            logic = False
            if date in note.note.get_date(notes):
                print(note.note.map_note(notes))
    if logic == True:
        print('Нет ни одной заметки...')


def id_edit_del_show(text):
    id = input('Введите id необходимой заметки: ')
    array = file_operation.read_file()
    logic = True
    for notes in array:
        if id == note.note.get_id(notes):
            logic = False
            if text == 'edit':
                note = ui.create_note(number)
                note.note.set_title(notes, note.get_title())
                note.note.set_body(notes, note.get_body())
                note.note.set_date(notes)
                print('Заметка изменена...')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена...')
            if text == 'show':
                print(note.note.map_note(notes))
    if logic == True:
        print('Такой заметки нет, возможно, вы ввели неверный id')
    file_operation.write_file(array, 'a')
