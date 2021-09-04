num_card = input('введите номер карты')

def credit(num):
    return num

print(credit(num_card))

def palindrom(s):

    if s[::1] == s[::-1]:
        return True
    else:
        return False

print(palindrom('шалаш'))

