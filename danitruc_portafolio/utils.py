import reflex as rx

# comun
def lang():
    return rx.script("document.documentElement.lang='es'")
preview = "preview.png"

_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview},
]

# index
index_title = "Danitruc6's Link Bio"
index_description = "Hola, esta es mi pagina de link bio, con links a mis redes y repos"
index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
index_meta.extend(_meta)

# courses
courses_title = "Danitruc | cursos"
courses_description = "En esta pagina van a estar los cursos"
courses_meta = [
    {"name": "og:title", "content": courses_title},
    {"name": "og:description", "content": courses_description},
]
courses_meta.extend(_meta)
