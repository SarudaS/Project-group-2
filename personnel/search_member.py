# =====================================================
#  personnel/search_member.py — คนรับผิดชอบ: Napat Sakpradupkul
#  หน้าที่: ค้นหาลูกน้องจากชื่อ
# =====================================================
from data import family_members

def search_member(target_name):
    for N in family_members :
        if target_name.lower() == N ["name"].lower()  :
            return N    
    return None
        
#   - หาคนใน family_members ที่ชื่อตรงกับ target_name (ไม่สนตัวพิมพ์ใหญ่/เล็ก)
#   - เจอ -> return dict ของคนนั้น | ไม่เจอ -> return None
    # TODO: เขียนโค้ดตรงนี้

# ทดสอบเฉพาะไฟล์ตัวเอง: พิมพ์  python -m personnel.search_member
if __name__ == "__main__":
    print(search_member("tony"))        # ต้องได้ dict ของ Tony (พิมพ์เล็กก็ต้องเจอ)
    print(search_member("ไม่มีคนนี้"))    # ต้องได้ None


