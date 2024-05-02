import reflex as rx
from danitruc_portafolio.styles.colors import Color, TextColor
import danitruc_portafolio.styles.styles as styles
from danitruc_portafolio.styles.styles import Size as Size, Spacing


def link_button(
    title: str, body: str, url: str, image: str, is_external=True
) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag=image,
                    width=styles.Size.LARGE.value,
                    height=styles.Size.LARGE.value,
                    margin=Size.MEDIUM.value,
                    color=TextColor.HEADER.value,
                    alt=title,
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    align_items="start",
                    spacing=Spacing.VERY_SMALL.value,
                    margin=Size.ZERO.value,
                    padding_right=Size.SMALL.value,
                ),
                align="center",
                width="100%",
            )
        ),
        href=url,
        is_external=is_external,
        width="100%",
    )
