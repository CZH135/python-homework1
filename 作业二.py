import math

def func(n,start_h=100,g=9.8):
    #start_h表示初始高度，g表示加速度
    # 1. 计算反弹高度
    bh=start_h/(2**n)
    
    # 2. 计算总路程
    total_distance = start_h  #初始下落的距离
    # 前n-1次弹起和下落的距离总和
    for i in range(1,n):
        hi=start_h/(2**i)
        total_distance+=2*hi  #弹起+下落的总距离

    total_distance+=bh#第n次弹起的距离
    
    # 3. 计算总时间t
    t= math.sqrt(2*start_h/g)  #初始下落时间
    # 前n-1次弹起和下落的时间总和
    for i in range(1,n):
        hi = start_h / (2**i)
        # 每次弹起和下落时间各一次
        t+=2*math.sqrt(2*hi/g)
    # 第n次弹起的时间
    t+=math.sqrt(2*bh/g)
    
    return bh,total_distance,t

#(1)第10次掉下并反弹到最高点时，反弹了多高？此时球一共经过多少米，运动了多少时间？
h0,d0,t0=func(10)
print(f"第10次掉下反弹的高度为{h0:.2f}米")#保留两位小数
print(f"第10次掉下一共经过{d0:.2f}米")
print(f"第10次掉下运动了{t0:.2f}秒")

#(2)第n次掉下并反弹到最高点时，反弹了多高？此时球一共经过多少米，运动了多少时间？
n=int(input("请输入第几次掉下（n的值）并反弹到最高点："))
h,d,t=func(n)
print(f"第n次(n={n})掉下并反弹到最高点时：")
print(f"反弹的高度为{h:.2f}米")
print(f"总路程为{d:.2f}米")
print(f"总时间为{t:.2f}秒")