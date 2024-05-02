import reflex as rx
from reflex.components.el import details
from danitruc_portafolio.components.navbar import navbar
from danitruc_portafolio.components.footer import footer
from danitruc_portafolio.views.header import header
from danitruc_portafolio.views.courses_links import courses_links
import danitruc_portafolio.styles.styles as styles
from danitruc_portafolio.styles.styles import Size as Size
import danitruc_portafolio.utils as utils
from danitruc_portafolio.routes import Route


@rx.page(
    route=Route.COURSES.value,
    title=utils.courses_title,
    description=utils.courses_description,
    image=utils.preview,
    meta=utils.courses_meta,
)
def courses() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(details=False),
                courses_links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value,
            )
        ),
        footer(),
    )
