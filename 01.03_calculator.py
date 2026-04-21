# 5단계: try-except를 이용한 견고한 코드 만들기

def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

def print_res(n1, n2, op, func):
    print(f"{n1} {op} {n2} = {func(n1, n2)}")

def calculator():
    fnc = {'+': add, '-':sub, '*': mul, '/': div}
    """로봇 SW 개발 입문용 계산기 메인 함수"""
    try:
        while True:
            op = input("operate(+,-,*,/), exit('q'): ")
            if op.lower() == 'q':
                print('exit')
                break

            if op not in fnc:
                print("Known operate")
                continue
            
            num1 = float(input("num1: "))
            num2 = float(input("num2: "))
            print_res(num1, num2, op, fnc[op])
    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    calculator()