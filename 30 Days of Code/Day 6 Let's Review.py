# Enter your code here. Read input from STDIN. Print output to STDOUT

def even_odd_char(s):
    even = ''
    odd = ''
    for i in range(len(s)):
        if i==0 or i%2==0:
            #print('even')
            even += s[i]
        else:
            #print('odd')
            odd += s[i]
    
    output = even +' '+ odd
    print(output)



n = int(input())

for _ in range(n):
    s = input()
    even_odd_char(s)
