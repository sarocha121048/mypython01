# คำสั่ง break, continue
# break ใน loop ทำงานเมื่อใดจบ loop ทันที
# continue ใน loop ทำงานเมื่อใดจบ loop แค่รอบนั้นทันที แล้วให้ไปรอบถัดไปเลย

for aa in range(5) :
    if aa == 2 :
        break
    print(aa, 'Hi...')

print('++++++++++++++++++++++')
for aa in range(5) :
    if aa == 2 :
        continue
    print(aa, 'Hi...') 