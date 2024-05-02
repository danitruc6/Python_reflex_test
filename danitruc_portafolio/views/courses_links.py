import reflex as rx
from sqlalchemy import False_
from danitruc_portafolio.components.link_button import link_button
from danitruc_portafolio.components.title import title
from danitruc_portafolio.styles.styles import Spacing
from danitruc_portafolio.routes import Route


def courses_links() -> rx.Component:
    return rx.vstack(
        title("Cursos gratis"),
        link_button(
            "Mech Master",
            "Aprende sobre teclados mecanicos custom",
            Route.COURSES.value,
            "book",
            is_external=False,
        ),
        link_button("Nueva pagina de curso", "Projects", "#", "book-copy"),
        width="100%",
        spacing=Spacing.SMALL.value,
    )
