"""Base class for creating components for aperture creation."""
from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING

from pydantic import BaseModel

from pygerber.backend.abstract.bounding_box import BoundingBox
from pygerber.backend.abstract.vector_2d import Vector2D

if TYPE_CHECKING:
    from pygerber.backend.abstract.aperture_handle import PrivateApertureHandle


class ApertureDraw(BaseModel):
    """Description of aperture component."""

    center_position: Vector2D

    @abstractmethod
    def draw(self, handle: PrivateApertureHandle) -> None:
        """Apply aperture draw component to handle."""

    @abstractmethod
    def get_bounding_box(self) -> BoundingBox:
        """Return bounding box of draw operation."""
