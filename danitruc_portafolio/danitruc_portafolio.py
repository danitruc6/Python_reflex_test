import reflex as rx
import danitruc_portafolio.styles.styles as styles
from danitruc_portafolio.styles.styles import Size as Size
from danitruc_portafolio.pages.index import index
from danitruc_portafolio.pages.courses import courses


class State(rx.State):
    """Define your state here."""


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    # theme=rx.theme(
    #     appearance="dark", has_background=True, radius="large", accent_color="teal"
    # ),
)
