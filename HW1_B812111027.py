def decimal_to_binary(decimal_num):
    binary_num = bin(decimal_num)
    return binary_num[2:]

def decimal_to_hexadecimal(decimal_num):
    hexadecimal_num = hex(decimal_num)
    return hexadecimal_num[2:]

def main():
    decimal_num = int(input("請輸入一個十進位數字: "))
    binary_num = decimal_to_binary(decimal_num)
    hexadecimal_num = decimal_to_hexadecimal(decimal_num)
    
    print("十進位數字", decimal_num, "對應的二進位數字為:", binary_num)
    print("十進位數字", decimal_num, "對應的十六進位數字為:", hexadecimal_num)

if __name__ == "__main__":
    main()
