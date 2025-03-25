import flet as ft

def main(page: ft.Page):
    page.title = "Моё первое Flet-приложение"
    page.vertical_alignment = "center"
    
    txt_name = ft.TextField(label="Введите имя")
    lbl_greeting = ft.Text()
    
    def say_hello(e):
        lbl_greeting.value = f"Привет, {txt_name.value}!"
        page.update()
    
    page.add(
        ft.Column(
            [
                txt_name,
                ft.ElevatedButton("Поздороваться", on_click=say_hello),
                lbl_greeting,
            ],
            alignment="center",
        )
    )

ft.app(target=main)
