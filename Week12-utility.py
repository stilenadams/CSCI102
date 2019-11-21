
def PrintOutput(string):
    print("Output",string)

def LoadFile(file):
    f=open(file,'r')
    lines=f.read()
    Lines=lines.split(" ")
    print("OUTPUT>",Lines)
    return Lines
    
def UpdateString(string1,string2,index):
    return string2[:index]+string1+string2[index+1:]

def FindWordCount(List,string):
    count=List.count(string)
    print("OUTPUT>",count)
def ScoreFinder(players,scores,name):
    if name in players:
        
        position=int(players.index(name))
        score=scores[position]
        print("OUTPUT>",name,"got a score of ",score)
    else:
        print("OUTPUT> Player not found")
    
def Union(players,scores):
    for i in players:
        scores.append(i)
    print("OUTPUT>" ,scores)

def Intersection(List1,List2):
    List3=[]
    for i in List1:
        if i in List2:
            List3.append(i)
    print("OUTPUT>",List3)
    
def NotIn(List1,List2):
    List3=[]
    for i in List1:
        if i not in List2:
            List3.append(i)
    print("OUTPUT>",List3)


