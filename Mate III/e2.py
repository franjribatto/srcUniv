print("Ingrese el dia de nacimiento (dd/mm/aaaa): ")

dd = int(input())
mm = int(input())
aaaa = int(input())

mm_d = {1 :"Verano",
        2 :"Verano",
        3 :"Verano",
        4 :"Otoño",
        5 :"Otoño",
        6 :"Invierno",
        7 :"Invierno",
        8 :"Invierno",
        9 :"Invierno",
        10 :"Primavera",
        11 :"Primavera",
        12 :"Primavera"}

if mm in mm_d:
  print("Su hijo nacio en: ")
  print(mm_d[mm])
