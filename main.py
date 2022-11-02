# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# Program make a simple calculator
import log
import calculate

debugLogger = log.getDebugLogger()
warnLogger = log.getWarnLogger()


def debugLog(message):
    debugLogger.debug(message)


def warnLog(message):
    warnLogger.warning(message)


# constant
YES = "YES"
NO = "NO"


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = f'{num1} + {num2} = {calculate.add(num1, num2)}'
            print(result)
            debugLog(result)

        elif choice == '2':
            result = f'{num1} - {num2} = {calculate.subtract(num1, num2)}'
            print(result)
            debugLog(result)

        elif choice == '3':
            result = f'{num1} * {num2} = {calculate.multiply(num1, num2)}'
            print(result)
            debugLog(result)

        # can't divide by zero
        elif choice == '4':
            if num2 == 0:
                message = "warning: You can't divide by zero"
                print(message)
                warnLog(message)
                continue
            result = f'{num1} / {num2} = {calculate.divide(num1, num2)}'
            print(result)
            debugLog(result)

        # check if user wants another calculation
        # double-check for end
        # the while loop if answer is yes
        # available all types of yes/no
        while(True):
            next_calculation = input(
                "Let's do next calculation? (yes/no): ").upper()
            if next_calculation == YES:  # 계산을 계속 할 것이다 처음으로
                break
            elif next_calculation == NO:  # 계산을 그만 두겠다
                checkShutDown = input(  # 재확인
                    "Are you sure? (yes/no): ").upper()
                if checkShutDown == YES:  # 계산 최종 그만
                    exit()
                elif checkShutDown == NO:  # 계산 더 할거면 처음으로
                    break
            else:
                print("Please answer yes or no.")
                continue

    else:
        print("Invalid Input")
        warnLog("Invalid Input")
