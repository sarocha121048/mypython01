# 3. no parameter have return
'''
def func_name() :
    คำสั่ง
    คำสั่ง
    ...
    return ค่าที่ต้องการส่งกลับ'''
...
def showhello() :
    
    print('^o^')
    print('wow')
    
    return 'hello...'
def funA() :
    print('hi...')
    return 'T_T', 999
print(showhello())

data = showhello()
print(data)

info1, info2 = funA()
print(info1)
print(info2)