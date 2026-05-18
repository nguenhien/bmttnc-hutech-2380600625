print("Nhập thông tin người dùng (Nhập 'done' để kết thúc):")
line =  []
while True:
    line = input()
    if line.lower() == 'done':
        break
    line.append(line)
print("\nCac dòng đã nhập sau khi chuyển thành chữ in hoa:")
for i in line:
    print(i.upper())