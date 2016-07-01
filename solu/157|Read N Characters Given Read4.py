# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        buffer, read_bytes = [''] * 4, 0
        for i in xrange(n / 4 + 1):
            size = read4(buffer)
            if size:
                buf[read_bytes:read_bytes+size] = buffer
                read_bytes += size
            else:
                break
        return min(read_bytes, n)
        