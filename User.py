class User:
    def __init__(self):
        self.id_usuario = 0
        self.nome = ""
        self.password = ""

    def validate(self):
        if self.password == "qwer" and self.nome == "gabriel":
            return True
        return False
