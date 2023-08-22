import text
def read_file():
    f = open('date_updt.txt','r')
    tex=f.read()
    arr=list(tex.split("\n"))

    for i in range(26):


        text.data_ch[i][2]=int(arr[i])
    f.close()
    return tex

def write_file():
    f = open('date_updt.txt','w')
    s=''
    for i in range(25):
        s=s+str(text.data_ch[i][2])+'\n'
    s=s+str(text.data_ch[25][2])

    f.write(s)
    f.close()

