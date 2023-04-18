"""Task 1
Створіть клас Editor, який містить методи view_document та edit_document.
Нехай метод edit_document виводить на екран інформацію про те, що редагування
документів недоступне для безкоштовної версії. Створіть підклас ProEditor,
у якому цей метод буде перевизначено. Введіть ліцензійний ключ із клавіатури і,
якщо він коректний, створіть екземпляр класу ProEditor, інакше Editor.
Викликайте методи перегляду та редагування документів.
"""


class Editor:

    @staticmethod
    def view_document(name):
        print(f"Viewing of the document {name}")

    def edit_document(self, name):
        print(f"Document editing isn't available in the free version")


class ProEditor(Editor):

    def edit_document(self, name):
        print(f"Editing of the document {name}")


class FullEditor(Editor):

    def __init__(self):
        self.__key = '123'

    def edit_document(self, name):
        entered_key = input("Enter the license key: ")
        editor = ProEditor() if entered_key == self.__key else Editor()
        editor.edit_document(name)


# test
doc = FullEditor()
doc.view_document('my_doc')
print()
doc.edit_document('my_doc')
