import json
from numbers import Real
import threading


class Stats(object):
    def __init__(self):
        self._lock = threading.Lock()

        self._counters = {}
        self._gauges = {}
        self._labels = {}

    def incr(self, key, count=1):
        if not isinstance(count, int):
            raise TypeError("count must be integer.")
        with self._lock:
            curr_count = self._counters.get(key, 0)
            self._counters[key] = curr_count + count

    def get_counter(self, key):
        with self._lock:
            return self._counters[key]

    def rm_counter(self, key):
        with self._lock:
            del self._counters[key]

    def set_gauge(self, key, value):
        if not isinstance(value, Real):
            raise TypeError("Value must be numeric type.")
        with self._lock:
            self._gauges[key] = value

    def get_gauge(self, key):
        with self._lock:
            return self._gauges[key]

    def rm_gauge(self, key):
        with self._lock:
            del self._gauges[key]

    def set_label(self, key, value):
        if not isinstance(value, basestring):
            raise TypeError("Value must be string type.")
        with self._lock:
            self._labels[key] = value

    def get_label(self, key):
        with self._lock:
            return self._labels[key]

    def rm_label(self, key):
        with self._lock:
            del self._labels[key]

    def to_dict(self):
        with self._lock:
            return {
                "counters": self._counters.copy(),
                "gauges": self._gauges.copy(),
                "labels": self._labels.copy(),
            }

    def to_json(self):
        return json.dumps(self.to_dict())


stats = Stats()
