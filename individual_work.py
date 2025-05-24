import json

employees = []

def save_data():
    with open('employees.json', 'w') as f:
        json.dump(employees, f)

def load_data():
    try:
        with open('employees.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def show_menu():
    print("""
1. Yeni əməkdaş əlavə et
2. Əməkdaşlara bax
3. Əməkdaş axtar
4. Əməkdaşı redaktə et
5. Əməkdaşı sil
6. Bütün məlumatları sil
7. Yardım
8. Çıxış
""")

def add_employee():
    while True:
        new_id = input("ID daxil edin: ")
        if any(emp['id'] == new_id for emp in employees):
            print("Bu ID artıq mövcuddur, başqa ID daxil edin.")
        else:
            break
    emp = {
        'id': new_id,
        'name': input("Ad daxil edin: "),
        'position': input("Vəzifə daxil edin: ")
    }
    employees.append(emp)
    print("Əməkdaş əlavə olundu.")

def view_employees():
    if not employees:
        print("Əməkdaş məlumatı yoxdur.")
    else:
        print(f"
Ümumi əməkdaş sayı: {len(employees)}")
        for emp in employees:
            print(f"ID: {emp['id']} | Ad: {emp['name']} | Vəzifə: {emp['position']}")

def search_employee():
    key = input("Axtarış üçün ID və ya Ad daxil edin: ").lower()
    found_emps = [emp for emp in employees if emp['id'] == key or emp['name'].lower() == key]
    if found_emps:
        for emp in found_emps:
            print(f"Tapıldı → ID: {emp['id']} | Ad: {emp['name']} | Vəzifə: {emp['position']}")
    else:
        print("Əməkdaş tapılmadı.")

def update_employee():
    update_id = input("Redaktə etmək istədiyiniz əməkdaşın ID-sini daxil edin: ")
    for emp in employees:
        if emp['id'] == update_id:
            emp['name'] = input("Yeni ad daxil edin: ")
            emp['position'] = input("Yeni vəzifə daxil edin: ")
            print("Əməkdaş məlumatları yeniləndi.")
            return
    print("Əməkdaş tapılmadı.")

def delete_employee():
    delete_id = input("Silmək istədiyiniz əməkdaşın ID-sini daxil edin: ")
    for i, emp in enumerate(employees):
        if emp['id'] == delete_id:
            employees.pop(i)
            print("Əməkdaş silindi.")
            return
    print("Əməkdaş tapılmadı.")

def clear_all_data():
    confirm = input("Bütün məlumatları silmək istəyirsiniz? (bəli/xeyr): ").lower()
    if confirm == 'bəli':
        employees.clear()
        print("Bütün əməkdaş məlumatları silindi.")
    else:
        print("Əməliyyat ləğv edildi.")

def show_help():
    print("""
Bu proqramda aşağıdakı funksiyalar mövcuddur:
1. Yeni əməkdaş əlavə etmək
2. Bütün əməkdaşlara baxmaq
3. ID və ya ada görə əməkdaş axtarışı
4. Əməkdaş məlumatlarını yeniləmək
5. Əməkdaş silmək
6. Bütün əməkdaş məlumatlarını silmək
7. Kömək menyusunu göstərmək
8. Proqramdan çıxmaq
""")

def main():
    global employees
    employees = load_data()
    print(f"Xoş gəlmisiniz - Ümumi əməkdaş sayı: {len(employees)}")

    while True:
        show_menu()
        choice = input("Seçiminizi daxil edin (1-8): ")
        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            update_employee()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            clear_all_data()
        elif choice == '7':
            show_help()
        elif choice == '8':
            save_data()
            print("Məlumat yadda saxlanıldı. Proqramdan çıxılır...")
            break
        else:
            print("Yanlış seçim etdiniz. Zəhmət olmasa 1-dən 8-ə qədər seçim edin.")

if __name__ == '__main__':
    main()
