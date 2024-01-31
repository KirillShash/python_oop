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

    def get_length(self) -> float:
        return self.__end - self.__start

    def is_inside(self, number: float) -> bool:
        return self.__start <= number <= self.__end
