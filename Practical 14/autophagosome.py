from xml.dom.minidom import parse
import xml.dom.minidom
import pandas as pd
def count_child_nodes(go_id): # Define a function to count the number of child nodes for a given node ID
    count = 0
    for term in root.getElementsByTagName('term'):
        is_a = term.getElementsByTagName('is_a')
        for isa in is_a:
            if isa.childNodes[0].data == go_id:
                count += 1
                count += count_child_nodes(term.getElementsByTagName('id')[0].childNodes[0].data)
    return count
# Parse the XML file and get the root element
DOMTree = xml.dom.minidom.parse("./go_obo.xml")
root = DOMTree.documentElement
# Get all the definition strings from the root element
defstrs = root.getElementsByTagName('defstr') 

root = DOMTree.documentElement
data = [] #create an empty list to store data
for term in root.getElementsByTagName('term'):
    defstr = term.getElementsByTagName('def')[0].getElementsByTagName('defstr')[0].childNodes[0].data #Get the definition string for the term
    if 'autophagosome' in defstr:  # Check if the definition string contains the word 'autophagosome'
        go_id = term.getElementsByTagName('id')[0].childNodes[0].data #get the id
        name = term.getElementsByTagName('name')[0].childNodes[0].data #get the name
        num_child_nodes = count_child_nodes(go_id)
        data.append([go_id,name,defstr,num_child_nodes]) #add the data to the list
df = pd.DataFrame(data, columns=['GO id', 'Term name', 'Definition string', 'Number of child nodes'])    
df.to_excel('./autophagosome.xlsx',index=False) #make excel using pandas  
