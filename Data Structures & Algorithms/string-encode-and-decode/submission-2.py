class Solution:
    def encode(self, strs: List[str]) -> str:
        arr = []
        for st in strs:
            arr.append(f"{len(st)}:{st}")
        return ''.join(arr)

    def decode(self, s: str) -> List[str]:
        arr = []
        pointer = 0
        while pointer < len(s):
            print(s)
            delim_index = s.index(":", pointer)
            print(f"delimieter index: {delim_index}")
            len_as_str = s[pointer:delim_index]
            print(f"len as str: {len_as_str}")
            len_of_length_str = len(len_as_str)
            start_of_string = delim_index + 1
            print(f"start of string {start_of_string}")
            end_of_string = start_of_string + int(len_as_str)  
            print(f"end of string {end_of_string}")
            string = s[start_of_string : end_of_string]
            arr.append(string)
            print(arr)
            pointer = end_of_string
            print(pointer)
        return arr
