result = 0

def add(num):
    global result
    result += num
    return result

class Cal():
    def __init__(self):
        self.result=0
        pass
    def sum(self, num):
        self.result += num
        return self.result
    def minus(self,num):
        self.result -= num
        return self.result
    def mul(self,num):
        self.result *= num
        return self.result
    def div(self,num):
        self.result /= num
        return self.result
    
    
Cal_1 = Cal()
cal1 = Cal_1.sum(10)
print(cal1)

Cal_2 = Cal()
cal2 =Cal_2.sum(20)

cal2 = cal1

print(cal2)

