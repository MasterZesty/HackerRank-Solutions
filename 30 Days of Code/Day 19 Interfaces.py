class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        sum = 0
        i = 1
        import math
        while i<= math.sqrt(n):
            if n % i == 0:
                if n//i == i:
                    #print(i)
                    sum+= i
                else:
                    #print(i,n//i)
                    sum+= i + n//i
            i+=1
        return sum    
        

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)