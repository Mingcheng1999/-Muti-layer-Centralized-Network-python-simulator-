class Node:
    def _init_(self,NodeType,idnum):
        self.NodeType=NodeType#FN/Node/Cluster head
        self.idnum=idnum#id of the node
        self.battery=1000
        self.NextNode=NULL
        self.PreviousNode=NULL
        self.EnergyConsumptionA=0
        self.EnergyConsumptionB=0
        self.waitconsump=1.65
        self.wakeup=1
        self.receive=1.40
    
    def getNodeType(self):
        return self.NodeType
        
    def getidnum(self):
        return self.idnum
        
    def getBattery(self):
        return self.battery
        
        
    def NextNode(self):
        return self.NextNode
        
        
    def setNodeType(self,NewNodetype):
        self.NewNodetype=NewNodetype
        
    def setidnum(self,Newidnum):
        self.idnum=Newidnum
        
    def setBattery(self,Newbattery):
        self.battery=Newbattery
    
    def setNextNode(self,NextNode):
        self.NextNode=NextNode
        
        
    def WaitConsumption():
        self.battery= self.battery-self.waitconsump   
        
    def wakeup():
        self.battery=self.battery-self.wakeup
        
 
        
        
    def boardcast(self):
        return
        #transmit
    
        #if self.NodeType=='AP':
         #   self.PreviousNode().WaitConsumption()
            
        #elif self.NodeType=='Node':
         #   if self.NextNode.getNodeType()=="Node":
          #      NextNode.wakeup()
           # elif self.NextNode.getNodeType()=="Node":
            #    NextNode.wakeup()
            #elif self.NextNode.getNodeType()=="AP":
             #   NextNode.wakeup()
        
       # elif self.NodeType=='FN':
        #else:
