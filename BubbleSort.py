class BubbleSort:

    @staticmethod
    def sort(list):
        num_records = len(list)
        for i in range( num_records - 1 ):
            for j in range( num_records - i - 1 ):
                if list[j] > list[j+1]:
                    # flip them!
                    temp = list[j]
                    list[j] = list[j+1]
                    list[j+1] = temp