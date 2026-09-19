class Solution:
    def reverseBits(self, n: int) -> int:
        res=0

        for i in range(32):
            #save the bit

            bit=(n>>i)&1

            res=res| (bit<<31-i)
        return res


        