import xml.etree.ElementTree as xeE

doc = xeE.ElementTree()

# 创建一个节点，并将节点设置为根节点
root = xeE.Element('root')
doc._setroot(root)

# 在root节点下创建一个Student节点
stu = xeE.SubElement(root, 'Student')
# 设置属性
stu.attrib = {'level': '1'}
# 在Student节点下创建一个Name节点
name = xeE.SubElement(stu, 'Name')
name.attrib = {'level': '2'}
name.text = 'mick'
age = xeE.SubElement(stu, 'Age')
age.text = '18'

# 继续在root节点下创建一个Student节点
stu = xeE.SubElement(root, 'Student')
# 设置属性
stu.attrib = {'level': '1'}
# 在Student节点下创建一个Name节点
name = xeE.SubElement(stu, 'Name')
name.attrib = {'level': '2'}
name.text = 'tony'
age = xeE.SubElement(stu, 'Age')
age.text = '19'

doc.write('create_by_etree.xml', encoding='utf-8', xml_declaration={'encoding': 'utf-8', 'version': '1.0'})
