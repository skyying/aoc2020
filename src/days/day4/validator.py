import re


def byr(value):
    """
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    """
    return 1920 <= int(value) <= 2002


def iyr(value):
    """
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    """
    return 2010 <= int(value) <= 2020


def eyr(value):
    """
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    """
    return 2020 <= int(value) <= 2030


def hgt(value):
    """
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    """
    n = len(value)
    p = re.compile('(\d+cm)|(\d+in)')
    m = p.match(value)
    if m is not None and m.group() == value:
        follow_by = value[n-2:n]
        digits = int(value[0: n - 2])
        if follow_by == 'cm':
            return 150 <= digits <= 193
        if follow_by == 'in':
            return 59 <= digits <= 76
    return False


def hcl(value):
    """
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    """
    p = re.compile('(#[0-9a-z]{6})')
    m = p.match(value)
    return m is not None and m.group() == value


def ecl(value):
    """
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    """
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def pid(value):
    """
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    """
    p = re.compile('([0-9]{9})')
    m = p.match(value)
    return m is not None and m.group() == value


def cid(value):
    """
    cid (Country ID) - ignored, missing or not.
    """
    return True


def get_validator():
    return {
        'cid': cid,
        'pid': pid,
        'byr': byr,
        'iyr': iyr,
        'eyr': eyr,
        'hgt': hgt,
        'hcl': hcl,
        'ecl': ecl,
    }
