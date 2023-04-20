class LinearSearch:
    @staticmethod
    def search(list, client_to_find):
        n = len(list)             # number of elements in the list
        
        # step through the records one at a time
        for i in range( n ):
            if list[i] == client_to_find:
                # we found the item, so return it
                return list[i]
            
        # if we get this far, we did not find the record
        return None