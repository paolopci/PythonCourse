list = ['paolo', 'mario', 'luigi', 'peach', 'toad', 'bowser']

list.sort(reverse=True)

for index, item in enumerate(list):
    row = print(f"{index+1}) obj:  {item}")
