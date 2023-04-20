class InsertionSort:

    @staticmethod
    def sort(list):
        num_records = len(list)
        for i in range(1, num_records):
            j = i
        
            # Insert list[i] into sorted part 
            # stopping once list[i] in correct position
            while j > 0 and list[j] < list[j - 1]:
                # Swap numbers[j] and numbers[j - 1]
                temp = list[j]
                list[j] = list[j - 1]
                list[j - 1] = temp
                j -= 1