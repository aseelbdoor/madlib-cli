def read_template(path):
    try:
        with open(path,'r') as f:
            text=f.read()
        return text
    except FileNotFoundError:
        raise FileNotFoundError (f'File not found at path: {path}')
    
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
    print('''
    Welcome to the Madlib game! In this game, you will be asked to provide various parts of speech such as nouns, verbs, and adjectives, which will be used to fill in the blanks of a story.

    To get started, simply follow the prompts and enter the requested words when prompted. Once you've entered all the words, the completed story will be displayed.

    Let's get started!''')
    
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
if __name__=="__main__":
    a = read_template('/home/aseel/python-fun/madlib-cli/madlib_cli/assets/text.txt')
    b, c = parse_template(a)
    d = welcome(c)
    final = merge(b, d)
    print(write('/home/aseel/python-fun/madlib-cli/madlib_cli/assets/newFile.txt', final))

