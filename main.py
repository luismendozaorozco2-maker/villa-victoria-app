import flet as ft

def main(page: ft.Page):
    page.title = "Villa Victoria"
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # En versiones nuevas, usamos un control de tipo 'Html' o cargamos la URL
    # Si WebView falla, usamos el redireccionamiento directo para la prueba
    def launch_web(e):
        page.launch_url("https://www.villavictoria.com.pe")

    # Creamos una interfaz sencilla con un botón grande para probar
    # Esto es más seguro mientras resolvemos el tema de drivers en Linux
    page.add(
        ft.Column([
            ft.Container(
                content=ft.Text("Bienvenido a Villa Victoria", size=20, weight="bold"),
                alignment=ft.alignment.center,
                padding=20
            ),
            ft.ElevatedButton(
                "Abrir Portal Web", 
                icon=ft.icons.WEB,
                on_click=launch_web,
                width=300
            )
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

# Usamos ft.app (aunque diga deprecated, para escritorio sigue siendo la base)
# pero lo lanzamos con un pequeño ajuste para evitar el error de sesión
if __name__ == "__main__":
    ft.app(target=main)
