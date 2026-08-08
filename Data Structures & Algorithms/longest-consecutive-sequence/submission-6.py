class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #turn the array into a set
        #turn it back into an array
        #sort the array
        #init left
        #init right
        #TARGET=FIRST VALUE
        #count value
        #retval
        #for i in range array, start at secodn value
            #if array[r]==target+1
            #count+=1
            #else:
            #retval=max(count,retval)
            #count=1
            #l=r
            #retval=1

        my_set=set(nums)
        new_list=list(my_set)
        new_list.sort()
        left=0
        if len(new_list)>0:
            target=new_list[0]
        count=1
        retval=0

        if len(new_list)==0:
            return 0
        if len(new_list)==1:
            return 1

        for r in range(1,len(new_list)):
            if new_list[r]==target+1:
                count+=1
            else:
                retval=max(count,retval)
                count=1
                l=r
                
            target=new_list[r]
        retval=max(count,retval)
        return retval



        
            

        