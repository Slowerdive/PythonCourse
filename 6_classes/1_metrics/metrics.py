import csv
import time

class BaseFileHandler:
    def __init__(self, filepath, expected_extension):
        if not filepath.endswith(expected_extension):
            raise ValueError(f"Файл должен иметь расширение '{expected_extension}'")
        self.filepath = filepath
        self._initialize_file()

    def _initialize_file(self):
        try:
            with open(self.filepath, "x") as _:
                pass
        except FileExistsError:
            pass

    def append_data(self, records):
        raise NotImplementedError("Метод append_data должен быть переопределён в подклассе")


class TxtHandler(BaseFileHandler):
    def __init__(self, filepath):
        super().__init__(filepath, '.txt')

    def append_data(self, records):
        with open(self.filepath, "a", newline="") as file:
            for entry in records:
                date, metric, value = entry
                file.write(f"{date} {metric} {value}\n")


class CsvHandler(BaseFileHandler):
    def __init__(self, filepath):
        super().__init__(filepath, '.csv')
        if not self._file_exists_or_empty():
            self._initialize_csv_file()

    def _initialize_csv_file(self):
        with open(self.filepath, "w", newline="") as file:
            writer = csv.writer(file, delimiter=";", lineterminator="\n")
            writer.writerow(["date", "metric", "value"])

    def _file_exists_or_empty(self):
        try:
            with open(self.filepath, "r") as file:
                return file.read(1) != ""
        except FileNotFoundError:
            return False

    def append_data(self, records):
        with open(self.filepath, "a", newline="") as file:
            writer = csv.writer(file, delimiter=";", lineterminator="\n")
            writer.writerows(records)


class Statsd:
    def __init__(self, buffer_max, file_handler):
        self.buffer_max = buffer_max
        self.file_handler = file_handler
        self.buffer = []

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self._flush_buffer()

    def incr(self, metric):
        self._record_metric(metric, 1)

    def decr(self, metric):
        self._record_metric(metric, -1)

    def _record_metric(self, metric, adjustment):
        self.buffer.append([self._current_utc_time(), metric, adjustment])
        if len(self.buffer) >= self.buffer_max:
            self._flush_buffer()

    def _flush_buffer(self):
        if self.buffer:
            self.file_handler.append_data(self.buffer)
            self.buffer.clear()

    @staticmethod
    def _current_utc_time():
        return time.strftime("%Y-%m-%dT%H:%M:%S%z", time.gmtime())


def get_txt_statsd(filepath, buffer_max=10):
    return Statsd(buffer_max, TxtHandler(filepath))


def get_csv_statsd(filepath, buffer_max=10):
    return Statsd(buffer_max, CsvHandler(filepath))
