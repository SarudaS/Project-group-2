# =====================================================
#  personnel/add_member.py — คนรับผิดชอบ: ______________________
#  หน้าที่: รับข้อมูลลูกน้องใหม่ สร้างเป็น dict แล้วเพิ่มเข้าลิสต์แฟมิลี่
# =====================================================
from data import family_members

def add_member(name, age, power, money,role,equipment):
 
    name = input("ชื่อ: ")
    age = int(input("อายุ: "))
    role = "Slave"
    power = int(input("ความโหด (1-10): "))
    money = float(input("เงินส่วย: "))
    equipment = input("อุปกรณ์: ")

    new_member = {
        "name" : name,
        "age" : age,
        "role" : role,
        "power" : 0,
        "money" : 0,
        "equipment" : equipment,
    }

    if power >= 8 :
        new_member["role"] = "Hitman"
        new_member["power"] = power
        
    elif money >= 1000000 :
        new_member["role"] = "Sponsor"
        new_member["money"] = money

    if equipment == "":
        new_member["equipment"] = "ไม่มี"

    family_members.append(new_member)
    
    return(add_member)   # ต้องเห็น Vito ต่อท้ายลิสต์ และ role เป็น Hitman



# ทดสอบเฉพาะไฟล์ตัวเอง: พิมพ์  python -m personnel.add_member
if __name__ == "__main__":
    
    name = input("ชื่อ: ")
    age = int(input("อายุ: "))
    role = "Slave"
    power = int(input("ความโหด (1-10): "))
    money = float(input("เงินส่วย: "))
    equipment = input("อุปกรณ์: ")

    new_member = {
        "name" : name,
        "age" : age,
        "role" : role,
        "power" : 0,
        "money" : 0,
        "equipment" : equipment,
    }

    if power >= 8 :
        new_member["role"] = "Hitman"
        new_member["power"] = power
        
    elif money >= 1000000 :
        new_member["role"] = "Sponsor"
        new_member["money"] = money

    if equipment == "":
        new_member["equipment"] = "ไม่มี"

    family_members.append(new_member)
    
    print(family_members)   # ต้องเห็น Vito ต่อท้ายลิสต์ และ role เป็น Hitman
