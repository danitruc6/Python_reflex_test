import reflex as rx
from danitruc_portafolio.components.navbar import navbar
from danitruc_portafolio.components.footer import footer
from danitruc_portafolio.views.header import header
from danitruc_portafolio.views.index_links import index_links
from danitruc_portafolio.styles.styles import Size as Size
import danitruc_portafolio.utils as utils
import danitruc_portafolio.styles.styles as styles


@rx.page(
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.index_meta,
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                index_links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value,
            )
        ),
        footer(),
    )
