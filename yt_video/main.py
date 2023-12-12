import flet as ft
from  moviepy import editor as mv
from pytube import YouTube

def main(page: ft.Page):
    page.appbar = ft.AppBar(
        title=ft.Text('Ytb Video Dolwander'),
        center_title=True
    )

    # Create snack bar here
    snack_bar = ft.SnackBar(ft.Text("", color=ft.colors.WHITE), bgcolor=ft.colors.BLACK26)
    page.add(snack_bar)

    def text_charged(e):
        print(e.control.value)
        try:
            video_details = YouTube(e.control.value)
            button.text = 'Download - ' + video_details.title
            image.src = video_details.thumbnail_url
            image.update()
            button.update()
            print(video_details.title)
        except Exception as ex:
            button.text = 'Download Video!'
            image.src = ''
            image.update()

            # Update the snack bar text
            snack_bar.text = "Not a Link"
            snack_bar.open = True
            snack_bar.update()
            print('Not a Link', ex)

    def download_file(e):
        if len(txt.value) == 0:
            print("Empty link")
        else:
            try:
                get_link = txt.value
                mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
                vid_clip = mv.VideoFileClip(mp4_video)
                vid_clip.close()
                snack_bar.text = "Video descargado ..."
                snack_bar.open = True
                snack_bar.update()
                print("Video descargado")
            except Exception as ex:
                snack_bar.text = "Not a YouTube URL or error"
                snack_bar.open = True
                snack_bar.update()
                print("Not a YouTube URL or error", ex)

    txt = ft.TextField(hint_text='Link', on_change=text_charged)
    image = ft.Image(src='')
    button = ft.ElevatedButton('Download Video!', on_click=download_file)

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        image,
        txt,
        button
    )

if __name__ == '__main__':
    ft.app(target=main)
