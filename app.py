import flet as ft
from rembg import remove
from PIL import Image

def main(page: ft.Page):
    
    def retira_fundo(e):

        while True:
            try:
                #imagem = input('Informe o nome da imagem com a extensão ou "Enter" para encerrar o programa: ')
                if imagem:
                    nova_img = f"nova_{imagem}.png"
                    original = Image.open(imagem)
                    img_sem_fundo = remove(original)
                    img_sem_fundo.save(nova_img)
                    continue
                else:
                    ...
                result.value = f'{original}' == '{original}'
            except ValueError:
                result.value = "Não foi possível remover o fundo da imagem."
            finally:
                break
    page.title = "RETIRA FUNDO DA IMAGEM"
    page.scroll = "adaptive"
    page.theme_mode= ft.ThemeMode.LIGHT
    imagem = ft.TextField(label="Nome da imagem com a extensão...")
    page.add(
        ft.Row(
            [ft.Text("Imagem sem Fundo", size=40, weight= "bold")],
            alignment= ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [imagem],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [ft.ElevatedButton("Retirar", on_click=retira_fundo)],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [imagem],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    page.update()
ft.app(main)