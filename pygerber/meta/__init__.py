from typing import Tuple

from pygerber.exceptions import DeprecatedSyntax

from .broker import DrawingBroker
from .data import Vector2D
from .coparser import CoParser
from .meta import Interpolation, Mirroring, Polarity, Unit
from .aperture import Aperture, ApertureSet


class Meta(DrawingBroker):

    coparser = CoParser

    def __init__(
        self,
        apertureSet: ApertureSet,
        *,
        ignore_deprecated: bool = True,
    ) -> None:
        self.ignore_deprecated = ignore_deprecated
        self.coparser = CoParser()
        self.bind_aperture_set(apertureSet)

    def raiseDeprecatedSyntax(self, message: str):
        if not self.ignore_deprecated:
            raise DeprecatedSyntax(message)
