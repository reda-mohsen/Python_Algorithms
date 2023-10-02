"""
functions that test implementation of shorten thoroughly
"""

from twttr import shorten

def test_shorten():
    assert shorten("ahmed") == "hmd"
    assert shorten("Ahmed") == "hmd"
    assert shorten("RedA") == "Rd"
    assert shorten("rEdA") == "rd"
    assert shorten("Reda") == "Rd"
    assert shorten("REDA") == "RD"
    assert shorten("CS50") == "CS50"
    assert shorten("1234") == "1234"
    assert shorten("?RedA.") == "?Rd."
    assert shorten("re.da.") == "r.d."

