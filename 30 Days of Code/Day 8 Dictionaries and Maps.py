# Enter your code here. Read input from STDIN. Print output to STDOUT
phonebook = dict()

n = int(input())

for i in range(n):
    inp = input()
    inp_command = inp.split()
    #print(inp_command)
    phonebook[inp_command[0]] = int(inp_command[1])

#print(phonebook)

while True:
    try:
        name = input()
        phonenumber =  phonebook.get(name)
        if phonenumber:
            out = '%s=%d'%(name,phonenumber)
            print(out)
        else:
            print("Not found")
        
    except EOFError as e:
        break
