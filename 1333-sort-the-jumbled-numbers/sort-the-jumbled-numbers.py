class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        def mapped_sort_key(num: int, mapping: List[int]) -> int:
            # Convert num to its mapped value
            mapped_num = ""
            for digit in str(num):
                mapped_num += str(mapping[int(digit)])
            return int(mapped_num)
        
        mapping_dict = {i: mapping[i] for i in range(10)}
        return sorted(nums, key=lambda x: mapped_sort_key(x, mapping_dict))
            