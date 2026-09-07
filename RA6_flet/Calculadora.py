import flet as ft 
def main(page: ft.Page):
    page.title = "calc App"
    result = ft.Text(value="0")
    page.add(
        result,
        ft.Button("AC"), ft.Button("+/-"), ft.Button("%"), ft.Button("/"),
        ft.Button("7"), ft.Button("8"), ft.Button("9"), ft.Button("*"),
        ft.Button("4"), ft.Button("5"), ft.Button("6"), ft.Button("-"),
        ft.Button("1"), ft.Button("2"), ft.Button("3"), ft.Button("+"),
        ft.Button("0"), ft.Button("."), ft.Button("="),
        
        
    )
    from dataclasses import field
from dataclasses import field

import flet as ft


@ft.control
class CalcButton(ft.Button):
    expand: int = field(default_factory=lambda: 1)


@ft.control
class DigitButton(CalcButton):
    bgcolor: ft.Colors = ft.Colors.WHITE_24
    color: ft.Colors = ft.Colors.WHITE


@ft.control
class ActionButton(CalcButton):
    bgcolor: ft.Colors = ft.Colors.BLUE_100
    color: ft.Colors = ft.Colors.PINK_100


@ft.control
class ExtraActionButton(CalcButton):
    bgcolor: ft.Colors = ft.Colors.BLUE_GREY_100
    color: ft.Colors = ft.Colors.PURPLE_200


@ft.control
class CalculatorApp(ft.Container):
    def init(self):
        self.width = 350
        self.bgcolor = ft.Colors.PINK_300
        self.border_radius = ft.BorderRadius.all(20)
        self.padding = 20
        self.result = ft.Text(value="0", color=ft.Colors.WHITE, size=20)
        self.content = ft.Column(
            controls=[
                ft.Row(
                    controls=[self.result],
                    alignment=ft.MainAxisAlignment.END,
                ),
                ft.Row(
                    controls=[
                        ExtraActionButton(content="AC"),
                        ExtraActionButton(content="+/-"),
                        ExtraActionButton(content="%"),
                        ActionButton(content="/"),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(content="7"),
                        DigitButton(content="8"),
                        DigitButton(content="9"),
                        ActionButton(content="*"),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(content="4"),
                        DigitButton(content="5"),
                        DigitButton(content="6"),
                        ActionButton(content="-"),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(content="1"),
                        DigitButton(content="2"),
                        DigitButton(content="3"),
                        ActionButton(content="+"),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(content="0", expand=2),
                        DigitButton(content="."),
                        ActionButton(content="="),
                    ]
                ),
            ]
        )


def main(page: ft.Page):
    page.title = "Calc App"
    # create application instance
    calc = CalculatorApp()

    # add application's root control to the page
    page.add(calc)


ft.run(main)
    