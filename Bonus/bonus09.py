password = input("Enter the password: ")
# verifica le condizioni per la password


result = []

if len(password) > 8:
    result.append(True)
else:
    result.append(False)
# -------------------------------------------------------------------------------
if any(char.isdigit() for char in password):
    result.append(True)
else:
    result.append(False)
# -------------------------------------------------------------------------------
if any(char.isupper() for char in password):
    result.append(True)
else:
    result.append(False)
# -------------------------------------------------------------------------------

print(all(result))


# ------------------------------------------
# digit=False
# for char in password:
#     if char.isdigit():
#         digit = True
#         break
