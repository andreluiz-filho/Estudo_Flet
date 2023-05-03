import flet as ft

def main(page: ft.Page):
    ola = ft.Text(value='Ola, Mundo!')
    page.controls.append(ola)
    page.update()

ft.app(target=main)