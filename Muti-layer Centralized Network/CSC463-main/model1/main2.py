from Node import Node


def main():

    Node1=Node('Node',1)
    Node2=Node('CH',2)
    Node3=Node('CH',3)
    Node4=Node('CH',4)
    Node5=Node('CH',5)
    Node6=Node('CH',6)
    Node7=Node('CH',7)
    Node8=Node('CH',8)
    Node9=Node('CH',9)
    Node10=Node('CH',10)
    Node11=Node('CH',11)
    Node12=Node('CH',12)
    Node13=Node('CH',13)
    Node14=Node('CH',14)
    Node15=Node('CH',15)
    Node16=Node('AP',15)
    
    
    Node1.setNextNode(Node2)
    Node2.setNextNode(Node3)
    Node3.setNextNode(Node4)
    Node4.setNextNode(Node5)
    Node5.setNextNode(Node6)
    Node6.setNextNode(Node7)
    Node7.setNextNode(Node8)
    Node8.setNextNode(Node9)
    Node9.setNextNode(Node10)
    Node10.setNextNode(Node11)
    Node11.setNextNode(Node12)
    Node12.setNextNode(Node13)
    Node13.setNextNode(Node14)
    Node14.setNextNode(Node15)
    Node15.setNextNode(Node16)
    
    
    
    print(Node1.getBattery())
    print("simulate...\n")
    Node1.boardcast()
    
    print("Node status:\n")
    
    Sum=0
    print("Node1: "+"Type: "+Node1.getNodeType()+"  Battery: ",Node1.getBattery(),"  Takes:",round(1000-Node1.getBattery(),1),"watt\n")
    Sum=Sum+(1000-Node1.getBattery())
    print("Node2: "+"Type: "+Node2.getNodeType()+"  Battery: ",Node2.getBattery(),"  Takes:",round(1000-Node2.getBattery(),1),"watt\n")
    Sum=Sum+(1000-Node2.getBattery())
    print("Node3: "+"Type: "+Node3.getNodeType()+"  Battery: ",Node3.getBattery(),"  Takes:",round(1000-Node3.getBattery(),1),"watt\n")
    Sum=Sum+(1000-Node3.getBattery())
    print("Node4: "+"Type: "+Node4.getNodeType()+"  Battery: ",Node4.getBattery(),"  Takes:",round(1000-Node4.getBattery(),1),"watt\n")
    Sum=Sum+(1000-Node4.getBattery())
    print("Node5: "+"Type: "+Node5.getNodeType()+"  Battery: ",Node5.getBattery(),"  Takes:",round(1000-Node5.getBattery(),1),"watt\n")
    Sum=Sum+(1000-Node5.getBattery())
    print("Node6: "+"Type: "+Node6.getNodeType()+"  Battery: ",Node6.getBattery(),"  Takes:",round(1000-Node6.getBattery(),1),"watt\n")
    Sum=Sum+(1000-Node6.getBattery())
    print("Node7: "+"Type: "+Node7.getNodeType()+"  Battery: ",Node7.getBattery(),"  Takes:",round(1000-Node7.getBattery(),1),"watt\n")
    Sum=Sum+(1000-Node7.getBattery())
    print("Node8: "+"Type: "+Node8.getNodeType()+"  Battery: ",Node8.getBattery(),"  Takes:",round(1000-Node8.getBattery(),1),"watt\n")
    Sum=Sum+(1000-Node8.getBattery())
    print("Node9: "+"Type: "+Node9.getNodeType()+"  Battery: ",Node9.getBattery(),"  Takes:",round(1000-Node9.getBattery(),1),"watt\n")
    Sum=Sum+(1000-Node9.getBattery())
    print("Node10: "+"Type: "+Node10.getNodeType()+"  Battery: ",Node10.getBattery(),"  Takes:",round(1000-Node10.getBattery(),1),"watt\n")
    Sum=Sum+(1000-Node10.getBattery())
    print("Node11: "+"Type: "+Node11.getNodeType()+"  Battery: ",Node11.getBattery(),"  Takes:",round(1000-Node11.getBattery(),1),"watt\n")
    Sum=Sum+(1000-Node11.getBattery())
    print("Node12: "+"Type: "+Node12.getNodeType()+"  Battery: ",Node12.getBattery(),"  Takes:",round(1000-Node12.getBattery(),1),"watt\n")
    Sum=Sum+(1000-Node12.getBattery())
    print("Node13: "+"Type: "+Node13.getNodeType()+"  Battery: ",Node13.getBattery(),"  Takes:",round(1000-Node13.getBattery(),1),"watt\n")
    Sum=Sum+(1000-Node13.getBattery())
    print("Node14: "+"Type: "+Node14.getNodeType()+"  Battery: ",Node14.getBattery(),"  Takes:",round(1000-Node14.getBattery(),1),"watt\n")
    Sum=Sum+(1000-Node14.getBattery())
    print("Node15: "+"Type: "+Node15.getNodeType()+"  Battery: ",Node15.getBattery(),"  Takes:",round(1000-Node15.getBattery(),1),"watt\n")
    Sum=Sum+(1000-Node15.getBattery())
    print("Node16: "+"Type: "+Node16.getNodeType()+"  Battery: ",Node16.getBattery(),"  Takes:",round(1000-Node16.getBattery(),1),"watt\n")
    Sum=Sum+(1000-Node16.getBattery())
    
    
    print("the total energy consumption is",round(Sum,1))
    
    return
    
    

main()

