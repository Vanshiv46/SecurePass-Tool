import hashlib
import re

print("=== SecurePass Tool ===")
print("1. Check Password Strength")
print("2. Encrypt Password")

choice = input("Enter choice (1/2): ")

def check_strength(password):

    length = len(password)
    has_upper = re.search(r"[A-Z]", password)
    has_lower = re.search(r"[a-z]", password)
    has_digit = re.search(r"[0-9]", password)
    has_symbol = re.search(r"[@#$%^&*!]", password)

    score = 0

    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1

    if score <= 2:
        print("Password Strength: Weak")
    elif score == 3 or score == 4:
        print("Password Strength: Medium")
    else:
        print("Password Strength: Strong")


def encrypt_password(password):

    encrypted = hashlib.sha256(password.encode()).hexdigest()

    print("Encrypted Password:")
    print(encrypted)


if choice == "1":

    password = input("Enter Password: ")
    check_strength(password)

elif choice == "2":

    password = input("Enter Password: ")
    encrypt_password(password)

else:
    print("Invalid choice")