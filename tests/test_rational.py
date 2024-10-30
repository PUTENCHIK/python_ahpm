import pytest
from models import Rational


class TestRational:

    def test_init(self):
        r = Rational(1)
        assert r.num == 1 and r.den == 1
        r = Rational(1, 0)
        assert r.num == 1 and r.den == 1
        r = Rational(2, 4)
        assert r.num == 1 and r.den == 2
        r = Rational(2, -2)
        assert r.num == -1 and r.den == 1

    def test_init_string(self):
        r = Rational(string="1/2")
        assert r.num == 1 and r.den == 2
        r = Rational(string="1/-2")
        assert r.num == -1 and r.den == 2
        r = Rational(string="1/0")
        assert r.num == 1 and r.den == 1

    def test_init_string_fail(self):
        with pytest.raises(ValueError):
            Rational(string="1//1")
            Rational(string="/1")
            Rational(string="0.5")

    @pytest.mark.parametrize(
        "r, result",
        [(Rational(1), 1),
         (Rational(1, -1), -1),
         (Rational(3, 5), 0.6),
         (Rational(4, 8), 0.5),
         (Rational(2, 4), Rational(1, 2)),
         (Rational(13, 5), Rational(string="13/5")),
         (Rational(-3, -8), 0.375),]
    )
    def test_equal(self, r, result):
        assert r == result

    @pytest.mark.parametrize(
        "r1, r2, result",
        [(Rational(1), Rational(0), 1),
         (Rational(1, 2), Rational(1, 2), 1),
         (Rational(3, 4), Rational(7, 4), 2.5),
         (Rational(12, 5), Rational(3, 5), 3),
         (Rational(-1), Rational(1), 0),
         (Rational(35, 2), Rational(2, 35), Rational(1229, 70)),]
    )
    def test_add(self, r1, r2, result):
        assert r1 + r2 == result
