import random

chars = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{}|;:,.<>?`~"

password = ""
for i in range (16):
    password += random.choice(chars)
print(f"Your password is: {password}")    
