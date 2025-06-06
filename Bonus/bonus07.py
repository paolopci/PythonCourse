filenames=['1. testo.txt','2. testo.txt','3. testo.txt','4. testo.txt','5. testo.txt']


filenames=[filename.replace('.','-',1).replace('txt','pdf') for filename in filenames]
print(filenames) 


new = [i for i in ['a', 'b', 'c']]
print(new)