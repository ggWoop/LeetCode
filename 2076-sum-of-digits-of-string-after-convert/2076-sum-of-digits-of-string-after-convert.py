class Solution:
    def getLucky(self, s: str, k: int) -> int:

        
        count = 0

        converted_num = "".join([str(ord(c)-96)for c in s])
        
        for i in range(k):
            count = sum(int(digit) for digit in str(converted_num))  # 정수의 자릿수 합계 계산
            converted_num = count  # 다음 변환을 위해 변환된 숫자 업데이트
            
        return count

            
            
            






