import pytest
from mempg import generators


def test_init_exception():
    with pytest.raises(ValueError):
        generator = generators.Generator(length=1000)
        assert generator


def test_init_formats():
    for length in generators.fmt_options.keys():
        generator = generators.Generator(length=length)
        assert " ".join(generator.word_types) in generators.fmt_options[length]


def test_make_pass():
    for length in generators.fmt_options.keys():
        generator = generators.Generator(length=length)
        generator.make_pass()
        assert len(generator.phrase.split(" ")) == length


def test_make_pass_with_numbers():
    for length in generators.fmt_options.keys():
        generator = generators.Generator(length=length, add_num=True)
        generator.make_pass()
        assert len(generator.phrase.split(" ")) == length + 1
        assert generator.phrase[-4:].isdigit()
