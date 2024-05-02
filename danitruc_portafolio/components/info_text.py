import reflex as rx
import danitruc_portafolio.styles.styles as styles
from danitruc_portafolio.styles.colors import TextColor as TextColor
from danitruc_portafolio.styles.colors import Color as Color

def info_text(title: str, body: str) -> rx.Component:
    return rx.text(
        rx.text(
            title, 
            font_weight="bold", 
            color=Color.PRIMARY.value, 
            as_="span"
            ),

        body, 
        font_size=styles.Size.MEDIUM.value,
        color=TextColor.BODY.value
    )