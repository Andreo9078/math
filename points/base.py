from abc import ABC, abstractmethod


class BasePoint(ABC):
    @abstractmethod
    def as_dict(self):
        pass

    @abstractmethod
    def as_tuple(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class BasePointCreator(ABC):
    @abstractmethod
    def create_from_dict(self, dc: dict):
        pass

    @abstractmethod
    def create_from_tuple(self, tup: tuple):
        pass


class BasePointSet(ABC):
    @abstractmethod
    def __init__(self,
                 point_creator: BasePointCreator,
                 points: list[BasePoint | dict | tuple] = [], ):
        self.point_creator = point_creator
        self.set_points(points)

    @abstractmethod
    def set_points_from_dicts_list(self, lst: list[dict]):
        pass

    @abstractmethod
    def set_points_from_tuples_list(self, lst: list[tuple]):
        pass

    @abstractmethod
    def set_points(self):
        pass

    @abstractmethod
    def get_x_y_lists(self):
        pass

    @property
    def points(self) -> list[BasePoint]:
        return self._points

    @abstractmethod
    def __iter__(self):
        iter(self.points)

    @abstractmethod
    def __len__(self):
        len(self.points)