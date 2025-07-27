from abc import ABC,abstractmethod

class Ab(ABC):
    @abstractmethod
    def getusername(self):
        pass
    @abstractmethod
    def getBalance(self):
        pass
    @abstractmethod
    def setBalance(self,balance):
        pass
    @abstractmethod
    def getEmailId(self):
        pass
    @abstractmethod
    def getPassword(self):
        pass

class User(Ab):
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password
        self.balance = 0

    def getusername(self):
        return self.name
    def getEmailId(self):
        return self.email
    def getPassword(self):
        return self.password
    def setBalance(self, balance):
        self.balance = balance
    def getBalance(self):
        return self.balance
    def setusername(self,name):
        self.name = name


class Transaction(Ab):
    def Checkpassowrd(self):
        pass
    def Createnewuser(self):
        pass
    def deposit(self):
        pass
    def withdraw(self):
        pass

class Bank(Transaction):
    def __init__(self):
        pass
    

