# คำสั่งรับคำข้อความ string ทางแป้นพิมพ์ ใช้ฟังก์ชัน input()
# ******ตัวแปร variable คือ ชื่อที่Dev ตั้งขึ้นมาเอง (ต้องเป็นไปตามกฎการตั้งชื่อ) เอาไว้เก็บข้อมูลที่เดกิดขึ้นในโปรแกรม

Fullname =  input('ป้อนชื่อ: ')
year_born = input('ป้อนปีเกิด พ.ศ.: ')
print('------------------------')
print(F'สวัสดีคุณ{Fullname}')
print(F'คุณเกิดในปี {year_born} ตอนนี้คุณอายุ {2568 - int(year_born)}')
# ใช้ ,
print('คุณ',Fullname)'ตอนนี้คุณอายุ',2568 - int(ัyear_born))
# ใช้ + 
print('สวัสดีคุณ '+ fullname)
print('คุณเกิดในปี '+ year_born + ' ตอนนี้คุณอายุ '+ str(2568 - int(year_bor)

# ใช้ format
print(f'สวัสดีคุณ '+ {fullname})
print(f'คุณเกิดในปี {year_born} ตอนนี้คุณอายุ {2568 - int(year_born)}') '+ {fullname})

# ใช้ f+string
print("สวัสดีคุณ{}".format(Fullname))
print("คุณเกิดในปี{} ตอนนี้คุณอายุ{}".format(year_born,2568 - int(year_born)))