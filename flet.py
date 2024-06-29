import flet as ft
import os
import base64

def main(page: ft.Page):
    page.title = "Word File Downloader"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def download_file(e):
        # WordファイルのパスをFletアプリのアセットフォルダに置いてください
        file_path = os.path.join(os.path.dirname(__file__), "assets", "testfile.docx")
        
        if os.path.exists(file_path):
            with open(file_path, "rb") as file:
                content = file.read()
            
            # ファイルの内容をBase64エンコード
            base64_content = base64.b64encode(content).decode()
            
            # ダウンロードリンクを作成
            download_link = f'data:application/vnd.openxmlformats-officedocument.wordprocessingml.document;base64,{base64_content}'
            
            # JavaScriptを使用してダウンロードを開始
            page.launch_url(download_link)
            
            result.value = "ファイルのダウンロードを開始しました。"
        else:
            result.value = "ファイルが見つかりません。"
        
        page.update()

    download_button = ft.ElevatedButton("Word文書をダウンロード", on_click=download_file)
    result = ft.Text()

    page.add(
        ft.Column([
            download_button,
            result
        ], alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(target=main, view=ft.AppView.WEB_BROWSER)