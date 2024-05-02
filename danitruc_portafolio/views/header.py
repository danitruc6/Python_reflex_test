import reflex as rx
from danitruc_portafolio.components.link_icon import link_icon
from danitruc_portafolio.components.info_text import info_text
from danitruc_portafolio.styles.styles import Size, Spacing
from danitruc_portafolio.styles.colors import TextColor as TextColor
from danitruc_portafolio.styles.colors import Color as Color


def header(details=True) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                fallback="DH",
                src="/darker_avatar.jpeg",
                size=Spacing.MEDIUM_BIG.value,
                color=TextColor.BODY.value,
                bg=Color.CONTENT.value,
                padding="2px",
                border="4px",
                border_color=Color.PRIMARY.value,
                # radius="full",
            ),
            rx.vstack(
                rx.heading("Daniel H.", size=Spacing.BIG.value),
                rx.text("@danitruc6", color=TextColor.BODY.value),
                rx.hstack(
                    link_icon("linkedin", "https://linkedin.com/danitruc6", "linkedin"),
                    link_icon("twitter", "https://x.com/danitruc6", "twitter"),
                ),
                align_items="start",
                spacing=Spacing.SMALL.value,
            ),
            spacing=Spacing.LARGE.value,
        ),
        rx.cond(
            details,
            rx.vstack(
                rx.flex(
                    info_text("+9 ", "años de experiencia"),
                    rx.spacer(),
                    info_text("10+ ", "aplicaciones creadas"),
                    rx.spacer(),
                    info_text("3 ", "seguidores"),
                    width="100%",
                ),
                rx.text(
                    """Soy un ingeniero electrico, 
                con 9 años de experiencia en el mundo de diseño de semi conductores y 
                recientemente aprendiendo desarrollo web enfocado en el 
                lenguaje de programacion Python. Ademas de que me estoy iniciando 
                en el IA haciendo uso de machine learning.""",
                    color=TextColor.BODY.value,
                    font_size=Size.MEDIUM.value,
                ),
                width="100%",
                spacing=Spacing.DEFAULT.value,
            ),
        ),
        spacing=Spacing.DEFAULT.value,
        align_items="start",
    )
