def tao_tuble_tu_list(lst):
    return tuple(lst)   

input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

my_tuble = tao_tuble_tu_list(numbers)
print("list: ", numbers)
print("tuple từ list: ", my_tuble)