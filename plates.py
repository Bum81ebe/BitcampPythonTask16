plate = ""

def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    digit_count = 0
    for char in plate:
        if char.isdigit():
            digit_count += 1
        elif not char.isalpha():
            return False
    if plate[0:2].isalpha() and plate[-2:].isdigit() and int(plate[-2]) != 0 and len(plate)>= 0 and len(plate)<=6 and digit_count == 2:
        return True
    else:
        return False

main()
