import _1_Classes as CLASS

def check_get_younger():
    age = 12
    test_guy = CLASS.Human(age, "jeremy")
    test_guy.get_younger()

    assert test_guy.age == age-1

if __name__ == '__main__':
    check_get_younger()
    print "success"