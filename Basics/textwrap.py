def wrap(string, width):
    i=0
    a=[]
    while i<len(string):
        a.append(string[i:width+i])
        print(a)
        i+=width
    return '\n'.join(a)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
