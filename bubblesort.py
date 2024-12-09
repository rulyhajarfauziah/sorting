data=[17,4,10,2,7,9,27,6,33]
print("data sebelum diurutkan:",data)
banyak_data= len(data)
for i in range(banyak_data):
    for j in range(banyak_data-1):
        if data[j]>data[j+1]:
            temp=data[j]
            data[j]=data[j+1]
            data[j+1]=temp
print("data setelah diurutkan",data)
