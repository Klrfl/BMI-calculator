# taruh kalkulator dalam fungsi

def BMICalc():

  # input
  nama = input("namamu siapa? ")
  berat = float(input("masukkan berat (kg): "))
  tinggi = float(input("masukkan tinggi (cm): ")) / 100

  bmi = round(berat / tinggi**2, 1)

  print(f"\n{nama}, BMI kamu adalah {bmi}.")

  if bmi < 16:
    print("kamu kekurangan berat badan. Banget.")
  elif 16 < bmi < 16.9:
    print("kamu sedikit kekurangan badan.")
  elif 17 < bmi < 18.4:
    print("Dikit lagi berat badanmu normal. Makan yang banyak ya.")

  elif 18.5 < bmi < 24.9:
    print("BMI kamu normal. Pertahankan ya.")
  elif 25 < bmi < 29.9:
    print("kamu sedikit kelebihan berat badan.")
  elif 30 < bmi < 34.9:
    print("kamu masuk obesitas kelas 1.")
  elif 35 < bmi < 39.9:
    print("kamu masuk obesitas kelas 2.")
  elif bmi > 40:
    print("kamu masuk obesitas kelas 2.")

  ulang = int(input("mau ngitung lagi ga? 1 = ya, 0 = tidak "))
  if ulang:
    print("mengulang kalkulasi.. \n")
    BMICalc()
  else:
    print("ok")

BMICalc()