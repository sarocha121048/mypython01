# ปรแกรมตรวจสอบรถว่าผ่านเกณฑ์ของการตรวจสอบค่าคาร์บอนไดซ์ออกไซน์หรือ 
# โดยหากค่าคาร์บอนไดซ์ออกไซน์มีค่าเกินกว่า 678.55 ให้แสดงข้อความว่า “ไม่ผ่าน”  หากน้อยกว่า 678.55 
# ให้แสดงข้อความ “ผ่าน” โดยให้รับชื่อเจ้าของ ทะเบียนรถ และปริมาณก๊าซคาร์บอนไดซ์ออกไซน์ที่วัดได้ ทางแป้นพิมพ์

# หาฟีเจอร์การทำงานของโปรแกรมจากโจทย์
# รับค่าชื่อเจ้าของรถ ทะเบียนรถ และปริมาณก๊าซคาร์บอนไดออกไซน์ที่วัดได้
# การตรวจสอบก๊าซ 
# การแสดงผล
# การแสดงชื่อโปรแกรม

def show_program_name() :
    print('ตรวจสอบสภาพรถ')
   
def input_data() :
    car_owner = input('ป้อนชื่อเจ้าของรถ')
    car_number = input('ป้อนทะเบียนรถ')
    car_carbon = float(input('ป้อนปริมาณก๊าซคาร์บอนไดออกไซน์'))
    return car_owner, car_number, car_carbon
def show_result(car_owner, car_number, car_carbon, result) :
    print(f'คุณ{car_owner}ทะเบียนรถ{car_number}')
    print(f'ก๊าซ ที่วัดได้{car_carbon}สรุป{result}')

def check_gas(car_owner, car_number, car_carbon) :
    if car_carbon > 678.55 :
        show_result(car_owner, car_number, car_carbon, 'ไม่ผ่าน')
    else :
        show_result(car_owner, car_number, car_carbon, 'ผ่าน')

def show_pa() :
        print('..............')

show_pa()
show_program_name()
show_pa()
car_owner, car_number, car_carbon, =  input_data() 
show_pa()
check_gas(car_owner, car_number, car_carbon)
show_pa()
    
