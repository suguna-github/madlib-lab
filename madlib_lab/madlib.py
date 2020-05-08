def file_initial_read(inputfile):
    f= open(inputfile,'r')
    #'/Users/bayyanap/Documents/python/inputfile.txt'
    contents =f.read()
    return contents
 
def split_content(contents):
    line = contents.split('{') 
    length = len(line)
    input_list =[]
    for i in range(length):
        istr = line[i] #.split('}')
        if "}" in istr:
            istr = line[i].split('}')
            input_list.append(istr[0])
            contents = contents.replace(istr[0],'')         
    return input_list,contents

def collect_input(input_list):
    responses =[]
    for inpdata in input_list:
        inputval = input(f"Enter an {inpdata} : ")
        responses.append(inputval)
    return responses  
      
def merge(input_list,contents):
    contents = contents.format(*input_list)
    return contents   