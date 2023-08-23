#!/usr/bin/python3
"""
This module contains a method that determines if a given data set
is valid UTF-8 encoding.
"""

def validUTF8(data):
    num_bytes_to_check = 0
    
    for num in data:
        # Check if this byte is the start of a character
        if num_bytes_to_check == 0:
            if (num >> 7) == 0b0:
                num_bytes_to_check = 0
            elif (num >> 5) == 0b110:
                num_bytes_to_check = 1
            elif (num >> 4) == 0b1110:
                num_bytes_to_check = 2
            elif (num >> 3) == 0b11110:
                num_bytes_to_check = 3
            else:
                return False
        else:
            # Check if this byte is a continuation byte
            if (num >> 6) != 0b10:
                return False
            num_bytes_to_check -= 1
        
    # Check if all characters were validated
    return num_bytes_to_check == 0

# Test cases
data1 = [65]
print(validUTF8(data1))  # Output: True

data2 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data2))  # Output: True

data3 = [229, 65, 127, 256]
print(validUTF8(data3))  # Output: False
