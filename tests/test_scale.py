import unittest

from maskminder import maskminder as s


class ScaleTest(unittest.TestCase):
    Bb_chromatic = ['Bb', 'B', 'C', 'Db', 'D',
                    'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A']

    @classmethod
    def setUpClass(ScaleTest):
        ScaleTest.Cmaj = s.Scale('C', 'major')
        ScaleTest.Bbmaj = s.Scale('Bb', 'major')
        ScaleTest.Cnatmin = s.Scale('C', 'natural minor')

    def test_tonic_c(self):
        self.assertEqual('C', ScaleTest.Cmaj.tonic)

    def test_chromatic_scale_type(self):
        self.assertEqual(['C', 'C#', 'D', 'D#', 'E',
                          'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'], ScaleTest.Cmaj.chromatic_type(s.Scale.CHROMATIC))

    def test_chromatic_scale_type(self):
        self.assertEqual(ScaleTest.Bb_chromatic, ScaleTest.Bbmaj.chromatic_type(
            s.Scale.CHROMATIC_FLAT))

    def test_determine_cromatic_C(self):
        self.assertEqual(s.Scale.CHROMATIC, ScaleTest.Cmaj.chromatic)

    def test_determine_cromatic_Bb(self):
        self.assertEqual(ScaleTest.Bb_chromatic, ScaleTest.Bbmaj.chromatic)

    def test_notes_C_major(self):
        self.assertEqual(['C', 'D', 'E', 'F', 'G', 'A', 'B'],
                         ScaleTest.Cmaj.notes)

    def test_notes_Bb_major(self):
        self.assertEqual(['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A'],
                         ScaleTest.Bbmaj.notes)

    def test_notes_C_natural_minor(self):
        self.assertEqual(['C', 'D', 'Eb', 'F', 'G', 'Ab',
                          'Bb'], ScaleTest.Cnatmin.notes)
