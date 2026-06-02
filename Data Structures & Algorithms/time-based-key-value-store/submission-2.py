from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store=defaultdict(list)
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append({"name": value, "age": timestamp})

        

    def get(self, key: str, timestamp: int) -> str:
        l=0
        r=len(self.store[key])-1
        maxim=""
        while(l<=r):
            m=(l+r)//2
            if(self.store[key][m]["age"]==timestamp):
                return self.store[key][m]["name"]
            else:
                if(self.store[key][m]["age"]<timestamp):
                    maxim=self.store[key][m]["name"]
                    l=m+1
                else:
                    r=m-1
        return maxim
                


        
        
