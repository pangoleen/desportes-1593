"""Focused synthetic OOV history regressions; Python standard library only.

The decoder and character kernel run with in-memory scores/counts. LM.__init__
is never called, so no language tables, corpus or checkpoints are loaded.
"""
import collections
import importlib
import itertools
import math
from pathlib import Path
import sys
import unittest


class ToyLM:
    def __init__(self, trie=None):
        self.trie = {} if trie is None else trie
        self.calls = set()

    def logp(self, word, previous):
        return 20.0

    def charlp(self, history, letter):
        self.calls.add((history, letter))
        return 0.0 if letter in 'abcdefghilm' else -9.0


class InMemoryLM:
    trie = {}

    def __init__(self, module, counts):
        self.kernel = object.__new__(module.LM)
        self.kernel.ch = counts
        self.kernel.ch4 = collections.Counter()
        for key, value in counts.items():
            self.kernel.ch4[key[:4]] += value

    def logp(self, word, previous):
        return 20.0

    def charlp(self, history, letter):
        return self.kernel.charlp(history, letter)


def oracle_score(word, counts):
    """Independent left-to-right score for the full four-character context."""
    denominators = collections.Counter()
    for key, value in counts.items():
        denominators[key[:-1]] += value
    total = 0.0
    for index, letter in enumerate(word):
        prefix = ('    ' + word[:index])[-4:]
        total += math.log((counts.get(prefix + letter, 0) + 0.3) /
                          (denominators.get(prefix, 0) + 0.3 * 23))
    return total


class DecodeHistoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'code'))
        cls.decoder = importlib.import_module('decode')

    def values(self, tokens, lm):
        segments = self.decoder.decode(
            tokens, [None] * len(tokens), lm, beam=1024,
            a_nogap=0.0, b_ingap=0.0, oov=0.0)
        return self.decoder.letters(segments, tokens)

    def test_complete_history_for_lengths_zero_through_64(self):
        for length in range(65):
            with self.subTest(length=length):
                lm = ToyLM()
                self.assertEqual(self.values(['A'] * length, lm), ['a'] * length)
                expected = {((' ' + 'a' * index)[-4:], 'a')
                            for index in range(length)}
                self.assertFalse(expected - lm.calls,
                                 'character model did not receive complete history')

    def test_history_resets_after_sign_words_and_placeholder(self):
        for sign, expansion in (('Q', 'que'), ('K', 'qui'), ('P', 'pour'),
                                ('R', 'par'), ('&', 'et'), ('#', '#')):
            with self.subTest(sign=sign):
                lm = ToyLM()
                self.assertEqual(self.values([sign, 'A'], lm), [expansion, 'a'])
                self.assertIn((' ', 'a'), lm.calls)

    def test_history_resets_after_lexicon_word(self):
        lm = ToyLM(trie={'A': {'$': ['n']}})
        self.assertEqual(self.values(['A', 'B'], lm), ['n', 'b'])
        self.assertIn((' ', 'b'), lm.calls)

    def test_context_dependent_paths_and_tie_match_exhaustive_oracle(self):
        cases = (
            ('second_glyph_prefers_nonprimary', 'AA',
             {'    a': 10, '    n': 1, '   aa': 1, '   an': 20}),
            ('nonprimary_prefix_prefers_primary_suffix', 'AA',
             {'    a': 1, '    n': 10, '   na': 20, '   nn': 1}),
            ('two_context_dependent_nonprimary_choices', 'ABC',
             {'    a': 5, '    n': 1, '   ab': 1, '   ao': 20,
              '  aoc': 20, '  aop': 1}),
            ('tied_score_control', 'ABC', {}),
        )
        # This tiny alphabet is written independently of the decoder's PAIRS.
        choices = {'A': 'an', 'B': 'bo', 'C': 'cp'}
        for name, token_string, counts in cases:
            with self.subTest(case=name):
                scores = {''.join(path): oracle_score(''.join(path), counts)
                          for path in itertools.product(
                              *(choices[token] for token in token_string))}
                maximum = max(scores.values())
                maximizers = {word for word, score in scores.items()
                              if math.isclose(score, maximum,
                                              rel_tol=1e-13, abs_tol=1e-13)}
                chosen = ''.join(self.values(
                    list(token_string), InMemoryLM(self.decoder, counts)))
                self.assertIn(chosen, maximizers)


if __name__ == '__main__':
    unittest.main()
