import os

# 🔴 Command Injection
user_input = input("Enter a filename to display: ")  # SOURCE
os.system("cat " + user_input)  # SINK ❌

# 🔴 Path Traversal
file_name = input("Enter file path: ")  # SOURCE
with open("/tmp/" + file_name, "r") as f:  # SINK ❌
    print(f.read())