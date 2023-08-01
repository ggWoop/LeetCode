class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        # int를 기본 값으로 하는 defaultdict 생성
        result_dict = defaultdict(int)

        # nums1의 원소들을 순회하면서 defaultdict에 더하기
        for id, val in nums1:
            result_dict[id] += val

        # nums2의 원소들을 순회하면서 defaultdict에 더하기
        for id, val in nums2:
            result_dict[id] += val

        # defaultdict의 키-값 쌍을 정렬하여 결과 리스트 생성
        result = sorted(result_dict.items())

        return result