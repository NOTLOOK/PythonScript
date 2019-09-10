#请使⽤Python代码反转句⼦ long with me play game -->> game play me with long ;
a="long with me play game"
b=a.split() #得到的是一个列表
b.reverse() #反转列表
print(' '.join(b))