import sys

def main():
    print("Versi Python %.5s"%sys.version)
    print("Konversi Suhu (Fahrenheit ke Celcius)\n")

    F = float(input("Masukkan Suhu (Fahrenheit): "))
    C = 5 * (F - 32) / 9
    print("Fahrenheit\t: %.2f" % (F))
    print("Celcius\t: %.2f" % (C))
if __name__ == '__main__':
    main()