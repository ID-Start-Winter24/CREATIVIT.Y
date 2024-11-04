from gradio.themes.base import Base


class CustomTheme(Base):
    def __init__(self):
        super().__init__()

        super().set(
            body_background_fill="white",
            body_background_fill_dark="white",
            input_background_fill="#ffffff",
            input_background_fill_dark="white"
        )