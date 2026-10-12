from kivy.app import App
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window


class AIVideoCreatorApp(App):
    title = "AI Video Creator"

    def build(self):
        Window.clearcolor = (0.055, 0.07, 0.11, 1)

        root = BoxLayout(
            orientation="vertical",
            padding=dp(18),
            spacing=dp(12),
        )

        header = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height=dp(105),
            spacing=dp(5),
        )

        header.add_widget(Label(
            text="[b]AI VIDEO CREATOR[/b]",
            markup=True,
            font_size="25sp",
            color=(0.35, 0.75, 1, 1),
        ))

        header.add_widget(Label(
            text="Your AI-powered video production studio",
            font_size="14sp",
            color=(0.82, 0.86, 0.92, 1),
        ))

        root.add_widget(header)

        scroll = ScrollView()
        menu = BoxLayout(
            orientation="vertical",
            spacing=dp(12),
            size_hint_y=None,
            padding=(0, dp(5)),
        )
        menu.bind(minimum_height=menu.setter("height"))

        features = [
            ("AI Drama Editor", "Create and edit drama scenes"),
            ("Music Video Editor", "Make videos for your music"),
            ("Advertisement Video Editor", "Create promotional videos"),
            ("Video Tools", "Cut, merge, subtitles and overlays"),
            ("Auto-Edit & Publish", "Prepare videos for social platforms"),
        ]

        for name, description in features:
            button = Button(
                text=f"[b]{name}[/b]\n[size=13sp]{description}[/size]",
                markup=True,
                size_hint_y=None,
                height=dp(82),
                background_normal="",
                background_color=(0.12, 0.20, 0.31, 1),
                color=(1, 1, 1, 1),
                halign="center",
                valign="middle",
            )
            button.bind(
                size=lambda instance, value: setattr(
                    instance, "text_size",
                    (value[0] - dp(20), None)
                )
            )
            button.bind(on_release=lambda instance, feature=name:
                        self.show_feature(feature))
            menu.add_widget(button)

        scroll.add_widget(menu)
        root.add_widget(scroll)

        root.add_widget(Label(
            text="AI Video Creator • Initial Preview",
            size_hint_y=None,
            height=dp(30),
            font_size="12sp",
            color=(0.65, 0.70, 0.78, 1),
        ))

        return root

    def show_feature(self, feature):
        from kivy.uix.popup import Popup

        Popup(
            title=feature,
            content=Label(
                text="This feature is being prepared.",
                halign="center",
                valign="middle",
            ),
            size_hint=(0.85, 0.3),
        ).open()


if __name__ == "__main__":
    AIVideoCreatorApp().run()
