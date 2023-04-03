def binary_to_hex(binary_num):
    # Check if input is a valid binary string
    if not all(c in '01' for c in binary_num):
        return "Invalid binary number"
    
    # Add padding to the binary string to ensure it's a multiple of 4
    binary_num = binary_num.zfill((len(binary_num) + 3) // 4 * 4)
    
    # Split the binary string into groups of 4 bits
    binary_groups = [binary_num[i:i+4] for i in range(0, len(binary_num), 4)]
    
    # Map each binary group to its hexadecimal equivalent
    hex_groups = [hex(int(bg, 2))[2:].upper() for bg in binary_groups]
    
    # Join the hexadecimal groups to form the final result
    hex_num = ''.join(hex_groups)
    
    return hex_num
    

# Example usage
binary_num = input("Enter a binary number: ")
hex_num = binary_to_hex(binary_num)

print("The hexadecimal equivalent of", binary_num, "is", hex_num)
