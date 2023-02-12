import os
from docxtpl import DocxTemplate
import random

main_path = ""
temppath = "wanted/"
template_path = os.path.join(main_path, "TEMPLATE_wanted.docx")
template = DocxTemplate(template_path)

detective_1name = [
    "John",
    "Michael",
    "Joshua",
    "Matthew",
    "Adam",
    "Jacob",
    "Jackson",
    "Daniel",
    "Christopher",
    "Ethan",
    "Joseph",
]
detective_2name = [
    "Smith",
    "Johnson",
    "Garcia",
    "Williams",
    "Brown",
    "Rodriguez",
    "Miller",
    "Davis",
    "Wilson",
    "Anderson",
    "Perez",
]
detective_number = [
    "1-328-555-0167",
    "1-346-555-0186",
    "1-611-555-0184",
    "1-346-555-0183",
    "1-328-555-0177",
    "1-611-555-0126",
]
detective1_badge = random.randint(13333, 99999)
detective2_badge = random.randint(13333, 99999)

detective_1 = random.sample(detective_1name, k=2)
detective1_1 = detective_1[0]
detective2_1 = detective_1[1]
detective_2 = random.sample(detective_2name, k=2)
detective1_2 = detective_2[0]
detective2_2 = detective_2[1]
detective_num = random.sample(detective_number, k=2)
detective1_num = detective_num[0]
detective2_num = detective_num[1]

to_fill_in = {
    "DIVISION": None,
    "OFFENSE": None,
    "DESCRIPTION": None,
    "DATE": None,
    "TIME": None,
    "LOCATION": None,
    "RD": None,
    "DR": None,
    "FULL_NAME": None,
    "SEX": None,
    "ETHNICITY": None,
    "HAIR": None,
    "AGE": None,
    "WEAPONS": None,
    "detective1_1": detective1_1,
    "detective2_1": detective2_1,
    "detective1_2": detective1_2,
    "detective2_2": detective2_2,
    "detective1_num": detective1_num,
    "detective2_num": detective2_num,
    "detective1_badge": detective1_badge,
    "detective2_badge": detective2_badge,
}
def create_dr():
    dr1 = random.randint(10, 20)
    dr2 = random.randint(10, 20)
    dr3 = random.randint(1000, 9999)
    dr = f"{dr1}-{dr2}-0{dr3}"
    return dr
def save_file():
    try:
        pic_name = to_fill_in["FULL_NAME"].replace(" ", "_").lower()
        template.replace_pic("replace_me", f"mugshots/{pic_name}.png")
    except:
        full_name = to_fill_in["FULL_NAME"]
        print(f"No mugshot found for {full_name}.")
    finally:
        template.render(to_fill_in)
        filename = str(to_fill_in["FULL_NAME"]).replace(" ", "_") + "_wanted.docx"
        filled_path = os.path.join(temppath, filename)
        template.save(filled_path)
        print("Done with %s" % str(to_fill_in["FULL_NAME"]))
def main():
    while True:
        division = input("What's your division? (C/S/V/W) ").upper()
        if division == "C" or division == "S" or division == "V" or division == "W":
            if division == "C":
                to_fill_in["DIVISION"] = "Central"
            if division == "S":
                to_fill_in["DIVISION"] = "South"
            if division == "V":
                to_fill_in["DIVISION"] = "Valley"
            if division == "W":
                to_fill_in["DIVISION"] = "West"
            break
        else:
            print("Incorrect division")
    offense = str(input("What's the offense of the wanted suspect? "))
    to_fill_in["OFFENSE"] = offense.upper()
    description = str(input("Briefly describe the situation: "))
    to_fill_in["DESCRIPTION"] = description
    date = str(input("What's the date of the incident? (DD/MM/YYYY) "))
    to_fill_in["DATE"] = date
    time = str(input("When did the incident happen? (HH:MM) "))
    to_fill_in["TIME"] = time
    location = str(input("What's the location of the incident? "))
    to_fill_in["LOCATION"] = location
    rd = str(input("What's the postal of the incident? "))
    to_fill_in["RD"] = rd
    dr = create_dr()
    print(dr)
    to_fill_in["DR"] = dr
    full_name = str(input("What's offender's full name? "))
    to_fill_in["FULL_NAME"] = full_name
    while True:
        sex = str(input("What's the offender's sex? (M/F/U) ")).upper()
        if sex == "M" or sex == "F" or sex == "U":
            if sex == "M":
                to_fill_in["SEX"] = "Male"
            if sex == "F":
                to_fill_in["SEX"] = "Female"
            if sex == "U":
                to_fill_in["SEX"] = "Unknown"
            break
        else:
            print("Incorrect sex")
    ethnicity = str(input("What's offender's ethnicity? "))
    to_fill_in["ETHNICITY"] = ethnicity
    hair = str(input("Describe the hair the offender had (color, facial hair etc.) "))
    to_fill_in["HAIR"] = hair
    while True:
        try:
            age = int(input("What's the offender's age? (if unknown - write approx.) "))
            if age > 10 and age < 110:
                to_fill_in["AGE"] = age
                break
            else:
                print("Incorrect age")
        except:
            print("Incorrect age")
    weapons = str(input("What weapon's did the offender have? "))
    to_fill_in["WEAPONS"] = weapons
    to_fill_in["DIVISION_CAPS"] = to_fill_in["DIVISION"].upper()
    save_file()

if __name__ == "__main__":
    main()
