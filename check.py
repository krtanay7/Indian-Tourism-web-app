import bcrypt

# Your hashed password
hashed = b"$2b$12$ETutPP6pkFIzndOf1VO4TOqUsWAM5Y0JufzLEBjycF7alrsS7ReDu"
# The password to check
password = input("pass: ")

# Check if the password matches the hash
if bcrypt.checkpw(password.encode('utf-8'), hashed):
    print("Password matches!")
else:
    print("Password does not match.")
