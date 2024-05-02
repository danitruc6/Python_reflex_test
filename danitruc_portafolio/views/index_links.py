import reflex as rx
from sqlalchemy import False_
from danitruc_portafolio.components.link_button import link_button
from danitruc_portafolio.components.title import title
from danitruc_portafolio.styles.styles import Spacing
from danitruc_portafolio.routes import Route


def index_links() -> rx.Component:
    return rx.vstack(
        title("Coding links"),
        link_button(
            "Cursos",
            "Test de una pagina de cursos",
            Route.COURSES.value,
            "book",
            is_external=False,
        ),
        link_button("Github", "Projects", "https://github.com/danitruc6", "github"),
        link_button(
            "Youtube", "video demos", "https://youtube.com/danitruc6", "youtube"
        ),
        title("Redes Sociales"),
        link_button(
            "Instagram", "Profile page", "https://instagram.com/danitruc6", "instagram"
        ),
        link_button(
            "Facebook", "Profile page", "https://facebook.com/danitruc6", "facebook"
        ),
        link_button("X", "Profile page", "https://x.com/danitruc6", "twitter"),
        link_button("Reddit", "Profile page", "https://reddit.com/rowold", "text"),
        title("Contacto"),
        link_button(
            "Email", "danitruc6@hotmail.com", "mailto:danitruc6@hotmail.com", "mail"
        ),
        width="100%",
        spacing=Spacing.SMALL.value,
    )
