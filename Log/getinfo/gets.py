def log(path,num):
    parm={}
    with open(file=path,mode='r',encoding='utf8') as file:
        for line in file.readlines():
            if line.split()[num] not in parm.keys():
                parm.setdefault(line.split()[num],1)
            else:
                parm[line.split()[num]] +=1
    return parm

