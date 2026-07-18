# =====================================================
#  personnel/show_members.py — คนรับผิดชอบ: ______________________
#  หน้าที่: แสดงรายชื่อลูกน้องทั้งหมดในแฟมิลี่
# =====================================================
from data import family_members

def show_members():
    for N in family_members :
        N ["name"]
        print(N)
#   - print ข้อมูลลูกน้องทุกคนใน family_members บรรทัดละคน (ชื่อ, ตำแหน่ง, ความโหด, อาวุธ)
    # TODO: เขียนโค้ดตรงนี้


# ทดสอบเฉพาะไฟล์ตัวเอง: พิมพ์  python -m personnel.show_members
if __name__ == "__main__":
    show_members()   # ต้องเห็น Tony กับ Luigi คนละบรรทัด
