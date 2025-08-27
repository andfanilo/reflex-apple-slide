import reflex as rx


class AppState(rx.State):
    cpu_kpi: str = "3.5x"
    gpu_kpi: str = "6x"
    ml_kpi: str = "15x"
    battery_status: str = "20 Hours"


# Tailwind classes that I like but in CSS
bg_gray_100_css = "#E5E5E5"


def rx_gray_card(*children, **styles) -> rx.Component:
    return rx.flex(
        *children,
        flex_direction="column",
        align_items="center",
        justify_content="center",
        gap="0.8rem",
        padding="1rem",
        border_radius="0.5rem",
        background_color=bg_gray_100_css,
        height="100%",
        width="100%",
        **styles,
    )


def rx_kpi_row() -> rx.Component:
    return rx.flex(
        rx_gray_card(
            rx.image(
                src="/architecture_logo.png",
                width="33%",
            ),
            rx.box(
                "Unified Memory Architecture",
                width="50%",
                text_align="center",
            ),
            flex="1 1 0%",
        ),
        rx_gray_card(
            rx.box("Up to"),
            rx.box(
                AppState.cpu_kpi,
                font_weight="600",
                font_size="6.2rem",
                line_height="1",
                background="linear-gradient(to right, blue, purple)",
                background_clip="text",
                color="transparent",
            ),
            rx.box("Faster CPU"),
            flex="1 1 0%",
        ),
        rx_gray_card(
            rx.box("Up to"),
            rx.box(
                AppState.gpu_kpi,
                font_weight="600",
                font_size="6.2rem",
                line_height="1",
                background="linear-gradient(to right, purple, red)",
                background_clip="text",
                color="transparent",
            ),
            rx.box("Faster GPU"),
            flex="1 1 0%",
        ),
        rx_gray_card(
            rx.box("Up to"),
            rx.box(
                AppState.ml_kpi,
                font_weight="600",
                font_size="6.2rem",
                line_height="1",
                background="linear-gradient(to right, red, yellow)",
                background_clip="text",
                color="transparent",
            ),
            rx.box("Faster Machine Learning"),
            flex="1 1 0%",
        ),
        rx_gray_card(
            rx.flex(
                "Neural Engine",
                font_weight="600",
                font_size="3.5rem",
                line_height="1.1",
                text_align="center",
                padding_bottom="1rem",
                background="linear-gradient(to right, cyan, blue)",
                background_clip="text",
                color="transparent",
            ),
            flex="1 1 0%",
        ),
        flex="none",  # row should not grow nor shrink, keep container fixed height
        gap="0.5rem",
        height="25%",
    )


def rx_feature_row() -> rx.Component:
    return rx.flex(
        rx.flex(
            rx.flex(
                "MacOS Big Sur",
                flex="3",
                align_items="center",
                justify_content="center",
                border_radius="0.5rem",
                background_image="url('/apple_gradient.png')",
                color="white",
                font_weight="600",
                font_size="2rem",
            ),
            rx_gray_card(
                rx.image(
                    src="/apple_camera.png",
                    width="50%",
                ),
                rx.box(
                    "Advanced Camera ISP",
                ),
                flex="1",
            ),
            rx_gray_card(
                rx.flex(
                    "Industry-leading performance per Watt",
                    font_weight="600",
                    font_size="1.5rem",
                    line_height="1.2",
                    text_align="center",
                    background="linear-gradient(to right, cyan, blue)",
                    background_clip="text",
                    color="transparent",
                ),
                flex="1",
            ),
            flex="1",
            flex_direction="column",
            gap="0.5rem",
        ),
        rx.flex(
            rx.flex(
                rx.image(
                    src="/apple_computers.png",
                    width="75%",
                ),
                align_items="center",
                justify_content="center",
                flex="2",
            ),
            rx.flex(
                rx_gray_card(
                    rx.image(src="/apple_wifi.png"),
                    rx.box("Wifi-6"),
                ),
                rx_gray_card(
                    rx.image(src="/apple_devices.png"),
                    rx.box("iPhone and iPad apps"),
                ),
                rx_gray_card(
                    rx.image(src="/apple_lock.png"),
                    rx.box("Secure Enclave"),
                ),
                rx_gray_card(
                    rx.image(src="/apple_wave.png"),
                    rx.box("Universal Apps"),
                ),
                flex="1",
                gap="0.8rem",
            ),
            flex="2",
            flex_direction="column",
        ),
        rx.flex(
            rx_gray_card(
                rx.box("Up to"),
                rx.flex(
                    rx.box(
                        AppState.battery_status,
                        font_size="1.4rem",
                        font_weight="700",
                        color="white",
                        white_space="nowrap",
                    ),
                    padding="1rem 2rem",
                    border_radius="1rem",
                    background_color="green",
                ),
                rx.box("Battery Life"),
            ),
            rx_gray_card(
                rx.image(
                    src="m1_chip.png",
                    width="80%",
                ),
            ),
            flex="1",
            flex_direction="column",
            gap="0.5rem",
        ),
        # background_color="#93c5fd",
        flex_grow="1",  # row can grow to the rest of space, which is 75%
        gap="0.8rem",
    )


def index() -> rx.Component:
    return rx.box(
        rx.flex(
            rx_kpi_row(),
            rx_feature_row(),
            flex_direction="column",
            width="100%",
            height="100%",
            gap="0.5rem",
            padding="0.8rem",
        ),
        width="100%",
        height="100vh",
        # background_color="#fee2e2",
    )


app = rx.App()
app.add_page(index)
