
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None
        

class MyLinkedList:

    def __init__(self):
        self.left=Node(0)
        self.right=Node(0)
        self.left.next=self.right
        self.right.prev=self.left



    
    def get(self, index: int) -> int:
        cur=self.left.next

        while(index>0 and cur):
            cur=cur.next
            index-=1
        
        if(cur and index==0 and cur !=self.right):
            return cur.val
        
        return -1

      
        

    def addAtHead(self, val: int) -> None:
        
        prev=self.left
        next=prev.next

        new=Node(val)
        prev.next=new
        next.prev=new
        new.next=next
        new.prev=prev
        

    def addAtTail(self, val: int) -> None:

        prev=self.right.prev
        next=self.right

        new=Node(val)
        prev.next=new
        new.next=next
        new.prev=prev
        next.prev=new



      
        

    def addAtIndex(self, index: int, val: int) -> None:
        #Base nothing inside the LL

        
        
        cur=self.left.next
        new=Node(val)

        while(index>0 and cur):
            cur=cur.next
            index-=1
        
        if(cur and index==0 ):
            cur.prev.next=new
            
            new.prev=cur.prev
            cur.prev=new
            new.next=cur

            

                

                        







        

    def deleteAtIndex(self, index: int) -> None:

        cur=self.left.next
       

        while(index>0 and cur):
            cur=cur.next
            index-=1
        
        if(cur and index==0 and cur!=self.right and cur!=self.left ):
            cur.prev.next=cur.next
            cur.next.prev=cur.prev

            
            


        
        
                
                

                
                
            
        

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)