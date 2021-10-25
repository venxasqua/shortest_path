class Knot:
    def __init__(self,point,previous=None) -> None:
        self.point : tuple = point
        self.previous : tuple = previous
    def __eq__(self, o: object) -> bool:
        return self.point==o.point
    def __hash__(self) -> int:
        return hash(self.point)
    def __repr__(self) -> str:
        return "{}".format(self.point)