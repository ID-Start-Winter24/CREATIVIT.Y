from gradio.themes.base import Base




class CustomTheme(Base):
    def __init__(self):
        super().__init__()

        super().set(
            body_background_fill="#1e1e2f",
            body_background_fill_dark="#1e1e2f",
            input_background_fill="#2f2f3f",
            input_background_fill_dark="#2f2f3f",
        )

