def FizzBuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        if i % 5 == 0 and i % 3 != 0:
            print("Buzz")
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")


class TestClass:
    def test_one(self, capsys):
        FizzBuzz()
        out, err = capsys.readouterr()

        fizzCount = 0

        for i in range(0, len(out)):
            if(out[i] == 'F' and out[i+4] != 'B'):
                fizzCount += 1
        assert fizzCount == 27

    def test_two(self, capsys):
        FizzBuzz()
        out, err = capsys.readouterr()

        buzzCount = 0

        for i in range(0, len(out)):
            if(out[i] == 'B' and out[i-1] != 'z'):
                buzzCount += 1
        assert buzzCount == 14

    def test_three(self, capsys):
        FizzBuzz()
        out, err = capsys.readouterr()

        fizzBuzzCount = 0

        for i in range(0, len(out)):
            if(out[i] == 'F' and out[i+4] == 'B'):
                fizzBuzzCount += 1
        assert fizzBuzzCount == 6
