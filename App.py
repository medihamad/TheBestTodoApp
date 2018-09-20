courses = ['medi', 'hamad', 'fuad']
courses2 = ['art', 'eduction']
print(courses)

print(courses[:1])

courses.append('art')
print(courses)

courses.insert(0, 'math')
print(courses)

courses.extend(courses2)
print(courses)

x = courses.pop()
print(courses)
print(x)

sire = [1,5,40,5,8,55,11,55,4]
sire.reverse()
print(sire)

hi = sorted(sire)
print(hi)

print(min(sire))
print(max(sire))
print(sire)
print(courses.index('fuad'))

for index, item in enumerate(courses, start=1):
    print(index, item)


setmedi = {'history', 'geo', 'food', 'coco'}

print(setmedi)

