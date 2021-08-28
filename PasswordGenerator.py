import random
import csv
class PasswordGenerator:

    def __init__(self):
        self.CharsLower = "abcdefghijklmnopqrstuvwxyz"
        self.CharsUpper = self.CharsLower.upper()
        self.SpecialChars = "!@#$%^&*()_+"
        self.Nums = str(1234567890)
        self.Password = ""
        self.Run = True
        self.rows = []
        self.filename = "file.csv"

    def security_key(self):
        while self.Run:
            print("")
            self.SecurityKey = input("Enter the Security Key: ")
            print("=" * 50)
            if self.SecurityKey == "Enter":
                self.menu()
            else:
                print("Incorrect Password")
                continue

    def menu(self):
        print("Menu:\nPress 1 to generate a new password\nPress 2 to show my passwords\nPress 0 to exit!")
        print("=" * 50)
        self.menu_choice = int(input("Enter your choice(as an integer): "))
        print("=" * 50)
        if self.menu_choice == 0:
            self.Run = False
        elif self.menu_choice == 1:
            self.Password = ""
            self.new_password()
        elif self.menu_choice == 2:
            self.show_passwords()

    def new_password(self):
        self.Domain = input("Enter your domain: ")
        self.Length = int(input("Enter the Password's Length: "))
        print("=" * 50)
        self.password_generator()
        print("Domain: {}\nPassword: {}\n".format(self.Domain, self.Password))
        print("Do you wanna save it:\nPress 1 to save\nPress 2 to generate new password\nPress 0 to exit")
        self.save_input = int(input("Enter your input: "))
        if self.save_input == 1:
            self.rows.append([self.Domain, self.Password])
            for x in self.rows:
                print("Your value:\n{}: {}".format(x[0],x[1]))
            self.save_password()
        elif self.save_input == 2:
            self.Password = ""
            self.new_password()
        else:
            self.Run = False
        print("=" * 50)

    def save_password(self):
        with open(self.filename, 'a', newline='') as self.csvfile:
            self.csvwriter = csv.writer(self.csvfile)
            self.csvwriter.writerows(self.rows)
            self.csvfile.close()
        self.rows.clear()
        print("SAVED SUCCESSFULLY!")

    def show_passwords(self):
        self.show_feilds = []
        self.show_rows = []
        with open(self.filename, 'r') as self.csvfile:
            self.csvreader = csv.reader(self.csvfile)
            self.show_feilds = next(self.csvreader)
            print(self.csvreader)
            for row in self.csvreader:
                self.show_rows.append(row)
            print("Total no.of rows: %d"%(self.csvreader.line_num))
            self.cv_count = self.csvreader.line_num
            print(self.cv_count)
        print('Field names are: ' + ', '.join(field for field in self.show_feilds))
        print("The passwords are:\n")
        for x in self.show_rows:
            print(': '.join(map(str, x)))
            print("")
        print("Press 1 to run password generator\nPress 0 to exit")
        self.get_back_menu = int(input("Enter your input: "))
        print("=" * 50)
        if self.get_back_menu == 0:
            self.Run = False
        else:
            self.security_key()

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
        print("Password: {}\n".format(self.Password))


    def main(self):
        self.security_key()

if __name__ == '__main__':
    app = PasswordGenerator()
    app.main()

