_list = ['abc', 'hello', 'python', 'hi', 'code']

n = int(input("Nhập n: "))

ket_qua = []

for x in _list:
    if len(x) > n:
        ket_qua.append(x)

print("Các từ có độ dài > n:", ket_qua)