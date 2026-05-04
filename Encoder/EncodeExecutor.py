from VARS_DECLARATION import *
from FILES_DECLARATION import FILES_TABLE

from pathlib import Path
from bin.Logger.ConsolLogger import setLogger

logger = setLogger("Encoder logger")


class Executor:
    def __init__(self, path: Path):
        self.path = path

    def run(self, **kwargs):
        # Алгоритм:
        # 1. Получаем список директорий и файлов
        # 2. Поочерёдно открываем файлы
        # 3. Меняем названия переменных по таблице ассоциаций
        # 4. Если переменные объявляются в группе, объединяем их в одну строку
        # 5. Условные операторы с одной строкой так же объединяем в одну строку
        # 6. Шифруем название файла по таблице ассоциаций
        for p in self.path.iterdir():
            if p.is_dir():
                ...

    def rename_files_in_dir(self, path: Path):
        if path.is_file():
            obj = FILES_TABLE.get_file_by_origin(path.name)
            if obj:
                try:
                    new_path = path.with_name(obj.get_encoded())
                    path.rename(new_path)
                    logger.log("File renamed: [%s] => [%s]", obj.get_origin(), new_path)
                except Exception as e:
                    logger.error("Failed to rename: [%s] => [%s]\n(%s)", obj.get_origin(), new_path, e)
        elif path.is_dir():
            for file in path.iterdir():
                self.rename_files_in_dir(file)

    def encrypt_file(self, file: Path, context: VARS_CONTEXT):
        if not file.is_file():
            return file
        
        for v_enc in context:
            content = file.read_text(encoding='utf-8')
            replacment = content.replace(v_enc.value.get('origin'), v_enc.value.get('encoded'))
            file.write_text(replacment, encoding='utf-8')

    def complicate_file(self, file: Path):
        if not file.is_file():
            return file
        
        lines = file.read_text().splitlines()
        spaces = [i for i in range(lines) if lines[i].isspace() or lines[i] == ""]

        
