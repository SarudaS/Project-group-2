# =====================================================
#  main.py — ศูนย์กลางของระบบ (งานของหัวหน้ากลุ่ม!)
#
#  เมนู 1 และ 2 เขียนให้ดูเป็นตัวอย่างแล้ว
#  หน้าที่ของหัวหน้า: เขียนเมนู 3-6 โดยเรียกใช้ฟังก์ชันที่เพื่อนเขียน
#  pattern เดียวกันทุกเมนู:  รับ input -> เรียกฟังก์ชัน -> print ผลลัพธ์
# =====================================================
from data import weapons_catalog
from personnel.add_member import add_member
from personnel.show_members import show_members
from personnel.search_member import search_member
from personnel.remove_member import remove_member
from weapon_shop.show_catalog import show_catalog
from weapon_shop.equip_item import equip_item
from missions.send_mission import send_mission

def main():
    while True:
        print("\n=== MAFIA MANAGEMENT SYSTEM ===")
        print("1. รับลูกน้องใหม่")
        print("2. ดูรายชื่อแก๊ง")
        print("3. ค้นหาประวัติ")
        print("4. สั่งเก็บลูกน้อง")
        print("5. คลังอาวุธ")
        print("6. ส่งไปทำภารกิจ")
        print("7. ออกจากระบบ")

        choice = input("เลือกคำสั่ง (1-7): ")

        # ---------- เมนู 1 (ตัวอย่าง เขียนให้ดูแล้ว) ----------
        if choice == '1':
            print("\n--- เพิ่มลูกน้องใหม่ ---")
            new_member = add_member()
            print(new_member)
            # name = input("ชื่อ: ")
            # age = int(input("อายุ: "))
            # power = int(input("ความโหด (1-10): "))
            # money = float(input("เงินส่วย: "))

            # new_member = add_member(name, age, power, money)

            # if new_member is None:
            #     print("!! add_member ยังไม่ถูกเขียน (ไปเขียนใน personnel/add_member.py)")
            # else:
            #     print(f"เพิ่ม {new_member['name']} ในตำแหน่ง {new_member['role']} เรียบร้อยแล้ว")
            
        # ---------- เมนู 2 (ตัวอย่าง เขียนให้ดูแล้ว) ----------
        elif choice == '2':
            print("\n--- รายชื่อลูกน้องทั้งหมด ---")
            show_members()

        # ---------- เมนู 3 (TODO) ----------
        elif choice == '3':
            print("\n--- ค้นหาประวัติ ---")
            target_name = input("ชื่อ: ")
            result = search_member(target_name)
            
                # search_member(name)
            if result is not None:
                print(f"{result['name']}, {result['age']}, {result['money']}, {result['equipment']}")
            else:
                print("ไม่พบชื่อในระบบ")

            name = input("ชื่อ: ")
            member = search_member(name)
            if member is not None:
                print(f"{member['name']}, {member['power']}, {member['money']}, {member['equipment']}")
            else:
                print("ไม่พบชื่อในระบบ")


        # ---------- เมนู 4 (TODO) ----------
        elif choice == '4':
            print("\n--- สั่งเก็บลูกน้อง ---")

            remove_name = remove_member()
            # print(remove_name)

            # name = input()
            # remove_member(name)
            if remove_name == True:
                print("สั่งเก็บเรียบร้อย")
                
            elif remove_name == False:
                print("ไม่พบชื่อในระบบ")
            else:
                print("!! เมนูนี้ยังไม่ถูกเชื่อม")
            # 1) รับชื่อคนที่ต้องการลบด้วย input()
            # 2) เรียก remove_member(ชื่อ) แล้วเก็บผลไว้ (ได้ True หรือ False)
            # 3) True  -> print สั่งเก็บเรียบร้อย
            #    False -> print "ไม่พบชื่อในระบบ"


        # ---------- เมนู 5 (TODO) ----------
        elif choice == '5':
            print("\n=== คลังอาวุธ ===")
            show_catalog()
            weapon_search = input("รหัสอาวุธ: ") #รับค่ารหัสของอาวุธ
            weapon = weapons_catalog.get(weapon_search) 
            #.get(weapon_search) คือการหาค่าที่เรารับมากับ dict:weapon_catalog 
            if weapon == None:
                print("ไม่มีสินค้านี้ในระบบ")
                break
            name = input("ชื่อลูกน้อง: ")
            member = search_member(name)
            #เรียกใช้ฟังก์ชัน search_member ที่มาจากไฟล์ search_member.py
            if member == None:
                print("ไม่พบรายชื่อลูกน้องคนนี้")
                break
            result = equip_item(member, weapon)
            # result = มีค่าของ member and weapon ที่เรารับมา เพื่อนำไปใช้ในฟังก์ชัน equip_item
            print(result["message"])
            if result["status"] == True:
                print(member["power"])


        # ---------- เมนู 6 (TODO ของหัวหน้า — OPTIONAL) ----------
        # elif choice == '6':
        #     print("\n--- ส่งไปทำภารกิจ ---")
        #     name = input()
        #     if name is not  search_member():
        #         print("ไม่พบรายชื่อลูกน้องคนนี้ในระบบ")
        #     else:
        #         send_mission(name)
                
            # 1) รับชื่อลูกน้อง แล้วหาคนด้วย search_member(ชื่อ)
            #    ถ้าได้ None -> print "ไม่พบรายชื่อลูกน้องคนนี้ในระบบ" (จบเมนูนี้เลย)
            # 2) เรียก send_mission(คน) แล้วเก็บผลไว้ (ได้ dict)
            # 3) ถ้าผล["status"] เป็น True -> print ภารกิจสำเร็จ + เงินรางวัล + ยอดเงินปัจจุบัน
            #    ถ้าเป็น False -> เรียก remove_member(คน["name"]) แล้ว print ภารกิจล้มเหลว ถูกลบออกจากแฟมิลี่
            # print("!! เมนูนี้ยังไม่ถูกเชื่อม")

        elif choice == '7':
            print("ปิดระบบ...")
            break
        else:
            print("คำสั่งไม่ถูกต้อง")

if __name__ == "__main__":
    main()
