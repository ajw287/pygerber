from pathlib import Path
from pygerber.gerberx3.api.color_scheme import ColorScheme
from pygerber.gerberx3.api.layers import Rasterized2DLayer, Rasterized2DLayerParams


def render() -> None:
    source_path = Path(__file__).parent / "render_copper_from_path.grb"

    Rasterized2DLayer(
        options=Rasterized2DLayerParams(
            source_path=source_path,
            colors=ColorScheme.COPPER_ALPHA,
        ),
    ).render().save("output.png")


if __name__ == "__main__":
    render()
