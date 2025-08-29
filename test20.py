# โปรแกรมแสดงข้อความต้อนรับนักศึกษา โดยรับชื่อ และชั้นปีทางแป้นพิมพ์แล้วแสดงข้อความต้อนรับ ดังนี้
# 	กรณีป้อนชั้นปี 1 แสดงข้อความ "Welcome Freshman"
# 	กรณีป้อนชั้นปี 2 แสดงข้อความ "Welcome Sophomore"
# 	กรณีป้อนชั้นปี 3 แสดงข้อความ "Welcome Junior"
# 	กรณีป้อนชั้นปี 4 แสดงข้อความ "Welcome Senior
# 	กรณีป้อน ปีอื่นๆ  แสดงข้อความ "Oh, no ...."

print('.............................')
print('โปรแกรมแสดงข้อความต้อนรับนักศึกษา')
print('.............................')
your_name = input('ป้อนชื่อ : ')
your_year = int(input('ป้อนชั้นปี : '))
print('.............................')

if your_year == 1:
    print(f'Welcome Freshman {your_name}')
elif your_year == 2:
    print(f'Welcome Sophomore {your_name}')
elif your_year == 3:
    print(f'Welcome Junior {your_name}')
elif your_year == 4:
    print(f'Welcome Senior {your_name}')
else:
    print('Oh, no ...')

print('ยินดีต้อนรับครับ')