class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def traverse(s, idx, curs, balance, res, l_rm, r_rm):
            if idx == len(s):
                if balance == 0: res.append(curs)
                return
            if s[idx] == '(':
                traverse(s, idx+1, curs+'(', balance+1, res, l_rm, r_rm)
                if l_rm:
                    traverse(s, idx+1, curs, balance, res, l_rm-1, r_rm)
            elif s[idx] == ')':
                if balance > 0:
                    traverse(s, idx+1, curs+')', balance-1, res, l_rm, r_rm)
                if r_rm:
                    traverse(s, idx+1, curs, balance, res, l_rm, r_rm-1)
            else:
                traverse(s, idx+1, curs+s[idx], balance, res, l_rm, r_rm)
        stack, l_rm, r_rm = [], 0, 0
        for l in s:
            if l == '(': stack.append(l)
            elif l == ')':
                if stack and stack[-1] == '(': stack.pop()
                else: stack.append(l)
        for l in stack:
            if l == '(': l_rm += 1
            else: r_rm += 1
        if not len(stack): return [s]
        if len(s) == len(stack): return ['']
        res = []
        traverse(s, 0, '', 0, res, l_rm, r_rm)
        return list(set(res))
        