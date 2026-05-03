from enum import Enum

class DIRECTORY_TABLE(Enum):
    ENCODER = {'origin': "Encoder", 'encoded': "_ENCDATMNG"}
    MANAGERS = {'origin': "Managers", 'encoded': "_MNGCACHE"}
    BIN = {'origin': "bin", 'encoded': "_BINCACHEDDATA"}

    def get_encoded(self):
        return self.value['encoded']
    
    def get_origin(self):
        return self.value['origin']
    
    @staticmethod
    def get_file_by_origin(origin: str):
        for member in DIRECTORY_TABLE:
            if member.value.get('origin') == origin:
                return member
            
        return None
    
    @staticmethod
    def get_file_by_encrypt(encrypt: str):
        for member in DIRECTORY_TABLE:
            if member.value.get('encrypt') == encrypt:
                return member
            
        return None


class FILES_TABLE(Enum):
    ENCODE_EXECUTOR = {'origin': "EncodeExecutor.py", 'encoded': "OPERMAINENC.py"}
    VARS_DECLARATION = {'origin': "VARS_DECLARATION.py", 'encoded': "_OPERVARSCNSTTLST.py"}
    FILES_DECLARATION = {'origin': "FILES_DECLARATION.py", 'encoded': "_OPERFLSCNSTTLST.py"}
    MAIN = {'origin': "main.py", 'encoded': "_exec.py"}
    

    def get_encoded(self):
        return self.value['encoded']
    
    def get_origin(self):
        return self.value['origin']
    
    @staticmethod
    def get_file_by_origin(origin: str):
        for member in FILES_TABLE:
            if member.value.get('origin') == origin:
                return member
            
        return None
    
    @staticmethod
    def get_file_by_encrypt(encrypt: str):
        for member in FILES_TABLE:
            if member.value.get('encrypt') == encrypt:
                return member
            
        return None