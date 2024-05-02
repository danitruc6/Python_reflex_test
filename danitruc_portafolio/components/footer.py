import reflex as rx
import datetime
from danitruc_portafolio.styles.styles import Size, Spacing
from danitruc_portafolio.styles.colors import TextColor as TextColor


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/logo.png",
            width=Size.VERY_BIG.value,
            height="auto",
            alt="logo de danitruc6",
        ),
        rx.link(
            f"{datetime.date.today().year} by Danitruc6 designs",
            href="https://danitruc6.com",
            is_external=True,
            font_size=Size.MEDIUM.value,
        ),
        rx.text(
            "Designed with pure Python using Reflex, From Costa Rica to the world",
            font_size=Size.MEDIUM.value,
        ),
        # margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,
        spacing=Spacing.ZERO.value,
        align="center",
        color=TextColor.FOOTER.value,
    )
