def dec_to_bin(number):
    result = ''
    if number == 1:
        result += str(number)
        return result
    else:
        result += str(number % 2)
        dec_to_bin(number // 2)
        return result
    

if __name__ == '__main__':
    print(dec_to_bin(10))  # 1010
    print(dec_to_bin(5))   # 101
    print(dec_to_bin(50))  # 110010