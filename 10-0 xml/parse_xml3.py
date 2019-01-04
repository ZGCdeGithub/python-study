import xml.etree.ElementTree as xeE

tree = xeE.parse(r'edit.xml')
root = tree.getroot()
# 添加一个新元素
e = xeE.Element('Student')
e.attrib = {"num": "10001", "grade": '9'}
e.text = '#text'
root.append(e)
tree.write('edit.xml')
