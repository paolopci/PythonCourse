password = input("Enter the password: ")
# verifica le condizioni per la password


result = {}

# Controlla se la password è più lunga di 8 caratteri
if len(password) > 8:
    result['length'] = True
else:
    result['length'] = False
# -------------------------------------------------------------------------------
# Controlla se la password contiene almeno una cifra
if any(char.isdigit() for char in password):
    result['digits'] = True
else:
    result['digits'] = False
# -------------------------------------------------------------------------------
# Controlla se la password contiene almeno una lettera maiuscola
if any(char.isupper() for char in password):
    result['upper-case'] = True
else:
    result['upper-case'] = False
# -------------------------------------------------------------------------------
print(result)
# -------------------------------------------------------------------------------
if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")


#    print(all(result))


# ------------------------------------------
# digit=False
# for char in password:
#     if char.isdigit():
#         digit = True
#         break
