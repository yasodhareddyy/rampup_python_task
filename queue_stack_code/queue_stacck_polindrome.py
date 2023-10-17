class PalindromeChecker:
    def __init__(self):
        self.queue = []
        self.stack = []

    def enqueueCharacter(self, char):
        self.queue.append(char)

    def dequeueCharacter(self):
        return self.queue.pop(0)

    def pushCharacter(self, char):
        self.stack.append(char)

    def popCharacter(self):
        return self.stack.pop()

def is_palindrome(word):
    checker = PalindromeChecker()

    for char in word:
        checker.enqueueCharacter(char)
        checker.pushCharacter(char)

    is_palindrome = True
    while len(checker.queue) > 0 and len(checker.stack) > 0:
        if checker.dequeueCharacter() != checker.popCharacter():
            is_palindrome = False
            break

    return is_palindrome

# Sample input
input_string = "madam"

if is_palindrome(input_string):
    print("The word, " + input_string + ", is a palindrome.")
else:
    print("The word, " + input_string + ", is not a palindrome.")
