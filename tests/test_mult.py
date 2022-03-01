from app.operaciones import multiplicacion


class TestClass:
    def test_multiplicacion(self):
        assert multiplicacion(3, 3) == 9
        assert multiplicacion(2, 2) == 4
        assert multiplicacion(1, 2) == 2
        assert multiplicacion(-3, 4) == -12
