import time

class Timer:

    def __init__(self):
        self._start_time = None
        self.elapsed_time = None
        self.started = False

    def start(self):
        self._start_time = time.perf_counter()
        self.started = True

    def nostop(self):
        if self.started == False:
            self._start_time = time.perf_counter()
        elif self.elapsed_time == None:
            self.elapsed_time = time.perf_counter() - self._start_time
        else:
            self._start_time = time.perf_counter() - elapsed_time
				
    def stop(self):
        self.elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        return self.elapsed_time

    def check(self):
        if self._start_time == None:
            return self.elapsed_time
        else:
            self.elapsed_time = time.perf_counter() - self._start_time
            return self.elapsed_time