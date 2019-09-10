#请使⽤Python代码对 [23, 14, 12, 21, 45, 99, 34, 42] 进⾏排序, 请使⽤冒泡算法;
a=[23, 14, 12, 21, 45, 99, 34, 42]
for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)
#请使⽤Python代码对 {'tom': 198, 'jerry': 34, 'hale': 400, 'tony':23} 进⾏排序, 请使⽤⾼阶函数;
a={'tom': 198, 'jerry': 34, 'hale': 400, 'tony':23}
a=dict(sorted(a.items(),key=lambda x:x[1],reverse=False))
print(a)