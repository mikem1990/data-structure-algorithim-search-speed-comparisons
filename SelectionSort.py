class SelectionSort:

    @staticmethod
    def sort(list):
        num_records = len(list)
        for i in range(num_records - 1):
          
           # Find index of smallest remaining element
           index_smallest = i
           for j in range(i + 1, num_records):
          
              if list[j] < list[index_smallest]:
                 index_smallest = j
          
           # Swap list[i] and list[index_smallest]
           temp = list[i]
           list[i] = list[index_smallest]
           list[index_smallest] = temp