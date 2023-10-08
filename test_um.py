"""
test count() function
"""

from um import count

def test_count():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    assert count("umum um") == 1
    assert count("hello, um, world ") == 1
    assert count(" ") == 0
    assert count("um, hello, um, world") == 2
    assert count("um...") == 1
    assert count("yum") == 0
    assert count("cat") == 0