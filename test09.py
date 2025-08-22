# สร้างโปรแกรมคำนวณเงินเดือนสุทธิที่ต้องจ่ายหลังจากหักภาษีแล้ว 7% ของเงินเดือน  และหักค่าประกันสังคม 3% ของเงินเดือน
# โดยรับค่ารหัสพนักงาน ชื่อพนักงาน เงินเดือน ทางแป้นพิมพ์ และแสดงผลข้อมูลที่รับมา
# พร้อมกับรายละเอียดว่าต้องเสียภาษีกี่บาท หักค่าประกันสังคมกี่บาท และต้องจ่ายเงินเดือนสุทธิกี่บาท

print('+++++++++++++++++++++++')
print('โปรแกรมคำนวณเงินเดือน')
print('+++++++++++++++++++++++')
emp_code = input("ป้อนรหัสพนักงาน; ")
emp_name = input("ป้อนชื่อพนักงาน; ")
emp_salary = input("ป้อนเงินเดือน; ")
emp_tax = float(emp_salary) * 7 / 100 
insurance = float(emp_salary) * 3 / 100
emp_salary_not = float(emp_salary) - emp_tax - insurance
print(f'รหัส; {emp_code} ชื่อ; {emp_name} เงินเดือน; {emp_salary}')
print(f'ภาษี; {emp_tax} บาท')
print(f'ประกันสังคม; {insurance} บาท')
print(f'เงินเดือนสุทธิ; {emp_salary_not}บาท')
# ใช้ ,
print(f'รหัส; {emp_code}, ชื่อ; {emp_name}, เงินเดือน; {emp_salary}')
print(f'ภาษี; {emp_tax},บาท')
print(f'ประกันสังคม; {insurance},บาท')
print(f'เงินเดือนสุทธิ; {emp_salary_not},บาท')
# ใช้ +
print(f'รหัส'+str(emp_code)+'ชื่อ '+str(emp_name)+' เงินเดือน; '+str(emp_salary))
print(f'ภาษี'+str(emp_tax)+'บาท')
print(f'ประกันสังคม'+str(insurance)+'บาท')
print(f'เงินเดือนสุทธิ'+str(emp_salary_not)+'บาท')
# ใช้ format
print('รหัส {} ชื่อ {} เงินเดือน {}'.format(emp_code,emp_name,emp_salary))
print('ภาษี {} บาท'.format(emp_tax))
print('ประกันสังคม {} บาท'.format(insurance))
print('เงินเดือนสุทธิ {} บาท'.format(emp_salary_not))