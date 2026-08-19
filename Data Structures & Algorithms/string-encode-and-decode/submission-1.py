from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for s in strs:
            length = len(s)
            encoded_string += str(length).zfill(4) + s

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            # First 4 characters = length
            length = int(s[i:i + 4])

            # Move past the 4-digit length
            i += 4

            # Read exactly `length` characters
            decoded.append(s[i:i + length])

            # Move past the string
            i += length

        return decoded
