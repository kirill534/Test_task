# теперь при попытке открыть несуществующий файл
# менеджер должен автоматически создавать и
# открывать этот файл в режиме записи;
# на выходе из менеджера должны подавaться
# все исключения, связанные с файлами.

class File:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.name, self.mode, encoding='UTF-8')
        except:
            self.file = open(self.file, 'w', encoding='UTF-8')

        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not exc_type:
            self.file.close()
        return True


with open('my_file1.txt', 'w') as file:
    file.write('Hello')
