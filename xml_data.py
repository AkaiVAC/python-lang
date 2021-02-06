import xml.dom.minidom


def printSkills(doc):
    skills = doc.getElementsByTagName('skill')
    print('%d skills:' % skills.length)
    for skill in skills:
        print('\t%s' % skill.getAttribute('name'))


def main():
    doc = xml.dom.minidom.parse('files/index.xml')
    print(doc.nodeName)
    print(doc.firstChild.tagName)

    printSkills(doc)

    newSkill = doc.createElement("skill")
    newSkill.setAttribute('name', 'jQuery')
    doc.firstChild.appendChild(newSkill)

    printSkills(doc)


if (__name__ == '__main__'):
    main()
