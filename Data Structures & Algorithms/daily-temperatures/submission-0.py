class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = collections.deque()
        arr = [0]*len(temperatures)

        for i in range(len(temperatures)):
            if st:
                temp, idx = st.pop()
                st.append([temp,idx]) 
                while temperatures[i] > temp:
                    arr[idx] = (i - idx)
                    if st:
                        temp, idx = st.pop()
                        if temperatures[i] > temp:
                            continue
                        else:
                            st.append([temp,idx])                       
                    else:
                        break
            st.append([temperatures[i],i])
        
        if st:
            temp, idx = st.pop()
            arr[idx] = 0
        
        return arr
            

            

