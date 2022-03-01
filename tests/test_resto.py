from app.operaciones import resto


class TestClass:
    def test_resto(self):
        assert resto(10, 2) == 0
        assert resto(15, 3) == 0
        assert resto(12, 5) == 2
        assert resto(17, 3) == 2
