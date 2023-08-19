"""Tokenizer tests based on ATMEGA328-Motor-Board board."""


from __future__ import annotations

from test.gerberx3.test_tokenizer.common import make_tokenizer_test

test_sample = make_tokenizer_test(
    __file__,
    "test/assets/gerberx3/ATMEGA328-Motor-Board",
)
