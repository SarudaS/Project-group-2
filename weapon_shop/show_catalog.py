# =====================================================
#  weapon_shop/show_catalog.py — คนรับผิดชอบ: ______________________
#  หน้าที่: แสดงรายการอาวุธทั้งหมดที่มีขาย
# =====================================================
from data import weapons_catalog

def show_catalog():
#   - print อาวุธทุกชิ้นใน weapons_catalog บรรทัดละชิ้น (รหัส, ชื่อ, ราคา, พลังโบนัส)
    # TODO: เขียนโค้ดตรงนี้
    print(weapons_catalog)


# ทดสอบเฉพาะไฟล์ตัวเอง: พิมพ์  python -m weapon_shop.show_catalog
if __name__ == "__main__":
    show_catalog()   # ต้องเห็นอาวุธครบ 3 ชิ้น
