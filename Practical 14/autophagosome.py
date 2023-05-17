from xml.dom.minidom import parse
import xml.dom.minidom
import pandas as pd
DOMTree = xml.dom.minidom.parse("./go_obo.xml")
root = DOMTree.documentElement
defstrs = root.getElementsByTagName('defstr')

root = DOMTree.documentElement
data = []
for term in root.getElementsByTagName('term'):
    defstr = term.getElementsByTagName('def')[0].getElementsByTagName('defstr')[0].childNodes[0].data
    if 'autophagosome' in defstr:
        go_id = term.getElementsByTagName('id')[0].childNodes[0].data
        name = term.getElementsByTagName('name')[0].childNodes[0].data
        num_child_nodes = len(term.childNodes)
        data.append([go_id,name,defstr,num_child_nodes])
df = pd.DataFrame(data, columns=['GO id', 'Term name', 'Definition string', 'Number of child nodes'])       
df.to_excel('./autophagosome.xlsx',index=False)
