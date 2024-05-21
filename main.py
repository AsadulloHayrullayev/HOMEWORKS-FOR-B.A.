                         #Homework
class A :
    def add(self,a,b):
        return a + b
    def minus(self,a,b):
        return a - b
    def mult(self,a,b):
        return a * b
    def div(self,a,b):
        return a/b

    @staticmethod
    def frst(self,a,b):
        return a+b
    @staticmethod
    def nqr(a,b):
       return a**b
cal = A()

def input_ask():
    x = int(input('ur first number : '))
    y = int(input('ur second number : '))
    return x,y
symbol = input(" choose (+ - / * # & **)")

if symbol in ['+','-','*','/','&','**']:
    num1,num2 = input_ask()

    # if symbol == '+':
    #     num1,num2 = input_ask()
    if symbol == '+':
        print("Result : ", cal.add(num1,num2))
    # if symbol== '-':
    #     num1,num2 = input_ask()
    if symbol == '-':
        print("Result : ", cal.minus(num1,num2))
    # if symbol== '*':
    #     num1,num2 = input_ask()
    if symbol == '*':
        print("Result : ", cal.mult(num1,num2))
    # if symbol== '/':
    #     num1,num2 = input_ask()
    if symbol == '/':
        print("Result : ", cal.div(num1,num2))
    if symbol == '**':
        zza = input("nigga pay $50 first , will you pay? ")
        if zza == 'yes':
            dda = input('confirm ur payment : ' )
            if dda >= '50':
                print('thank you there is ur result : ', cal.nqr(num1,num2))
    if symbol == '&':
        print(input('nigga pay $120 first'))


