"""
You are given the strings key and message, which represent a cipher key and a secret message, respectively. The steps to decode message are as follows:
    - Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
    - Align the substitution table with the regular English alphabet.
    - Each letter in message is then substituted using the table.
    - Spaces ' ' are transformed to themselves.

For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet), we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 
'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').

Return the decoded message.
"""

class DecodeTheMessage(object):
    def decodeMessage(self, key, message):
        index = 0
        positions = {}
        for i in key:
            if i not in positions and i != ' ':
                positions[i] = index
                index += 1
        ans = []
        for i in message:
            if i != ' ':
                ans.append(chr(ord('a') + positions[i]))
            else:
                ans.append(' ')
        return ''.join(ans)
        