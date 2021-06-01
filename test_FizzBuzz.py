def FizzBuzz():
    for i in range(0, 100):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


class TestClass:
    def test_one(self, capsys):
        FizzBuzz()
        out, err = capsys.readouterr()

        fizzCount = 0
        buzzCount = 0
        fizzBuzzCount = 0

        for i in range(0, len(out)):
            if(out[i] == 'F'):
                if(out[i+4] == 'B'):
                    fizzBuzzCount += 1
                else:
                    fizzCount += 1
            elif(out[i] == 'B' and out[i-1] != 'z'):
                buzzCount += 1
        assert fizzCount == 27
