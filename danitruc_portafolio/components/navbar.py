import reflex as rx
import danitruc_portafolio.styles.styles as styles
from danitruc_portafolio.styles.styles import Size as Size
from danitruc_portafolio.styles.colors import TextColor as TextColor
from danitruc_portafolio.styles.colors import Color as Color
from danitruc_portafolio.routes import Route


def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.text(
                rx.text("dani", as_="span", color=Color.PRIMARY.value),
                rx.text("truc", as_="span", color=Color.SECONDARY.value),
                style=styles.navbar_title_style,
            ),
            href=Route.INDEX.value,
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        z_index="99",
        top="0",
    )
