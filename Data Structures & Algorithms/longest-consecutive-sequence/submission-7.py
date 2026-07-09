class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 0 :
            return 0

        # convert nums to set and reverse to have reversed, sorted, and unique list of ints for 0(1) lookups with .pop()
        nums: list[int] = sorted(set(nums), reverse=True)
        print(nums)

        # Store consecutive chains. Key increments when current chain doesn't have anymore consecutive integers
        chains: dict[int, list[int]] = {}
        
        current_key: int = 1
        for _ in range(len(nums)):
            # 1. Pop last value from reversed sorted list (should be current lowest)
            n = nums.pop()

            # 2. Set default list is doesn't exist
            if current_key not in chains:
                chains[current_key] = []
                chains[current_key].append(n)
                continue

            # 3. Check if next int is one more than current value 
            if n - 1 == chains[current_key][-1]:
                chains[current_key].append(n)
            else:
                current_key += 1
                chains[current_key] = []
                chains[current_key].append(n)
            
                

        print(chains)

        # Find the list with the longest chain and return the length     
        longest_chain: str = max(chains, key=lambda k: len(chains[k])) 
        return len(chains[longest_chain])