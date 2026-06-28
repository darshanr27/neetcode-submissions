class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_ls = []
        for s in strs:
            encoded_ls.append(str(len(s)) + '#' + s)
        
        return ''.join(encoded_ls)

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_ls = []
        while i < len(s):
            j = s.find('#', i)
            s_len = int(s[i:j])
            decoded_word = s[j+1:j+1+s_len]
            decoded_ls.append(decoded_word)
            i = j + 1 + s_len
        
        return decoded_ls