import xml.etree.ElementTree as ET

xml_data = '''<users>
    <user id="1">
        <name>Shalini</name>
        <profession>Tester</profession>
        <age type="int">27</age>
    </user>
    <user id="2">
        <name>Vibhor</name>
        <profession>Lead</profession>
        <age type="int">30</age>
    </user>
</users>'''
# Parsing xml_data from elemntTree to fromString is known as DE-SERIALIZATION
tree = ET.fromstring(xml_data)
# print('Name: ', tree.find('name').text)
lst = tree.findall('user')
print("Length of tree: ",len(tree.findall('user')))
for item in lst:
    print('name: ', item.find('name').text)
    print('profession: ', item.find('profession').text)
    print('age: ', item.find('age').text)
