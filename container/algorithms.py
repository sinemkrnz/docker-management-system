class algorithms:

    def bubble_sort(self, nums):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    swapped = True
        return nums

    def selection_sort(self, nums):
        for i in range(len(nums)):
            lowest_value_index = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[lowest_value_index]:
                    lowest_value_index = j
            nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
        return nums

    def insertion_sort(self,nums):
        for i in range(1, len(nums)):
            item_to_insert = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > item_to_insert:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = item_to_insert
        return nums