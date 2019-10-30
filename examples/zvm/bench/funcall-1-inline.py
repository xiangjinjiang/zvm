# Function call overhead test
# Establish a baseline for performing a trivial operation inline


def test(num):
    for i in iter(range(num)):
        a = i + 1

test(100000000)
