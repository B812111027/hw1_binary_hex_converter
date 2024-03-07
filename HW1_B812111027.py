def decimal_to_binary(decimal_num):
    binary_num = ""
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_num = str(remainder) + binary_num
        decimal_num //= 2
    return binary_num if binary_num else "0"

def decimal_to_hexadecimal(decimal_num):
    hexadecimal_chars = "0123456789ABCDEF"
    hexadecimal_num = ""
    while decimal_num > 0:
        remainder = decimal_num % 16
        hexadecimal_num = hexadecimal_chars[remainder] + hexadecimal_num
        decimal_num //= 16
    return hexadecimal_num if hexadecimal_num else "0"

def main():
    decimal_num = int(input("請輸入一個十進位數字: "))
    binary_num = decimal_to_binary(decimal_num)
    hexadecimal_num = decimal_to_hexadecimal(decimal_num)
    
    print("十進位數字", decimal_num, "對應的二進位數字為:", binary_num)
    print("十進位數字", decimal_num, "對應的十六進位數字為:", hexadecimal_num)

if __name__ == "__main__":
    main()
