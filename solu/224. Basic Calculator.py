class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def getdigit(s, i):
            ret = []
            while i < len(s) and s[i].isdigit():
                ret.append(s[i])
                i += 1
            return i, int(''.join(ret))
        def helper(s, idx):
            res, op = 0, '+'
            while idx < len(s):
                if s[idx] == ' ': idx += 1
                elif s[idx].isdigit():
                    idx, d = getdigit(s, idx)
                    res = (res + d) if op == '+' else (res - d)
                elif s[idx] == '(':
                    idx, d = helper(s, idx+1)
                    res = (res + d) if op == '+' else (res - d)
                elif s[idx] == ')': return idx + 1, res
                else: op, idx = s[idx], idx+1
            return len(s), res
        _, res = helper(s, 0)
        return res

        # stack1, stack2, i = [], [], 0
        # while i < len(s):
        #     l = s[i]
        #     if l == ' ':
        #         i += 1
        #     elif l.isdigit():
        #         i, d = getdigit(s, i)
        #         stack1.append(d)
        #     elif l in ('(', ')'):
        #         if l == '(': stack2.append('(')
        #         else:
        #             while stack2:
        #                 t = stack2.pop()
        #                 if t == '(': break
        #                 stack1.append(t)
        #         i += 1
        #     else:
        #         while stack2 and stack2[-1] != '(': stack1.append(stack2.pop())
        #         stack2.append(l)
        #         i += 1
        # while stack2: stack1.append(stack2.pop())
        # for l in stack1:
        #     if isinstance(l, int): stack2.append(l)
        #     else:
        #         n1 = stack2.pop()
        #         n2 = stack2.pop()
        #         if l == '+':
        #             stack2.append(n1+n2)
        #         else:
        #             stack2.append(n2-n1)
        # return stack2.pop()
