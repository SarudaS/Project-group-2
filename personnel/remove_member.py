# =====================================================
#  personnel/remove_member.py — คนรับผิดชอบ: ______________________
#  หน้าที่: ลบลูกน้องออกจากแฟมิลี่ตามชื่อ
# =====================================================
from data import family_members

def remove_member():
    target_name = input("ลบชื่อ: ")
    for remove_name in family_members :
        if remove_name["name"].lower() == target_name.lower():
            family_members.remove(remove_name)
            return True
    return False
        


# ทดสอบเฉพาะไฟล์ตัวเอง: พิมพ์  python -m personnel.remove_member
if __name__ == "__main__":
    target_name = input("ลบชื่อ: ").lower()
    for remove_name in family_members :
    
        if remove_name["name"].lower() == target_name:
            family_members.remove(remove_name)
        
        
print(family_members)

        


        
    

