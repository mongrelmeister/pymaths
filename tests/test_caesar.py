from re import S

from app.rotcaesar import rot13_cipher


class TestClass:
    def test_rot13_cipher(self):
        assert rot13_cipher("foobar") == "sbbone"
        assert rot13_cipher("HELLO WORLD") == "URYYBaJBEYQ"
        assert rot13_cipher("HolaMundo") == "UbynZhaqb"
