Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
class Solution:
    def reverse(self, x: int) -> int:
        s = str(abs(x))
        newvalue = int(s[::-1])
        if newvalue > 2**31 - 1:
            return 0
        return newvalue if x > 0 else newvalue*-1
