def read_template(path):
    try:
        with open(path,'r') as f:
            text=f.read()
        return text
    except FileNotFoundError:
        return f'This path not found {path}'
    
def parse_template(a):
    try:
        start=a.find('{')
        end=a.find('}')
        listW=[]
        listW.append(a[start+1:end])
        b=a.replace(a[start:end+1],'{}',1)
        nWord=a.count('{')
        counter=1
        while counter<nWord:
            start=a.find('{',end)
            end=a.find('}',end+1)
            listW.append(a[start+1:end])
            b=b.replace(a[start:end+1],'{}',1)
            counter+=1
        listW=tuple(listW)
        return b, listW
    except:
        return "The text formate does not appropriate"

def welcome(words):
    print('Welcome in Madlib Cli Game we hope you to have fun')
    inputs=[]
    for i in words:
        a=input(f"Please enter {i}  ")
        if i[:6]=="Number":
            while not a.isdigit():
                a=input(f"Please enter {i} you should inter number ")
        if i=="Number 1-50":
            while float(a)<1 or float(a)>50:
                a=input(f"Please enter {i} you should inter number that between 1-50 ")
        inputs.append(a)
    inputs=tuple(inputs)
    return inputs
    
def merge(text,inputs):
    for i in inputs:
        text=text.replace("{}",i,1)
    return text

def write(path,content):
    with open(path,'w+') as f:
        f.write(content)
        f.seek(0)
        result=f.read()
    return result

#main 
# a=read_template('assests\dark_and_stormy_night_template.txt')
# b,c=parse_template(a)
# d=welcome(c)
# final=merge(b,d)
# print(write('assests\dark_and_stormy_night_template.txt', final))
