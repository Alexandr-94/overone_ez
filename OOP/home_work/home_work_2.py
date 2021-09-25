import string


class Alphabet:
    def __init__(self, leng, letters):
        self.leng = leng
        self.letters = letters
    def out(self):
        self.alf = []
        for i in self.letters:
            if i.isalpha():
                self.alf.append(i)
        print(self.letters)
    def num(self):
        print(len(self.alf))


class EngAlphabet(Alphabet):
    def __init__(self, En, letters_str):
        super().__init__(self, En)
        self.En = En
        self.str_one = letters_str


    @staticmethod
    def __letters_num():
        print(len(al_two.letters_str()))

    def is_en_letter(self):
        for i in test_letters:
            if i in self.str_one:
                print(i, 'буква из английского алфавита')
            else:
                print(i, 'буква не из английского алфавита')

    def num (self):
        print(al_two.__letters_num())

    @staticmethod
    def example():
        print('Hello World')



leng = ()
letters = ('а, б, в, г, д, е, ё, ж, з, и, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ъ, ы, ь, э, ю, я')

al = Alphabet(leng, letters)
al.out()
al.num()

letters_str = string.ascii_uppercase
test_letters = 'FЩ'
al_two = EngAlphabet(test_letters, letters_str)
al_two.is_en_letter()
al_two.example()
al_two.num()
print(len(letters_str))
