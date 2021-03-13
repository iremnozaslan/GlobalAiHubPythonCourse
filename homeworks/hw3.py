d = {}
l = []
for i in range(1,3):
    midterm = float(input("Enter your midterm grade:"))
    project = float(input("Enter your project grade:"))
    final = float(input("Enter your final grade:"))
    passingGrade = (midterm * (0.3)) + (project * (0.3)) + (final * (0.4))
    d['Stdnt'+str(i)] = passingGrade

print(d)


#with looping through dict:

for value in d:
    l.append(d[value])
print(l)

#Without indexing:

"""
l = list(d.values())
print(l)

""" 
l.sort()
print(l)
