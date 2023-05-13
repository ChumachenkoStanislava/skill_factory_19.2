import pytest

from app.calculator import Calculator


class TestCalc:
    def setup_method(self):
        self.calc = Calculator()

    def test_adding_success(self):
        assert self.calc.adding(1, 1) == 2

    def test_multiply_success(self):
        assert self.calc.multiply(1, 2) == 2

    def test_division_success(self):
        assert self.calc.division(4, 2) == 2

    def test_subtraction_success(self):
        assert self.calc.subtraction(4, 2) == 2


    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(1, 0)

    def teardown_method(self):
        print("Выполнение метода Teardown")