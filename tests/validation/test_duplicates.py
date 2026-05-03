def test_no_duplicate_words():
    text = "I I just want to"
    words = text.split()

    for i in range(len(words) - 1):
        assert words[i] != words[i + 1], "Duplicate word detected"