class Range:
    def __init__(self, start: float, end: float):
        self.__start = start
        self.__end = end

    @property
    def start(self) -> float:
        return self.__start

    @start.setter
    def start(self, start: float):
        self.__start = start

    @property
    def end(self) -> float:
        return self.__end

    @end.setter
    def end(self, end: float):
        self.__end = end

    def __repr__(self):
        return f'({self.__start}; {self.__end})'

    def get_length(self) -> float:
        return self.__end - self.__start

    def is_inside(self, number: float) -> bool:
        return self.__start <= number <= self.__end

    def get_intersection(self, input_range):
        max_start = max(self.__start, input_range.start)
        min_end = min(self.__end, input_range.end)

        if max_start < min_end:
            return Range(max_start, min_end)

        return None

    def get_union(self, input_range):
        max_start = max(self.__start, input_range.start)
        min_end = min(self.__end, input_range.end)

        if max_start <= min_end:
            return [Range(min(self.__start, input_range.start), max(self.__end, input_range.end))]

        return [Range(self.start, self.end), Range(input_range.start, input_range.end)]

    def get_difference(self, input_range):
        if input_range.start > self.__start and input_range.end < self.__end:
            return [Range(self.start, input_range.start), Range(input_range.end, self.__end)]

        if input_range.start <= self.start and input_range.end >= self.end:
            return []

        if input_range.start <= self.__start < input_range.end:
            return [Range(input_range.end, self.end)]

        if input_range.end >= self.end and input_range.start < self.__end:
            return [Range(self.__start, input_range.start)]

        return [Range(self.start, self.end)]
