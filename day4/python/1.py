import functools
import re
from validator import get_validator

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' ]
optional_fields = ['cid']

def read_passports():
    f = open('../in', 'r')
    return f.read().split("\n\n")


def normalize_passports(passport):
    return ' '.join(passport.strip('\n').split('\n')).split(' ')


def translate_to_dict(password):
    password_dict = {}
    for field in password:
        key, value = field.split(":")
        password_dict[key] = value
    return password_dict


def missing_only_cid(passport):
    cid = 'cid'
    info_dict = translate_to_dict(passport)
    for key in required_fields:
        if key not in info_dict and key is not cid:
            return False
    return True


def contain_all_fields(passport):
    return len(passport) == len(required_fields) + len(optional_fields)


def is_all_fields_valid(passport):
    if is_pass_simple_validation(passport):
        passport_dict = translate_to_dict(passport)
        return all([get_validator()[field](value) for field, value in passport_dict.items()])
    return False


def is_pass_simple_validation(passport):
    return contain_all_fields(passport) or missing_only_cid(passport)


def get_valid_passport_count(passports, validator):
    count = 0
    for passport in passports:
        passport = normalize_passports(passport)
        if validator(passport):
            count+=1
    return count


passports = read_passports()

# part 1
print(get_valid_passport_count(passports, is_pass_simple_validation))

# part 2
print(get_valid_passport_count(passports, is_all_fields_valid))

