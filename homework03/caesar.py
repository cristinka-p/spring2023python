import typing as tp

en_abc = 'abcdefghijklmnopqrstuvwxyzabc'
en_ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABC'
ru_abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабв'
ru_Abc = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВ'
def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    if plaintext.islower():
        for i in plaintext:
            a = en_abc.index('i')
            ciphertext = + en_abc[a+3]
    if plaintext.isupper():
        for i in plaintext:
            a = en_ABC.index('i')
            ciphertext = + en_ABC[a+3]
    print ciphertext
    return ciphertext

    #word = 'apple'
    #print(encrypt_caesar(word))


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    # PUT YOUR CODE HERE
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
