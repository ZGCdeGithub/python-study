import xml.etree.ElementTree as xeE

root = xeE.parse('student.xml')

print('***使用getiterator**')
nodes = root.getiterator()
for e in nodes:
    print('{0} -- {1}'.format(e.tag, e.text))

print('***使用find访问')
e_teacher = root.find('Teacher')
print(e_teacher)
print('{0} -- {1}'.format(e_teacher.tag, e_teacher.text))
e_c = e_teacher.find('Name')
print('{0} -- {1}'.format(e_c.tag, e_c.text))

print('***使用findall访问')
e_student = root.findall('Student')
print(e_student)
for ele in e_student:
    print('-- {0} -- {1}'.format(ele.tag, ele.text))
    for sub in ele.getiterator():
        print('---- {0} -- {1}'.format(sub.tag, sub.text))
