class UserMail:

    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, new_mail):
        if new_mail.count("@") == 1 and new_mail.find("@") < new_mail.rfind("."):
            self.__email = new_mail
        else:
            print("Ошибочная почта")

    email = property(fget=get_email, fset=set_email)
    

k = UserMail('belosnezhka', 'prince@wait.you')
print(k.email)  # prince@wait.you
k.email = [1, 2, 3] # Ошибочная почта
k.email = 'prince@still@.wait'  # Ошибочная почта
k.email = 'prince@still.wait'
print(k.email)  # prince@still.wait

