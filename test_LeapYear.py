def leapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return False
        return True
    else:
        return False


class TestClass:
    def test_one(self):
        assert leapYear(2021) == False

    def test_two(self):
        assert leapYear(2100) == True
