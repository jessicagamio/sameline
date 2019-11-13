import itertools

def sameline(points):

    lines=[]

    for p1,p2,p3 in itertools.combinations(points,3):
        print(p1,p2,p3)
        if p1[0]==p1[1] and p2[0] == p2[1] and p3[0]==p3[1]:
            print('we have an x,y match')
            lines.append([p1,p2,p3])
        elif p1[0]==p2[0] and p1[0] == p3[0]:
            lines.append([p1,p2,p3])
        elif p1[1]==p2[1] and p1[1] == p3[1]:
            lines.append([p1,p2,p3])

    return lines

points=[(0,0), (1,1), (2,3), (3,2), (3,3), (3,4)]

print(sameline(points))
