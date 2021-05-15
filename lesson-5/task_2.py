"""
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число
представляется как коллекция, элементы которой это цифры числа.

	Например, пользователь ввёл A2 и C4F.
	Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
	Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
	Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

# Уже увидел  решение с deque, поэтому решиил сделать "по-старинке" без коллекций, но с ООП.
# Код получился так-себе.
# Теперь уж почно запомню что можно collections использовать. :)
class HexNum:
    temp = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']


    def __init__(self, num_string):
        self.number = [i for i in num_string]

    def __add__(self, obj):
        foo = ''

        len1 = len(self.number)
        len2 = len(obj.number)

        if len1 > len2:
            j = 1
            carry = 0
            for i in range(1, len1 + 1):
                one = HexNum.temp.index(self.number[-i])
                if j <= len2:
                    two = HexNum.temp.index(obj.number[-j])
                else:
                    two = 0
                three = (one + two + carry) % 16
                carry = (one + two + carry)// 16
                foo = HexNum.temp[three] + foo
                j += 1
            if carry != 0:
                foo = HexNum.temp[carry] + foo
        else:
            j = 1
            carry = 0
            for i in range(1, len2 + 1):
                one = HexNum.temp.index(obj.number[-i])
                if j <= len1:
                    two = HexNum.temp.index(self.number[-j])
                else:
                    two = 0
                three = (one + two + carry) % 16
                carry = (one + two + carry)// 16
                foo = HexNum.temp[three] + foo
                j += 1
            if carry != 0:
                foo = HexNum.temp[carry] + foo

        return HexNum(foo)

# Произведение недоделано, хотел сделать через использование уже написаного метода суммы
    # def __mul__(self, obj):
    #     foo = HexNum('0')
	#
    #     len1 = len(self.number)
    #     len2 = len(obj.number)
	#
    #     carry = 0
    #     for i in range(1, len1 + 1):
    #         for j in range(1, len2 + 1):
    #             one = HexNum(self.number[-i] + '0'*i)
    #             two = HexNum(self.number[j])
	# 			times = HexNum.temp.index(obj.number[-j])
	#
    #         if carry != 0:
    #             foo = HexNum(HexNum.temp[three]) + foo
	#
    #     return foo

    def __str__(self):
        return str(self.number)

a = HexNum('A2')
b = HexNum('C4F')
c = a + b
d = HexNum('CFA4')
e = HexNum('AD45')
print(c)
print(d + e)
# d + e = 17CE9 - верно
