class BinarySearch:
    @staticmethod
    def search(list, client_to_find):
        
        n = len(list)      # n is the length of the list  
        first = 0
        last = n - 1
        middle = 0
        
        # keep looking until we find the client or the first and last are flipped
        while first <= last:
            middle = int( (first + last) / 2 )
            if list[middle] == client_to_find:
                return list[middle]
            else:
                # move the end of list based on the middle number
                if client_to_find < list[middle]:
                    last = middle - 1
                else:
                    first = middle + 1
                    
        # if we get this far, we did not find the record
        return None