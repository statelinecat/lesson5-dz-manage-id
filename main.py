class User:
    def __init__(self, id, name, access_level='user'):
        self.__id = id
        self.__name = name
        self.__access_level = access_level

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_name(self, name):
        self.__name = name

    def set_access_level(self, access_level):
        self.__access_level = access_level

class Admin(User):
    def __init__(self, id, name, access_level='admin'):
        super().__init__(id, name, access_level)
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user_id):
        for user in self.users:
            if user.get_id() == user_id:
                self.users.remove(user)
                break
        else:
            print("Пользователь с таким ID не найден.")
