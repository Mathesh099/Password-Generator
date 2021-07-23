import random
class PasswordGenerator:

    def __init__(self):
        self.CharsLower = 'abcdefghijklmnopqrstuvwxyz'
        self.CharsUpper = self.CharsLower.upper()
        self.SpecialChars = '!@#$%^&*()_+'
        self.Nums = str(1234567890)
        self.Length = int(input("Enter the Password's Length: "))
        self.Password = ""

    def password_generator(self):
        while len(self.Password) < self.Length:
            if len(self.Password) < self.Length:
                self.Password += random.choice(self.CharsUpper)
            if len(self.Password) < self.Length:
                self.Password += random.choice(self.CharsLower)
            if len(self.Password) < self.Length:
                self.Password += random.choice(self.SpecialChars)
            if len(self.Password) < self.Length:
                self.Password += random.choice(self.Nums)
        print(self.Password)

    def main(self):
        self.password_generator()

if __name__ == '__main__':
    app = PasswordGenerator()
    app.main()

