import xml.dom.minidom as xdm
import time

# 在内存中创建一个空的文档
doc = xdm.Document()
# 创建一个根节点对象
root = doc.createElement('root')
# 设置根节点的属性
root.setAttribute('version', '1.0')
root.setAttribute('time', time.strftime('%Y-%m-%d %H:%M:%S'))
# 将根节点添加到文档对象中
doc.appendChild(root)

students = [
    {"name": "jack", "age": 18, "sex": 1},
    {"name": "mick", "age": 16, "sex": 2},
    {"name": "tony", "age": 19, "sex": 1}
]
for i in students:
    # 创建一个Student节点
    stu = doc.createElement('Studen')
    # 创建一个Name节点
    name = doc.createElement('Name')
    # 给Name节点添加文本
    name.appendChild(doc.createTextNode(str(i['name'])))

    # 创建Age节点
    age = doc.createElement('Age')
    age.appendChild(doc.createTextNode(str(i['age'])))

    # 创建Sex节点
    sex = doc.createElement('Sex')
    sex.appendChild(doc.createTextNode(str(i['sex'])))

    # 将Name、Age、Sex添加到Student节点下
    stu.appendChild(name)
    stu.appendChild(age)
    stu.appendChild(sex)

    # 将Student添加到root节点下
    root.appendChild(stu)

# 将创建的文档写入文件中
with open('create.xml', 'w') as f:
    doc.writexml(f, encoding='utf-8', indent='\t', addindent='\t', newl='\n')
