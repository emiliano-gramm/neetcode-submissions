class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        mBananas = piles[-1]
        print("mbananas", mBananas)

        l, r = 1, mBananas
        k = 1

        while(l <= r):
            mid = l + (r-l)//2
            print("mid", mid)
            if self.canEatAll(piles, mid) <= h:
                k = mid
                r = mid - 1
            else:
                l = mid + 1
        return k
    

    def canEatAll(self, piles, k):

        hr = 0
        
        for b in piles:
            b = (b + k - 1)//k
            hr += b
        print("hr", hr)
        return hr
