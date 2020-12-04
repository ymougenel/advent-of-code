#!/usr/bin/env python3
import re


def get_file(file_name):
    inputFile = open(file_name, "r")
    data = inputFile.read().splitlines()
    inputFile.close()
    passports = []
    i = 0
    for line in data:
        if line == "":
            i += 1
        else:
            if len(passports) > i:
                passports[i] += " " + line
            else:
                passports.append(" " + line)
    return passports



required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
hair_color = re.compile(r'^#[a-z0-9]{6}$')
passport_id = re.compile(r'^[0-9]{9}$')
four_digits = re.compile(r'^[0-9]{4}$')

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid optional
def validate(passport):
    fields = passport.split(" ")
    fields = [(field.split(':')[0], field.split(':')[1]) for field in fields if field != ""]
    for required in required_fields:
        found = False
        for (key, val) in fields:
            if key == required:
                found = True
                if not validate_field(key, val):
                    return False
        if not found:
            return False
    return True


def validate_field(field, value) -> bool:
    if field == "byr":
        return four_digits.match(value) is not None and 1920 <= int(value) <= 2002
    if field == "iyr":
        return four_digits.match(value) is not None and 2010 <= int(value) <= 2020
    if field == "eyr":
        return four_digits.match(value) is not None and 2020 <= int(value) <= 2030
    if field == "hgt":
        if "cm" in value:
            value = value[:-2]
            return 150 <= int(value) <= 193
        if "in" in value:
            value = value[:-2]
            return 59 <= int(value) <= 76
    if field == "hcl":
        return hair_color.match(value) is not None
    if field == "ecl":
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if field == "pid":
        return passport_id.match(value) is not None
    return False


if __name__ == '__main__':
    # passports = get_file("inputs/part1.example")
    # passports = get_file("inputs/part2.valid.example")
    # passports = get_file("inputs/part2.invalid.example")
    passports = get_file("inputs/part1.input")
    print(len([passport for passport in passports if validate(passport)]))
