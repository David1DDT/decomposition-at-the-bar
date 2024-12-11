class number():
    def __init__(self, value):
        self.value = value
    def PrimeFactorizationCalculator(self):
        temp = self.value
        primefactorslist = []
        while temp != 1:
            for i in range(2,temp + 1):
                if temp % i == 0:
                    temp = int(temp /i)
                    primefactorslist.append(i)
                    break
        return primefactorslist


num = number(int(input("Prime Factorization Calculator: ")))
print(num.PrimeFactorizationCalculator())

                
