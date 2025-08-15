# คำสั่งรับคำข้อความ string ทางแป้นพิมพ์ ใช้ฟังก์ชัน input()
# ******ตัวแปร variable คือ ชื่อที่Dev ตั้งขึ้นมาเอง (ต้องเป็นไปตามกฎการตั้งชื่อ) เอาไว้เก็บข้อมูลที่เดกิดขึ้นในโปรแกรม

Fullname =  input('ป้อนชื่อ: ')
year_born = input('ป้อนปีเกิด พ.ศ.: ')
print('------------------------')
print(F'สวัสดีคุณ{Fullname}')
print(F'คุณเกิดในปี {year_born} ตอนนี้คุณอายุ {2568 - int(year_born)}')
# ใช้ ,
print("F'คุณ {Fullname}",year_born,'ตอนนี้คุณอายุ',2568 - int(year_born))
# ใช้ + 
print("F'คุณ {fullname}' +str(year_born)+'ตอนนี้คุณอายุ'+ str(year_born))
# ใช้ format
print("F'คุณ {Fullname}",year_born,'ตอนนี้คุณอายุ',2568 - int(year_born))