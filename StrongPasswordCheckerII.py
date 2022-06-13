"""
A password is said to be strong if it satisfies all the following criteria:
    - It has at least 8 characters.
    - It contains at least one lowercase letter.
    - It contains at least one uppercase letter.
    - It contains at least one digit.
    - It contains at least one special character. The special characters are the characters in the following string: "!@#$%^&*()-+".
    - It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).

Given a string password, return true if it is a strong password. Otherwise, return false.
"""

class StrongPasswordCheckerII(object):
    def strongPasswordCheckerII(self, password):
        if len(password) < 8:
            return False
        lowercase = False
        uppercase = False
        digit = False
        special = False
        special_chars = {'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+'}
        last_char = ''
        for i in password:
            if i == last_char:
                return False
            if ord(i) >= ord('a') and ord(i) <= ord('z'):
                lowercase = True
            elif ord(i) >= ord('A') and ord(i) <= ord('Z'):
                uppercase = True
            elif ord(i) >= ord('0') and ord(i) <= ord('9'):
                digit = True
            elif i in special_chars:
                special = True
            last_char = i
        return lowercase and uppercase and digit and special
            
        