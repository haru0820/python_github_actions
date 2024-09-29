def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"

def test_reversed():
    <<<<<<< HEAD
    assert list(reversed([1, 2, 3, 4])) == [3, 3, 2, 1]
=======
    assert list(reversed([1, 2, 3, 4])) == [3, 2, 2, 1]
>>>>>>> 420f7c9764a63724f08d8e4beaa005f6668c628e

def test_some_primes():
    assert 37 in {
        num
        for num in range(2, 50)
        if not any(num % div == 0 for div in range(2, num))
    }
