import doctest
import unittest
import MyUnitTest

def algo_func(*args, **kwargs):
    """Функция, реализующая ваш алгоритм/математическую функцию.
    >>> algo_func(178)
    871
    >>> algo_func(-178)
    -1
    >>> algo_func("876")
    -1
    >>> algo_func("Hello")
    -1
    >>> algo_func(None)
    -1
    >>> algo_func(True)
    -1
    >>> algo_func(algo_func)
    -1
    """
    # здесь реализация алгоритма
    number = args[0]
    if not isinstance(number, int):
        return -1
    if isinstance(number, bool):
        return -1
    if number < 0:
        return -1
    numberBackwards = 0
    while number > 0:
        numberBackwards = numberBackwards * 10 + number % 10
        number //= 10
    
    return numberBackwards

if __name__ == '__main__':
    # здесь используйте инструкции assert
    assert algo_func(123) == 321, "функция работает не верно"
    assert algo_func(12536452547684268794623) == 32649786248674525463521, "функция работает не верно"
    assert algo_func(-123) == -1, "функция работает не верно"
    assert algo_func("123") == -1, "функция работает не верно"
    assert algo_func(None) == -1, "функция работает не верно"
    assert algo_func(321.432) == -1, "функция работает не верно"
    assert algo_func(1e-3) == -1, "функция работает не верно"
    assert algo_func(algo_func) == -1, "функция работает не верно"
    assert algo_func(True) == -1, "функция работает не верно"
    assert algo_func(False) == -1, "функция работает не верно"
    assert algo_func(0) == 0, "функция работает не верно"
    assert algo_func(1) == 1, "функция работает не верно"
    
    # здесь вызовите код проверки через doctest
    doctest.testmod()

    # для unittest сделайте дополнительный файл в который поместите его тесты.
    suite = unittest.TestLoader().loadTestsFromModule(MyUnitTest)
    unittest.TextTestRunner().run(suite)