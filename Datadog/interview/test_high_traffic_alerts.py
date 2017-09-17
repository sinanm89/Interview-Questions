# -*- coding: utf-8 -*-
u"""
Tests for the http log file monitoring Script for Datadog.

Since the code is divided into methods, if we want to test the alert logic we
can simply test the method that calls it. This assumes the rest of the code
is also tested and works correctly.
"""
import unittest

from datadog_http_monitor import CLFMonitor
from datetime import datetime, timedelta

from settings import AVERAGE_TRAFFIC_INTERVAL, AVERAGE_TRAFFIC_TOLERANCE


class TestAlerts(unittest.TestCase):

    """Test the alert case."""

    def test_high_traffic_exceed(self):
        """Test to see if there is high traffic."""
        test_class = CLFMonitor('')

        test_class.hit_average = {
            'current_hit_count':
                (AVERAGE_TRAFFIC_TOLERANCE + 1) * AVERAGE_TRAFFIC_INTERVAL,
            'average_count': 0,
            'last_taken': datetime.now() - timedelta(
                seconds=AVERAGE_TRAFFIC_INTERVAL + 10)
        }
        test_class.update_average()
        self.assertTrue(test_class.high_traffic_mode)

    def test_high_traffic_recede(self):
        """Test to see if the recession of traffic is understood."""
        test_class = CLFMonitor('')
        test_class.hit_average = {
            'current_hit_count': 0,
            'average_count': 0,
            'last_taken': datetime.now() - timedelta(
                seconds=AVERAGE_TRAFFIC_INTERVAL + 10)
        }
        test_class.high_traffic_mode = True
        test_class.update_average()
        self.assertFalse(test_class.high_traffic_mode)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAlerts)
    unittest.TextTestRunner(verbosity=2).run(suite)
