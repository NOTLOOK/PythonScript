def plog(dict01):
    dict02=dict(sorted(dict01.items(),key=lambda x:x[1],reverse=True)[:10])
    return dict02

def hot(dict01):
    dict02=dict(sorted(dict01.items(),key=lambda x:x[1],reverse=True)[:1])
    return dict02