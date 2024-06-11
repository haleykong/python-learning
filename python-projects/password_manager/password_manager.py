from cryptography.fernet import Fernet

# ENCRYPTION:
# key + password + txt to encrypt = random text
# random text + key + password = text to encrypt

'''
def write_key():
    key = Fernet.generate_key()
    # wb = write bytes
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


# Bytes is used to store information
# Encode takes string and turns into bytes
key = load_key()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        # readlines will return all lines of file
        for line in f.readlines():
            # Strips off carriage return
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    # With statement - automatically closes file
    # 'w' - overwrite file
    # 'r' - read file
    # 'a' - append to end of existing file, create new file if does not exist
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("Would you like to add a new password or view existing ones\
                 (view, add), press q to quit? ").lower()

    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue
