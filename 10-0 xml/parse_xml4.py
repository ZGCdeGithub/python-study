import xml.etree.ElementTree as xeE

root = xeE.Element('root')
stu = xeE.SubElement(root, 'Student')
stu.attrib = {'num': '10001'}

name = xeE.SubElement(stu, 'Name')
name.text = 'jack'

age = xeE.SubElement(stu, 'Age')
age.text = '18'

xeE.dump(root)
