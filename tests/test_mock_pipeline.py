"""Run from the repository root: python -m unittest discover -s tests -v"""
import unittest
from integration.mock_pipeline import demo, record, validate


class TestContract(unittest.TestCase):
    def test_valid_record(self):
        self.assertTrue(validate(record('feed_weight_kg', 2.4, 'feed-01')))

    def test_wrong_unit(self):
        bad = record('feed_weight_kg', 2.4, 'feed-01')
        bad['unit'] = 'L'
        self.assertFalse(validate(bad))

    def test_invalid_percentage(self):
        self.assertFalse(validate(record('humidity_pct', 105.0, 'dht-01')))

    def test_mock_sources_run(self):
        observations = demo(0.6)
        metrics = {x['metric'] for x in observations}
        self.assertIn('feed_weight_kg', metrics)
        self.assertIn('water_distance_cm', metrics)
        self.assertIn('temperature_c', metrics)


if __name__ == '__main__':
    unittest.main()
