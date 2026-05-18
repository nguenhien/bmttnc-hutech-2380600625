def truy_cap_phan_tu(tuple_data):
   first_element = tuple_data[0]
   last_element = tuple_data[-1]
   return first_element, last_element

#Nhập danh sách số từ người dùng và xử lý chuỗi
input_tuple = eval(input("Nhập tuple (phân tách bởi dấu ,):"))
first, last = truy_cap_phan_tu(input_tuple)

print("Phần tử đầu tiên:", first)
print("Phần tử cuối cùng:", last)