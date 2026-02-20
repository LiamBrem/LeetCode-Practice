class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for val in tokens:
            if isOperator(val):
                num1 = stack.pop()
                num2 = stack.pop()
                
                new = operate(num1, num2, val) 

                stack.append(new)

            else:
                stack.append(int(val))


        return stack[0]

def operate(num1, num2, op):
    if op == "*":
        return num2 * num1
    elif op == "/":
        return int(num2/num1)
    elif op == "-":
        return num2 - num1
    else:
        return num2 + num1

def isOperator(s):
    if s in {"+", "*", "/", "-"}:
        return True
        