#                          ### HOMEWORK FOR LESSON 29
# class A :
#     def add(self,a,b):
#         return a + b
#     def minus(self,a,b):
#         return a - b
#     def mult(self,a,b):
#         return a * b
#     def div(self,a,b):
#         return a/b
#
#     @staticmethod
#     def frst(self,a,b):
#         return a+b
#     @staticmethod
#     def nqr(a,b):
#        return a**b
# cal = A()
#
# def input_ask():
#     x = int(input('ur first number : '))
#     y = int(input('ur second number : '))
#     return x,y
# symbol = input(" choose (+ - / * # & **)")
#
# if symbol in ['+','-','*','/','&','**']:
#     num1,num2 = input_ask()
#
#     # if symbol == '+':
#     #     num1,num2 = input_ask()
#     if symbol == '+':
#         print("Result : ", cal.add(num1,num2))
#     # if symbol== '-':
#     #     num1,num2 = input_ask()
#     if symbol == '-':
#         print("Result : ", cal.minus(num1,num2))
#     # if symbol== '*':
#     #     num1,num2 = input_ask()
#     if symbol == '*':
#         print("Result : ", cal.mult(num1,num2))
#     # if symbol== '/':
#     #     num1,num2 = input_ask()
#     if symbol == '/':
#         print("Result : ", cal.div(num1,num2))
#     if symbol == '**':
#         zza = input("nigga pay $50 first , will you pay? ")
#         if zza == 'yes':
#             dda = input('confirm ur payment : ' )
#             if dda >= '50':
#                 print('thank you there is ur result : ', cal.nqr(num1,num2))
#     if symbol == '&':
#         print(input('nigga pay $120 first'))







                            ### HOMEWORK FOR LESSON 30
# class SAlam:
#     def __init__(self):
#         self.salam = {}
#     def name_age(self,salam_id,name,age):
#         self.salam[salam_id] = 'name : ', name
#         self.salam[salam_id] += 'age : ', age
#     def pri(self,salam_id):
#         return self.salam[salam_id]
# class Bye(SAlam):
#     def __init__(self):
#         super().__init__()
#     def name_age(self,salam_id,data,surname,name,age):
#         SAlam.name_age(self,salam_id,name,age)
#         self.salam[salam_id] += "surname : ",surname,"data : ",data
#
# a = SAlam()
# a.name_age(1, "Jim", 12)
# print(a.pri(1))
#
# b = Bye()
# b.name_age(1,"22.09.2002","Carter","Jordan",77)
# print(b.pri(1))

                        ### HOMEWORK FOR LESSON 31
# class BankAccStatus:
#     def __init__(self):
#         self.balance = 1
#         self.__all_balance = {}
#
#     def deposit(self, __number_acc, amount):
#         self.__all_balance[__number_acc] = amount + self.balance
#         self.balance += amount
#
#     def withdraw(self, __number_acc, amount):
#         self.__all_balance[__number_acc] = self.balance - amount
#         self.balance -= amount
#
#     def get_balance(self, __number_acc):
#         return f"Money You Got Now : {self.__all_balance[__number_acc]}"
#
#     def get_account_number(self, __number_acc):
#         return f"Account's Number : {__number_acc}"
#
#
# a = BankAccStatus()
# a.deposit(1, 121)
# a.withdraw(1, 21)
# print(a.get_account_number(1))
# print(a.get_balance(1))

                                   ### HOMEWORK FOR LESSON 32
def game():
    score = 0
    hello = input('Hello bro , we r gonna play a mini-game , are u ready?')
    num = input("GIMME word which is polindrom ")
    if num == num [::-1]:
            print("that was  polindrom")
            score =score +3
    else:
        score = score - 0.5
        print("not polindrom")
    print(f'Ur overall score is {score}')

    num2 = input("Bro again , give me one word , which should be polindrom ")
    if num2 == num2 [::-1]:
            print("that was  polindrom")
            score1 =score +3
    else:
        score1 = score - 0.5
        print("not polindrom")
    print(f'Ur overall score is {score1}')

    num3 = input("Bro again , give me one word , which should be polindrom ")
    if num3 == num3[::-1]:
        print("that was  polindrom")
        score2 = score1 + 3
    else:
        score2 = score1 - 0.5
        print("not polindrom")
    print(f'Ur overall score is {score2}')
game()