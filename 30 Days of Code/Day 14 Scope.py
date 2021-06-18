class Difference:
    def __init__(self, a):
        self.__elements = a
    maximumDifference = 0 
    # Add your code here
    def computeDifference(self):
        self.maximumDifference = self.__elements[0] - self.__elements[1]
        for i in range(0,len(self.__elements)):
            for j in range(i+1,len(self.__elements)):
                dif = abs(self.__elements[i]-self.__elements[j])
                #print('dif:',dif)
                if dif > self.maximumDifference:
                    self.maximumDifference = dif
        #print('maximumDifference:',self.maximumDifference)
        return self.maximumDifference

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)