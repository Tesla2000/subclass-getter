from collections.abc import Generator
from typing import TypeVar

ClassType = TypeVar("ClassType", bound=type)


def get_subclasses(
    base_class: type[ClassType],
) -> Generator[type[ClassType], None, None]:
    for subclass in base_class.__subclasses__():
        yield subclass
        yield from get_subclasses(subclass)
