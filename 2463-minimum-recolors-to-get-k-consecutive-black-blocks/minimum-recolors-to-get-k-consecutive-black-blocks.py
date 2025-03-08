class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left =0
        n_whites=0
        n_recolors=float('inf')
        for right in range(len(blocks)):
            if blocks[right]=='W':
                n_whites+=1
            if right-left+1==k:
                n_recolors=min(n_recolors,n_whites)
                if blocks[left]=='W':
                    n_whites-=1
                left+=1
        return n_recolors