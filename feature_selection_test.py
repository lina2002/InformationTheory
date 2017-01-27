import unittest

import feature_selection


class UrlTest(unittest.TestCase):
    def test_should_compute_mutual_information_of_2_vectors(self):
        self.assertEquals(1, feature_selection.mutual_information([[0, 0, 1, 1]], [1, 1, 0, 0]))
        self.assertEquals(0, feature_selection.mutual_information([[1, 0, 1, 0]], [1, 1, 0, 0]))

    def test_should_compute_mutual_information_of_3_vectors(self):
        self.assertEquals(1, feature_selection.mutual_information([[0, 0, 1, 1], [1, 0, 1, 0]], [1, 1, 0, 0]))
        self.assertAlmostEquals(0.7219280948873623,
                                feature_selection.mutual_information([[0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                                                                      [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]],
                                                                     [1, 1, 0, 1, 1, 0, 1, 1, 1, 1]))