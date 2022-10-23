def isPalindrome(word):
    return print("Es palindromo") if word[::-1] == word[::] else print("No es palindromo")

def run():
    word = (input("Ingresa la palabra: ")).lower()
    isPalindrome(word.replace(" ", ""))

if __name__ == '__main__':
    run()