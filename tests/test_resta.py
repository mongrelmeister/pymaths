from app.operaciones import resta


class TestClass:
    def test_resta(self):
        assert resta(3, 1) == 2
        assert resta(5, 3) == 2
        assert resta(-3, -3) == 0
        assert resta(-2, 4) == -6
