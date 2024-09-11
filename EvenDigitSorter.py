class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        even_digit_count = 0  
        
        for i in nums:
            straw = str(i)
            counter = len(straw)
            if counter % 2 == 0:
                print(str(i) + " is an even digit sequence.")
                even_digit_count += 1
            else:
                print(str(i) + " is not an even digit sequence.")
        
        return even_digit_count  

input_list = input("Enter numbers separated by commas: ").split(',')
digit_list = [int(num) for num in input_list]  # Convert the input string list to integers

solution = Solution()
result = solution.findNumbers(digit_list)

print(f"Total numbers with even digits: {result}")
