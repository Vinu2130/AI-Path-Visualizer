from abc import abstractclassmethod,ABC

class AbstractPathFinder(ABC):
    @abstractclassmethod
    def findPath(self)->list:
        pass

class defaultPathFinderClass(AbstractPathFinder):
    def findPath(self) -> list:
        return [(2, 8), (3, 8), (4, 8), (4, 7), (4, 6), (4, 5), (4, 4), (4, 3), (4, 2), (4, 1), (5, 1), (6, 1), (7, 1)]




