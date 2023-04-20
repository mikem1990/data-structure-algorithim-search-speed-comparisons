class MergeSort:

    @classmethod
    def sort(cls, list):
        num_records = len(list)
        # Initial call to merge_sort
        cls.merge_sort(list, 0, num_records - 1)
        
    @classmethod
    def merge_sort(cls, list, i, k):
        j = 0
    
        if i < k:
            j = (i + k) // 2  # Find the midpoint in the partition
    
            # Recursively sort left and right partitions
            cls.merge_sort(list, i, j)
            cls.merge_sort(list, j + 1, k)
                
            # Merge left and right partition in sorted order
            cls.merge(list, i, j, k)
        
    @classmethod
    def merge(cls, list, i, j, k):
        merged_size = k - i + 1               # Size of merged partition
        merged_list = [0] * merged_size    # Dynamically allocates temporary array
                                              # for merged list
        merge_pos = 0                         # Position to insert merged number
        left_pos = i                          # Initialize left partition position
        right_pos = j + 1                     # Initialize right partition position
       
        # Add smallest element from left or right partition to merged list
        while left_pos <= j and right_pos <= k:
            if list[left_pos] <= list[right_pos]:
                merged_list[merge_pos] = list[left_pos]
                left_pos += 1
            else:
                merged_list[merge_pos] = list[right_pos]
                right_pos += 1
            merge_pos = merge_pos + 1
       
        # If left partition is not empty, add remaining elements to merged list
        while left_pos <= j:
            merged_list[merge_pos] = list[left_pos]
            left_pos += 1
            merge_pos += 1
       
        # If right partition is not empty, add remaining elements to merged list
        while right_pos <= k:
            merged_list[merge_pos] = list[right_pos]
            right_pos = right_pos + 1
            merge_pos = merge_pos + 1
       
        # Copy merge number back to list
        for merge_pos in range(merged_size):
            list[i + merge_pos] = merged_list[merge_pos]