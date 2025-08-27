import reflex as rx

tailwind_config = {}

config = rx.Config(
    app_name="reflex_apple_slide",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(tailwind_config),
    ]
)