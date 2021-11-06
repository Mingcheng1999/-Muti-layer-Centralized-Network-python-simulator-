from Node import Node


def main():

    Node1=Node('Node',1)
    Node2=Node('FN',2)
    Node3=Node('CH',3)
    Node4=Node('AP',4)
    Node1.setNextNode(Node3)
    Node3.setNextNode(Node2)
    Node2.setNextNode(Node4)
    print("simulate...\n")
    
    Node1.boardcast()
    
    
    print("get the result!")
    
    print("Node status:\n")
    
    
    
    
    Sum=0
    print("Node1: "+"Type: "+Node1.getNodeType()+"  Battery: ",Node1.getBattery(),"  Takes:",round(1000-Node1.getBattery(),1),"watt\n")
    Sum=Sum+(1000-Node1.getBattery())
    #print(Sum)
    print("Node2: "+"Type: "+Node2.getNodeType()+"  Battery: ",Node2.getBattery(),"  Takes:",round(1000-Node2.getBattery(),1),"watt\n")
    Sum=Sum+(1000-Node2.getBattery())
    #print(Sum)
    print("Node3: "+"Type: "+Node3.getNodeType()+"  Battery: ",Node3.getBattery(),"  Takes:",round(1000-Node3.getBattery(),1),"watt\n")
    Sum=Sum+(1000-Node3.getBattery())
    #print(Sum)
    print("Node4: "+"Type: "+Node4.getNodeType()+"  Battery: ",Node4.getBattery(),"  Takes:",round(1000-Node4.getBattery(),1),"watt\n")
    Sum=Sum+(1000-Node4.getBattery())
    #print(Sum)

    print("the total energy consumption is",round(Sum,1))
    return
    
    

main()

