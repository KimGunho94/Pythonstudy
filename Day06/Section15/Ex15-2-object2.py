'''파일명: Ex15-2-object2.py'''
class Calculator:

    def input_expr(self):
        expr = input('수식을 입력하세요 >> ')
        self.expr = expr

    def calculate(self):
        return eval(self.expr)

calc = Calculator()
calc.input_expr()
#또는 이런 방법
# result = calc.calculate()
# print('수식 결과는 {}입니다.'.format(result))
print('수식 결과는 {}입니다.'.format(calc.calculate()))
