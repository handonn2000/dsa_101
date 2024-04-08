class RPN:
    def __init__(self, expression: str) -> None:
        self.expression = expression.replace(" ", "")

    def generatePostFix(self) -> list[str]:
        precedence = {
            "-": 0,
            "+": 1,
            "/": 2,
            "*": 3 
        }
        out = []
        stack = []

        for char in self.expression:
            if char.isdigit():
                out.append(char)
                continue

            if char in "+-*/":
                if stack and precedence[char] < precedence[stack[-1]]:
                    out.append(stack.pop())
                stack.append(char)
        
        while stack:
            out.append(stack.pop())
        
        return out
    
    def calculateExpression(self) -> int:
        post_fix = self.generatePostFix()

        stack = []
        for char in post_fix:
            if char.isdigit():
                stack.append(char)
                continue

            if stack and char in "+-*/":
                d1 = float(stack.pop())
                d2 = float(stack.pop())
                if char == "+":
                    stack.append(d2 + d1)
                if char == "-":
                    stack.append(d2 - d1)
                if char == "*":
                    stack.append(d2 * d1)
                if char == "/":
                    stack.append(d2/d1)

        print(stack)
        return 0
    
    def calculate(self, operand1: str, operand2: str, operator: str):
        d1 = float(operand1)
        d2 = float(operand2)
        if operator == "+":
            return d2 + d1
        if operator == "-":
            return d2 - d1
        if operator == "*":
            return d2 * d1
        if operator == "/":
            return d2 / d1

    def getResult(self):
        stack = []
        
        for char in self.expression:
            if char in "+-*/":
                stack.append(char)

            if char.isdigit():
                if not stack:
                    stack.append(char)
                elif stack and stack[-1] in "+-":
                    stack.append(char)
                elif stack and stack[-1] in "*/":
                    operator = stack.pop()
                    operand = stack.pop()
                    res = self.calculate(char, operand, operator)
                    stack.append(str(res))

        res = float(stack[0])
        for pos in range(1, len(stack), 2):
            operator = stack[pos]
            operand2 = float(stack[pos + 1])
            res = self.calculate(operand2, res, operator)
       
        return res

rpn = RPN("2 + 1 *3")
print(rpn.getResult())