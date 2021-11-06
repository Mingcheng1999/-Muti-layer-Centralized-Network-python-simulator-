class Node:
    def __init__(self,NodeType,idnum):
        self.NodeType=NodeType#FN/Node/CH
        self.idnum=idnum#id of the node
        self.battery=1000
        self.NextNode=None
        self.PreviousNode=None
        self.EnergyConsumptionA=0
        self.EnergyConsumptionB=0
        self.waitconsump=1.65
        self.wakeup=1
        self.receive=1.40
        
        
        
        
        #To do: the following data are not accurrate, please find it on the website
        self.Ek=1.5
        self.E_sleep=2.6
        self.E_wk=3.7
        self.E_rx=4.8
        self.E_tx_ack=5.9
        self.E_tx_pack=6.3
        self.E_eidle=7.7
        self.E_rx_pack11=8.2
        self.E_rx_ack11=7.8
        
        
        
    
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
        
        
    def WaitConsumption():#did not use but I am too lazy to delete
        self.battery= self.battery-self.waitconsump   
        
    def wakeup():#did not use but I am too lazy to delete
        self.battery=self.battery-self.wakeup
        
 
        
        
    def boardcast(self):
        #To do:improve this method
        if self.NodeType=='Node':#energy of Node
            self.Ek=self.E_wk+self.E_wk+self.E_rx+self.E_tx_pack+self.E_rx
            self.battery=self.battery-self.Ek
            self.NextNode.boardcast()
        elif self.NodeType=='CH':#energy of cluster head
            self.Ek=self.E_sleep+self.E_wk+self.E_tx_ack+self.E_rx+self.E_tx_ack+self.E_eidle+self.E_tx_pack
            self.battery=self.battery-self.Ek
            self.NextNode.boardcast()
        elif self.NodeType=='FN':#energy of FN
            self.Ek=self.E_sleep+self.E_wk+self.E_rx+self.E_tx_ack+self.E_rx+self.E_tx_ack+self.E_eidle+self.E_rx_pack11+self.E_rx_ack11
            self.battery=self.battery-self.Ek
            self.NextNode.boardcast()
        else:#ap
            return
        
        
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
