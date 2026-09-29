def konversi_suhu(value, unit):
    "Mengonversi suhu antara Celsius dan Fahrenheit"
    if unit == 'C':
        return (value * 9 / 5) + 32
    elif unit == 'F':
        return (value - 32) * 5 / 9

value = float(input("Masukkan suhu: "))
unit = input("Masukkan satuan(C/F): ")

hasil = konversi_suhu(value, unit)

print("Hasil:", hasil) 