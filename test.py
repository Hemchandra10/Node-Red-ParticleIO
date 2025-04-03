import json
import os

file_path = "/home/codespace/.node-red/data/rules.json"

# 🔹 Read the JSON file
with open(file_path, "r") as file:
            rules = file.read()

print(rules)



