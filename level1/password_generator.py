import random
import string

def main():
    print("\nWelcome to Password Generator!")
    print("You can choose to generate 3 types of password.")
    print("r: random password(letter, number and symbols)")

    user_choice = input("Please enter: ")
    if user_choice == 'r':
        print(random_pw())


def random_pw():
    letter_str = string.ascii_lowercase  #return a string of 'abc----z'
    num_list = string.digits
    symbols_list = string.punctuation    
    password = ""

    while True:
        try:
            num = input("Do you want to include number or not? (y/n): ").lower()
            symbols = input("Do you want to include symbols or not? (y/n): ").lower()

            if num == 'y' and symbols == 'y':
                pool = letter_str + num_list + symbols_list
                length = int(input("Choose the length of the password: "))
                for _ in range(length):
                    pw = random.choice(pool)  #<-- in here dont have to be list,  even string that has sequence index
                    password += pw

            elif num == 'y' and symbols == 'n':
                pool = letter_str + num_list
                length = int(input("Choose the length of the password: "))
                for _ in range(length):
                    pw = random.choice(pool)  #<-- in here dont have to be list,  even string that has sequence index
                    password += pw
            elif num == 'n' and symbols == 'y':
                pool = letter_str + symbols_list
                length = int(input("Choose the length of the password: "))
                for _ in range(length):
                    pw = random.choice(pool)  #<-- in here dont have to be list,  even string that has sequence index
                    password += pw
            else:
                pool = letter_str
                length = int(input("Choose the length of the password: "))
                for _ in range(length):
                    pw = random.choice(pool)  #<-- in here dont have to be list,  even string that has sequence index
                    password += pw
        except ValueError:
            print("Please enter (y/n): ")
            continue
        else:
            break
    return password
if __name__ == "__main__":
    main()