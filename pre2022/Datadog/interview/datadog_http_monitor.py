# -*- coding: utf-8 -*-
u"""
HTTP log monitoring console program.
"""
import sys
import os
import re

from datetime import datetime

from settings import logger, CONSOLE_REFRESH_INTERVAL, \
    AVERAGE_TRAFFIC_TOLERANCE, AVERAGE_TRAFFIC_INTERVAL


class CLFMonitor(object):

    """Main CLF Monitoring class."""

    time_begin = None
    high_traffic_mode = False
    # the current hit count counts the number of hits between 2 min intervals
    hit_average = {
        'current_hit_count': 0,
        'average_count': 0,
        'last_taken': None
    }
    # This hash_table should probably be a db
    sites_hit = {}

    def __init__(self, log_file):
        """Initialize with default values on the instance."""
        self.cleanup = False
        self.log_file = log_file
        self.max_hit_page = ''

    def update_stats(self, line_read):
        """
        Update stats for the pages hit.

        The Regex matches the url part of the logger.

        Parameters:
        -----------
        line_read: str
            A line from the log file with the common log format.
        """
        request_section = ''

        self.hit_average['current_hit_count'] += 1

        # this can be further advanced to only get the first part of url.
        # regex = '(?:.*?) - (?:.*?) \[(?:.*?)\] "(?:.*?) /(.*?) (?:.*?)" ' \
        #    '(?:.*?) (?:.*?)'
        regex = '^.*? - [^\"]*\"[^/]*\/([^/]*/[^/\s]*)'

        request_section = re.match(regex, line_read).groups()[0]
        # request_section = url.split('/')[0]

        self.sites_hit[request_section] = \
            self.sites_hit.get(request_section, 0) + 1
        if (
            self.sites_hit.get(self.max_hit_page, 0) <
            self.sites_hit[request_section]
        ):
            self.max_hit_page = request_section

    def update_average(self):
        """
        Update the average every 2 minutes.

        Generates warnings when traffic is abnormal.
        """
        now = datetime.now()
        if (
            (self.hit_average['last_taken'] - now).seconds >
            AVERAGE_TRAFFIC_INTERVAL
        ):
            self.hit_average['last_taken'] = now
            self.hit_average['average_count'] = (
                self.hit_average['current_hit_count'] /
                AVERAGE_TRAFFIC_INTERVAL
            )
            self.hit_average['current_hit_count'] = 0
            if self.hit_average['average_count'] > AVERAGE_TRAFFIC_TOLERANCE:
                logger.warning(
                    "High traffic generated an alert - hits = "
                    "{value}, triggered at {time}".format(
                        value=self.hit_average['average_count'],
                        time=self.hit_average['last_taken'])
                )
                self.high_traffic_mode = True
            elif self.high_traffic_mode:
                logger.warning("Traffic normalized at {time}".format(
                    time=self.hit_average['last_taken']))
                self.high_traffic_mode = False

    def display_stats(self):
        """Display interesting stats."""
        for key in self.hit_average.keys():
            logger.info("{key} : {value}".format(
                key=key, value=self.hit_average[key]))
        logger.info("Most hit page: {url} with {value}".format(
            url=self.max_hit_page, value=self.sites_hit[self.max_hit_page]))

    def read_http_log_file(self):
        """
        Read the log file and if the intervals meet, take and display stats.

        Opens file once, goes through the actively written file if a valid line
        can be read. When the keyboard interrupt is given we start the cleanup
        process which closes the file.
        """
        last_check = self.time_begin
        self.last_update_average = self.time_begin

        with open(self.log_file) as f:
            while not self.cleanup:
                cursor_position = f.tell()
                line = f.readline()
                now = datetime.now()

                if not line:
                    # if we cannot read the line set the cursor to prev. pos.
                    f.seek(cursor_position)
                else:
                    self.update_stats(line)
                if (now - last_check).seconds > CONSOLE_REFRESH_INTERVAL:
                    self.display_stats()
                    last_check = now
                if (
                    (now - self.hit_average['last_taken']).seconds >
                    AVERAGE_TRAFFIC_INTERVAL
                ):
                    self.update_average()

    def do_cleanup(self):
        """Cleanup file handlers."""
        self.cleanup = True

    def run(self):
        """Run the Monitor."""
        self.cleanup = False
        self.time_begin = datetime.now()
        self.hit_average['last_taken'] = self.time_begin

        logger.info('Begin')
        try:
            self.read_http_log_file()
        except KeyboardInterrupt:
            logger.info('User End.')
        except:
            logger.error(sys.exc_info()[0])
        finally:
            self.do_cleanup()
            sys.exit(0)


def main():
    """Main part, tries to access the file provided by the user."""
    file_path = sys.argv[1]
    read_possible = os.access(file_path, os.R_OK)
    if not read_possible:
        logger.error("File does not exist or cannot be read.")
        raise Exception("File does not exist or cannot be read.")
    monitor = CLFMonitor(file_path)
    monitor.run()

if __name__ == '__main__':
    """Run file as a script."""
    main()
