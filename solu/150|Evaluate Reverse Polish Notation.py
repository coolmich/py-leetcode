class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack, i = [], 0
        while i < len(tokens):
            try:
                stack.append(int(tokens[i]))
            except:
                num2 = stack.pop()
                num1 = stack.pop()
                if tokens[i] == '+': num = num1 + num2
                elif tokens[i] == '-': num = num1 - num2
                elif tokens[i] == '*': num = num1 * num2
                else:
                    num = num1 / num2
                    if num < 0: num = -1 * (abs(num1)/abs(num2))
                stack.append(num)
            i += 1
        return stack.pop()