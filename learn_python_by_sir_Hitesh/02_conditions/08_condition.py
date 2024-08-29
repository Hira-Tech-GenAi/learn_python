password = "Secure3P@ss"

if len(password)<6:
    strength = "Week"
elif len(password) <= 10:
    strength = "medium"
else:
    strength = "strong"

print("Password strength: ", strength)
