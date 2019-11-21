
def PrintOutput(string):
    print("Output",string)

def LoadFile(file):
    f=open(file,'r')
    lines=f.read()
    print("OUTPUT>",lines)
    
def UpdateString(string1,string2,index):
    return string2[:index]+string1+string2[index+1:]

