from app.operaciones import cociente


class TestClass:
    def test_cociente(self):
        assert cociente(11, 5) == 2
        assert cociente(23, 2) == 11
        assert cociente(7, 3) == 2
        assert cociente(9, 2) == 4
