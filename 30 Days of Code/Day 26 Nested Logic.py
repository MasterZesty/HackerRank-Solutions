# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
#my logic
return_date = list(map(int,input().split(' ')))
due_date = list(map(int,input().split(' ')))


def lib_fine_calculator(return_date,due_date):
    fine = 0
    #condition 1
    if return_date == due_date:
        return fine
    
    flag_1 = return_date[0] < due_date[0]
    flag_2 = return_date[1] < due_date[1]
    flag_3 = return_date[2] < due_date[2]
    
    if flag_1 and (flag_2 and flag3):
        return fine
    
    #condition 4
    if return_date[2] > due_date[2]:
        return 1000
    
    #condition 2
    if return_date[0] > due_date[0]:
        if (return_date[1] == due_date[1]) and (return_date[2] == due_date[2]):
            return (15*(return_date[0]-due_date[0]))
    
    #condition 3
    if return_date[1] > due_date[1]:
        if (return_date[2] == due_date[2]):
            return (500*(return_date[1]-due_date[1]))
    
print(lib_fine_calculator(return_date,due_date))
'''
rd, rm, ry = [int(x) for x in input().split(' ')]
ed, em, ey = [int(x) for x in input().split(' ')]

if (ry, rm, rd) <= (ey, em, ed):
    print(0)
elif (ry, rm) == (ey, em):
    print(15 * (rd - ed))
elif ry == ey:
    print(500 * (rm - em))
else:
    print(10000)
