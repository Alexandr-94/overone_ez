num_card = ('1234 6321 4563 9654' ).split()
def credit():
    num_len = 0
    new_num = ''
    for i in num_card:
        num_len += 1
        if num_len != 4:
            new_num += '**** '
        else:
            new_num += i
    print(new_num)
credit()



def palindrom(s):

    if s[::1] == s[::-1]:
        return True
    else:
        return False

print(palindrom('шалаш'))

