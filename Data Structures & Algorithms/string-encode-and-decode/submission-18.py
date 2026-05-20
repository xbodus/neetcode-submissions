
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
            word_len = 0
            try:
                length = ""
                for x in range(pointer, len(s)):
                    if s[x] == "#":
                        pointer += 1
                        break
                    length += s[x]
                    pointer += 1

                word_len = int(length)

                if word_len == 0:
                    decoded.append("")
                    continue
                
                decoded.append(s[pointer: pointer + word_len])
                pointer += word_len
            except ValueError as e:
                pointer += 1

        return decoded
