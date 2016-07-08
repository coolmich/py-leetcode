class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack, res, priority, i = [], [], {'+':0, '-':0, '*':1, '/':1}, 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            elif s[i].isdigit():
                buff = []
                while i < len(s) and s[i].isdigit():
                    buff.append(s[i])
                    i += 1
                res.append(int(''.join(buff)))
            else:
                while len(stack) and priority[stack[-1]] >= priority[s[i]]:
                    res.append(stack.pop())
                stack.append(s[i])
                i += 1
        while len(stack): res.append(stack.pop())

        eval = []
        for item in res:
            if isinstance(item, int):
                eval.append(item)
            else:
                num1 = eval.pop()
                num2 = eval.pop()
                if item == '+': num = num1+num2
                elif item == '-': num = num2 - num1
                elif item == '*': num = num1*num2
                else: num = num2/num1
                eval.append(num)
        return eval.pop()

