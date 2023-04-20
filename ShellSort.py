class ShellSort:

    @staticmethod
    def sort(list):
        num_records = len(list)
        
        # keep cutting the gap size in half as an integer -- using //
        gap = num_records // 2;
        while gap > 0:
            for i in range(gap, num_records):
                temp = list[i]
                j = i;
                
                while j >= gap and temp < list[j - gap]:
                    list[j] = list[j - gap]
                    j -= gap;
                
                list[j] = temp
                
            # cut gap in half as an integer -- using //
            gap = gap // 2