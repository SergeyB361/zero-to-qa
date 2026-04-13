# Bonus Advanced Python OOP, День 6 - Data classes, multiple inheritance и __slots__
#
# В этом файле 4 задания. Сейчас он запускается как scaffold,
# но часть advanced-паттернов ещё не реализована.


from dataclasses import dataclass


# Задание 1
# Добавь useful dataclass-поведение для ReleaseKey.
# Подумай, нужен ли здесь frozen и slots.
@dataclass
class ReleaseKey:
    version: str
    environment: str


# Задание 2
# Доведи mixin-цепочку через super().
class BaseModel:
    def __init__(self, **kwargs: object) -> None:
        super().__init__()


class TimestampMixin(BaseModel):
    def __init__(self, created_at: str, **kwargs: object) -> None:
        self.created_at = created_at
        super().__init__(**kwargs)


class OwnerMixin(BaseModel):
    def __init__(self, owner: str, **kwargs: object) -> None:
        # TODO:
        # self.owner = owner
        # super().__init__(**kwargs)
        pass


class ArtifactRecord(TimestampMixin, OwnerMixin):
    def __init__(self, name: str, created_at: str, owner: str) -> None:
        self.name = name
        super().__init__(created_at=created_at, owner=owner)


# Задание 3
# Добавь __slots__ для FixedCoordinate.
class FixedCoordinate:
    # TODO: __slots__ = ("x", "y")
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


# Задание 4
# После практики ответь:
# когда dataclass лучше обычного класса,
# а когда __slots__ только мешает.


if __name__ == "__main__":
    print("=== Current scaffold output ===")

    key_1 = ReleaseKey("1.0.0", "prod")
    key_2 = ReleaseKey("1.0.0", "prod")
    print("ReleaseKey equality ->", key_1 == key_2)

    artifact = ArtifactRecord("report.json", "2026-04-13", "sergey")
    print("artifact.name ->", artifact.name)
    print("artifact.created_at ->", artifact.created_at)
    print("artifact.owner ->", getattr(artifact, "owner", "<owner missing>"))

    point = FixedCoordinate(10, 20)
    print("point ->", point.x, point.y)
    try:
        point.label = "origin"
        print("dynamic attribute was accepted")
    except AttributeError as error:
        print("dynamic attribute rejected:", error)