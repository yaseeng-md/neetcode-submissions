from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            # check token is integer
            if token not in ["+", "-", "*", "/"]:
                # print(f"token is integer: {token}")
                stack.append(int(token))
            # if not interger, then it is an operator
            else:
                # print(f"token is operator: {token}")
                # print("stack before operation: ", stack)
                first_ele = stack.pop()
                second_ele = stack.pop()
                if token == "+":
                    # print(f"first_ele: {first_ele} +  second_ele: {second_ele}")
                    stack.append(second_ele + first_ele)
                elif token == "-":
                    # print(f"first_ele: {first_ele} -  second_ele: {second_ele}")
                    stack.append(second_ele - first_ele)
                elif token == "*":
                    # print(f"first_ele: {first_ele} *  second_ele: {second_ele}")    
                    stack.append(second_ele * first_ele)
                elif token == "/":
                    # print(f"first_ele: {first_ele} /  second_ele: {second_ele}")
                    stack.append(int(second_ele / first_ele))
        print(stack)
        return stack.pop()
