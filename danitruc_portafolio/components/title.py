import reflex as rx
import danitruc_portafolio.styles.styles as styles
from danitruc_portafolio.styles.styles import Size, Spacing
    
def title(text: str) -> rx.Component:
    return rx.heading(
        text, 
        size=Spacing.BIG.value,
        style=styles.title_style
        )
