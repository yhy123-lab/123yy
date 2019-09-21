#二分查找
x = [1,3,4,6,7,8,9,10,11,12,13]
find = 8
def binary_chop(x,find):
    while len(x) > 1:
        if find > x[len(x)//2]:
            x = x[len(x)//2:len(x)]
        elif find < x[len(x)//2]:
            x = x[0:len(x)//2]
        else:
            return x[len(x)//2]
      
