import xml.dom.minidom as xml


# 打开xml文件
XmlDoc = xml.parse('student.xml')
# 得到文档对象
doc = XmlDoc.documentElement

print(doc)

for elm in doc.childNodes:
    if (elm.nodeName != '#text') and (elm.nodeName != '#comment'):
        print('element name is :', elm.nodeName)
        for child in elm.childNodes:
            if child.nodeName != '#text':
                print('--', child.nodeName, ':', child.childNodes[0].data)
                # for k, v in child.attributes.items():
                #     print('------', k, ':', v)
                if child.hasAttribute('Detail'):
                    print('------', 'Detail: ', child.getAttribute('Detail'))


