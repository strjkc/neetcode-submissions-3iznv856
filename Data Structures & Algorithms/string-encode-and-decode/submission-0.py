class Solution:
    def encode(self, strs: List[str]) -> str:
        arr = []
        for st in strs:
            arr.append(f"{len(st)}:{st}")
        return ''.join(arr)
        #5:Hello5:World
    def decode(self, s: str) -> List[str]:
        arr = []
        while s:
            print(s)
            delim_index = s.index(":")
            len_as_str = s[:s.index(":")]
            print(delim_index)
            len_of_length_str = len(len_as_str)
            start_of_string = delim_index + 1
            end_of_string = start_of_string + int(len_as_str)  
            string = s[start_of_string : end_of_string]
            arr.append(string)
            print(arr)
            s = s[end_of_string:]
        return arr
