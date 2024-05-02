import reflex as rx
from danitruc_portafolio.styles.styles import Size


def link_icon(image: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.icon(
            tag=image, width=Size.DEFAULT.value, height=Size.DEFAULT.value, alt=alt
        ),
        href=url,
        is_external=True,
    )
