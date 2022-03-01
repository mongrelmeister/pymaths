from app.operaciones import division


class TestClass:
    def test_division(self):
        assert division(10, 2) == 5
        assert division(9, 3 ) == 3
        assert division(12, 4) == 3
        assert division(25, 5) == 5
