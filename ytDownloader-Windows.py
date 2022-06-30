import os
import ssl
import webbrowser
from tkinter import PhotoImage
from tkinter import filedialog

import customtkinter
import ffmpy
import pyglet
import tkinter
from pytube import YouTube

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("700x500")
app.title("YTDownloader")
app.resizable(False, False)
app.iconphoto(True, PhotoImage(file="ytdownloader.ico"))

# ----Fonts----
pyglet.font.add_file('Fonts/BebasNeue-Regular.ttf')
pyglet.font.add_file('Fonts/Cantarell-Regular.ttf')
pyglet.font.add_file('Fonts/RobotoMono-VariableFont_wght.ttf')
pyglet.font.add_file('Fonts/IndieFlower-Regular.ttf')

ytdwntitle = ("BebasNeue-Regular", 25)
finished = ("IndieFlower-Regular", 15)
btns = ("RobotoMono-VariableFont_wght", 10)
creditfnt = ("Cantarell-Regular", 10)

# ----Default file path----
filepath = os.path.join(os.path.expanduser("~"), "Desktop")


def main():
    ssl._create_default_https_context = ssl._create_unverified_context
    directory(True)
    app.mainloop()


def create_toplevel(title, message):
    window = customtkinter.CTkToplevel()
    window.geometry("400x200")

    finishedwind = customtkinter.CTkLabel(window, text=message, text_font=finished)
    finishedwind.pack(side="top", fill="both", expand=True, padx=40, pady=40)
    window.title(title)


def confirm():
    link = ytlink.get()
    if not link:
        create_toplevel("YTDOWNLOADER - Error", "No valid link in input field")
    else:
        yt = YouTube(link)

        vidtitle = yt.title
        numviews = yt.views
        vidlen = yt.length

        title = customtkinter.CTkLabel(master=frame, text=f"Title : {vidtitle}")
        title.place(relx=0.05, rely=0.35, anchor="w")

        views = customtkinter.CTkLabel(master=frame, text=f"Number of Views : {numviews:,}")
        views.place(relx=0.05, rely=0.5, anchor="w")

        length = customtkinter.CTkLabel(master=frame,
                                        text=f"Length of Video : {vidlen} secs")
        length.place(relx=0.05, rely=0.65, anchor="w")


def download_mp4():
    link = ytlink.get()
    if not link:
        create_toplevel("YTDOWNLOADER - Error", "No valid link in input field")
    else:
        confirm()
        yt = YouTube(link)

        ys = yt.streams.get_highest_resolution()

        ys.download(output_path=filepath)
        create_toplevel("YTDOWNLOADER - Successfully Downloaded", "Successfully Downloaded")


def download_mp3():
    link = ytlink.get()
    if not link:
        create_toplevel("YTDOWNLOADER - Error", "No valid link in input field")
    else:
        confirm()
        yt = YouTube(link)

        ys = yt.streams.filter(only_audio=True, file_extension='webm').first()
        ys.download(output_path=filepath, filename="Output.webm")
        ff = ffmpy.FFmpeg(
            inputs={f'{filepath}/Output.webm': None},
            outputs={f'{filepath}/{yt.title} - Audio.mp3': None})
        ff.run()
        os.remove(f'{filepath}/Output.webm')

        create_toplevel("YTDOWNLOADER - Successfully Downloaded", "Successfully Downloaded")


def download_webm():
    link = ytlink.get()
    if not link:
        create_toplevel("YTDOWNLOADER - Error", "No valid link in input field")
    else:
        confirm()

        yt = YouTube(link)

        ys = yt.streams.filter(file_extension='webm').first()
        ys.download(output_path=filepath)

        create_toplevel("YTDOWNLOADER - Successfully Downloaded", "Successfully Downloaded")


def developer():
    webbrowser.open_new(r"https://github.com/itzkavindu/")


def openweb():
    webbrowser.open_new(r"https://github.com/itzkavindu/ytDownloader")


# -----------------------------Frame---------------------------

frame = customtkinter.CTkFrame(master=app,
                               width=600,
                               height=150,
                               corner_radius=10,
                               border_width=7,
                               border_color="black",
                               fg_color="#181818")
frame.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

# ----------------------------Title----------------------------

mainlab = customtkinter.CTkLabel(master=app, text="YTDOWNLOADER", text_font=ytdwntitle)
mainlab.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

# ----------------------------Entry----------------------------

ytlink = customtkinter.CTkEntry(master=app,
                                placeholder_text="YouTube Link | Enter the link of the YouTube video you wish to "
                                                 "Download",
                                width=550, justify="center")
ytlink.place(relx=0.1, rely=0.2)

# ----------------------Destination-----------------------------

destinationtext = customtkinter.CTkLabel(master=app,
                                         text="Destination | Select the destination by clicking the browse button",
                                         width=550,
                                         justify="center",
                                         fg_color="#424242")
destinationtext.place(relx=0.1, rely=0.3)


# ----------------------Open Directory-----------------------------
def directory(first_run=False):
    global filepath
    if first_run:
        destinationtext.configure(text=filepath, state="disabled")
    else:
        filepath = filedialog.askdirectory(title="Select A Dir")
    destinationtext.configure(text=filepath, state="disabled")


# ------------------------Confirm Button-------------------------
confirmbtn = customtkinter.CTkButton(master=app, text="Confirm", command=confirm, fg_color="white", text_color="black",
                                     corner_radius=25, hover_color="#757575", width=230, text_font=btns)
confirmbtn.place(relx=0.329, rely=0.5, anchor=tkinter.CENTER)

# -----------------------Download Button-------------------------

downloadbtn = customtkinter.CTkButton(master=app, text="Download .MP4",
                                      command=download_mp4,
                                      fg_color="white",
                                      text_color="black",
                                      corner_radius=25,
                                      hover_color="#757575", width=160, cursor="hand1", text_font=btns)
downloadbtn.place(relx=0.494, rely=0.42, anchor=tkinter.CENTER)

# ---------------------Download audio Button-----------------------

audiodown = customtkinter.CTkButton(master=app, text="Download .MP3",
                                    command=download_mp3,
                                    fg_color="white",
                                    text_color="black",
                                    corner_radius=25,
                                    hover_color="#757575", width=160, cursor="hand1", text_font=btns)
audiodown.place(relx=0.25, rely=0.42, anchor=tkinter.CENTER)

# ---------------------Download audio Button-----------------------

webmdown = customtkinter.CTkButton(master=app, text="Download .WEBM",
                                   command=download_webm,
                                   fg_color="white",
                                   text_color="black",
                                   corner_radius=25,
                                   hover_color="#757575", width=160, cursor="hand1", text_font=btns)
webmdown.place(relx=0.74, rely=0.42, anchor=tkinter.CENTER)

# -----------------------OpenDir Button-------------------------

opendir = customtkinter.CTkButton(master=app, text="Browse",
                                  command=directory,
                                  fg_color="white",
                                  text_color="black",
                                  corner_radius=25,
                                  hover_color="#757575", width=230, cursor="hand1", text_font=btns)
opendir.place(relx=0.68, rely=0.5, anchor=tkinter.CENTER)

# --------------YTDownloader on GitHub Button---------------------

githubrepo = customtkinter.CTkButton(master=app, text="YTDownloader on GitHub", command=openweb, corner_radius=50,
                                     cursor="hand1", fg_color="white", text_color="#171515", hover_color="#757575",
                                     width=900, text_font=creditfnt)
githubrepo.place(relx=0.5, rely=0.9, anchor="center")

# ---------YTDownloader by Kavindu Nimsara 2022 Button-------------

dev = customtkinter.CTkButton(master=app, text="YTDownloader by Kavindu Nimsara 2022", width=800, fg_color="black",
                              text_color="white", command=developer, hover_color="grey", cursor="heart",
                              text_font=creditfnt)
dev.place(relx=0.5, rely=0.95, anchor=tkinter.CENTER)

# -----------------------------------------------------------------
if __name__ == "__main__":
    main()
