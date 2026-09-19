Accounts = {
    "Cryolevel": "Abcakuganteng103",
    "salvinoke24": "Lelele1332"
}

username = input("Input Username: ")
password = input("Input Password: ")

if username in Accounts:
    if password == Accounts[username]:
        print("Login success")
    else:
        print("Login failed: Wrong Password")
else:
    print("Login failed: Username not found in database")