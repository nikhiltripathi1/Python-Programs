import re
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    p=r'([\w])+\.[0-9]{1}'
    for i in student_marks:
        if i==query_name:
            per=str(round(sum(student_marks[i])/3,2))
            match=re.match(p,per)
            if match:
                print(per+'0')
            else:
                print(per)    
