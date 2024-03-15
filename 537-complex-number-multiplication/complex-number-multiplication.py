class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        
        def extract_parts(num):
            real, imag = num.split('+')
            return int(real), int(imag[:-1])
        
        def format_result(real, imag):
            return f"{real}+{imag}i"
        
        real1, imag1 = extract_parts(num1)
        real2, imag2 = extract_parts(num2)
        
        real_result = real1 * real2 - imag1 * imag2
        imag_result = real1 * imag2 + real2 * imag1
        
        return format_result(real_result, imag_result)