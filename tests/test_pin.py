import sys, unittest


class PinTests(unittest.TestCase):
    def test_runs_on_the_pinned_interpreter(self):
        self.assertEqual(sys.version_info[:2], (3, 12))
