import time

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)


def add_nums(n1, n2):
    """Toplama işlemini yapan fonksiyon"""
    return n1 + n2


def sub_nums(n1, n2):
    """Çıkarma işlemini yapan fonksiyon"""
    return n1 - n2


def mul_nums(n1, n2):
    """Çarpma işlemini yapan fonksiyon"""
    return n1 * n2


def div_nums(n1, n2):
    """Bölme işlemini yapan fonksiyon"""
    return n1 / n2


first_number = 0
second_number = 0
oper = ""
choose = ""
check = 0
result = ""

while True:
    if check == 0:
        first_number = float(input("Birinci sayıyı giriniz: "))

    print("+\n-\n*\n/")
    oper = input("Hangi işlemi yapmak istiyorsunuz?: ")
    second_number = float(input("İkinci sayıyı giriniz: "))

    if oper == "+":
        result = add_nums(first_number, second_number)
    elif oper == "-":
        result = sub_nums(first_number, second_number)
    elif oper == "*":
        result = mul_nums(first_number, second_number)
    elif oper == "/":
        try:
            result = div_nums(first_number, second_number)
        except ZeroDivisionError:
            print("Bir sayıyı 0'a bölemezsiniz. Hesap makinesi sıfırlanıyor...")
            time.sleep(1)
            print("\n\n\n\n")
            result = "HATA!"
    else:
        print("Tanımsız işlem girdiniz. Hesap makinesi sıfırlanıyor...")
        result = "HATA!"
        time.sleep(1)
        print("\n\n\n\n")


    if result != "HATA!":

        if first_number % int(first_number) == 0:
            first_number = int(first_number)

        if second_number % int(second_number) == 0:
            second_number = int(second_number)

        if result % int(result) == 0:
            result = int(result)

        print(f"{first_number} {oper} {second_number} = {result}")
        choose = input(f"{result} ile işleme devam etmek için 'e'ye basınız. "
                       f"Yeni hesaplamaya başlamak için 'h'ye basınız: ")

    if choose == "e" or choose == "E":
        check = 1
        first_number = result

    elif choose == "h" or choose == "H" or result == "HATA!":
        check = 0

    else:
        print("Hesap makinesinden çıkılıyor...")
        time.sleep(0.5)
        break
