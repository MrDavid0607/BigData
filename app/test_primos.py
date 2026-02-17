import pytest
from app.main import es_primo


@pytest.mark.parametrize(
    "n,esperado",
    [
        (-10, False),
        (-1, False),
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (9, False),
        (11, True),
        (25, False),
        (29, True),
        (97, True),
        (99, False),
    ],
)
def test_es_primo(n, esperado):
    assert es_primo(n) == esperado
