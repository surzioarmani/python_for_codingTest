import re

def solution(new_id):
    answer = ''
    new_id = case1(new_id)
    new_id = case2(new_id)
    new_id = case3(new_id)
    new_id = case4(new_id)
    new_id = case5(new_id)
    new_id = case6(new_id)
    new_id = case7(new_id)

    
    print(new_id)
    return new_id

def case1(new_id):
    return new_id.lower()

def case2(new_id):
    p = re.compile("[0-9a-z-_.]")
    return ("".join(p.findall(new_id)))

def case3(new_id):
    for i in range(len(new_id)):
        if ".." in new_id:
            new_id = new_id.replace("..",".", 1)             
    return new_id

def case4(new_id):
    if len(new_id) >= 1:
        if new_id[-1] == ".":
            new_id = new_id[:-1]        
        if new_id:
            if  new_id[0] ==".":
                new_id = new_id[1:]
    return new_id

def case5(new_id):
    if not new_id or new_id =="":
        new_id = "a"
    return new_id

def case6(new_id):
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id =new_id[:-1]
    return new_id

def case7(new_id):
    while len(new_id) <= 2:
        if len(new_id) == 3:
            break
        else:
            new_id = new_id + new_id[-1]
    return new_id
        

        
    
    
solution("...!@BaT#*..y.abcdefghijklm")
solution("z-+.^.")
solution("=.=")
solution("123_.def")
solution("abcdefghijklmn.p")
solution("")


