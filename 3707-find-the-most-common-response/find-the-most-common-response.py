class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        count = defaultdict(int)
        for daily in responses:
            for response in set(daily):
                count[response]+=1
        max_count = max(count.values())
        most_common = min(response for response,cnt in count.items() if cnt==max_count )
        return most_common