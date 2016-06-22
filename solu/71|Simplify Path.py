class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        paths = path.split('/')[1:]
        stack = ['']
        for p in paths:
            if p == '.' or p == '':
                continue
            elif p == '..' and len(stack):
                if stack[-1] != '':
                    stack.pop()
            else:
                stack.append(p)
        if len(stack) == 1:
            return '/'
        else:
            return '/'.join(stack)