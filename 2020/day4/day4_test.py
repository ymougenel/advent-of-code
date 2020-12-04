import unittest
import day4


class day4_test(unittest.TestCase):

    def test_validate_field_test(self):
        # Birth year
        self.assertEqual(day4.validate_field("byr", "1920"), True)
        self.assertTrue(day4.validate_field("byr", "2002"))
        self.assertFalse(day4.validate_field("byr", "1919"))
        self.assertFalse(day4.validate_field("byr", "2003"))

        # Issue year
        self.assertTrue(day4.validate_field("iyr", "2010"))
        self.assertTrue(day4.validate_field("iyr", "2020"))
        self.assertFalse(day4.validate_field("iyr", "2009"))
        self.assertFalse(day4.validate_field("iyr", "2021"))

        # Expiration year
        self.assertTrue(day4.validate_field("eyr", "2020"))
        self.assertTrue(day4.validate_field("eyr", "2030"))
        self.assertFalse(day4.validate_field("eyr", "2019"))
        self.assertFalse(day4.validate_field("eyr", "2031"))

        # Height year
        self.assertTrue(day4.validate_field("hgt", "150cm"))
        self.assertTrue(day4.validate_field("hgt", "193cm"))
        self.assertTrue(day4.validate_field("hgt", "59in"))
        self.assertTrue(day4.validate_field("hgt", "76in"))
        self.assertFalse(day4.validate_field("hgt", "149cm"))
        self.assertFalse(day4.validate_field("hgt", "194cm"))
        self.assertFalse(day4.validate_field("hgt", "58in"))
        self.assertFalse(day4.validate_field("hgt", "77in"))

        # Hair Color
        self.assertTrue(day4.validate_field("hcl", "#123456"))
        self.assertTrue(day4.validate_field("hcl", "#1da2a5"))
        self.assertFalse(day4.validate_field("hcl", "123456"))
        self.assertFalse(day4.validate_field("hcl", "#12345"))
        self.assertFalse(day4.validate_field("hcl", "#1234567"))
        self.assertFalse(day4.validate_field("hcl", "#1+2345"))
        self.assertFalse(day4.validate_field("hcl", "#1z2345"))

        # Eyes Color
        self.assertTrue(day4.validate_field("ecl", "amb"))
        self.assertTrue(day4.validate_field("ecl", "oth"))
        self.assertFalse(day4.validate_field("ecl", ""))
        self.assertFalse(day4.validate_field("ecl", "azerty"))
        self.assertFalse(day4.validate_field("ecl", "#blue-tooth"))

        # Passport Id
        self.assertTrue(day4.validate_field("pid", "123456789"))
        self.assertTrue(day4.validate_field("pid", "000000001"))
        self.assertFalse(day4.validate_field("pid", "azertyui"))
        self.assertFalse(day4.validate_field("pid", ""))
        self.assertFalse(day4.validate_field("pid", "12345678910"))


if __name__ == '__main__':
    unittest.main()
