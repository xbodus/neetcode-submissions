
class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)
        
    def decode(self, s: str) -> List[str]:
        decoded = []
        pointer = 0
        while pointer < len(s):
            hash_pos = s.index("#", pointer)
            word_len = int(s[pointer:hash_pos])
            pointer = hash_pos + 1
            decoded.append(s[pointer:pointer + word_len])
            pointer += word_len

        return decoded
