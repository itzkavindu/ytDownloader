import os
import tkinter
import webbrowser

import customtkinter
import ffmpy
from pytube import YouTube

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("700x500")
app.title("YTDownloader")

# ----Fonts----
ytdwntitle = ("BebasNeue", 25)
finished = ("IndieFlower", 15)
btns = ("RobotoMono", 10)
creditfnt = ("Cantarell", 10)


def create_toplevel():
    window = customtkinter.CTkToplevel()
    window.geometry("400x200")

    finishedwind = customtkinter.CTkLabel(window, text="Successfully Downloaded", text_font=finished)
    finishedwind.pack(side="top", fill="both", expand=True, padx=40, pady=40)
    window.title('YTDOWNLOADER - Successfully Downloaded')


def run_app():
    link = ytlink.get()
    yt = YouTube(link)

    ys = yt.streams.get_highest_resolution()

    ys.download(output_path=destinationtext.get())
    create_toplevel()


def confirm():
    link = ytlink.get()
    yt = YouTube(link)

    vidtitle = yt.title
    numviews = yt.views
    vidlen = yt.length

    title = customtkinter.CTkLabel(master=frame, text=f"Title : {vidtitle}")
    title.place(relx=0.05, rely=0.35, anchor="w")

    views = customtkinter.CTkLabel(master=frame, text=f"Number of Views : {numviews}")
    views.place(relx=0.05, rely=0.5, anchor="w")

    length = customtkinter.CTkLabel(master=frame,
                                    text=f"Length of Video : {vidlen} secs")
    length.place(relx=0.05, rely=0.65, anchor="w")


def audio():
    link = ytlink.get()
    yt = YouTube(link)

    ys = yt.streams.filter(only_audio=True, file_extension='webm').first()
    ys.download(output_path=destinationtext.get())
    ff = ffmpy.FFmpeg(
        inputs={f'{yt.title}.webm': None},
        outputs={f'{yt.title} - Audio.mp3': None})
    ff.run()
    os.remove(f'{yt.title}.webm')
    create_toplevel()


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
                               fg_color="#757575")
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

destinationtext = customtkinter.CTkEntry(master=app,
                                         placeholder_text="Destination | If you do not add a destination the video "
                                                          "will be "
                                                          "saved in the default location",
                                         width=550,
                                         justify="center")
destinationtext.place(relx=0.1, rely=0.3)

# ------------------------Confirm Button-------------------------
confirmbtn = customtkinter.CTkButton(master=app, text="Confirm", command=confirm, fg_color="white", text_color="black",
                                     corner_radius=25, hover_color="#757575", width=200, text_font=btns)
confirmbtn.place(relx=0.5, rely=0.49, anchor=tkinter.CENTER)

# -----------------------Download Button-------------------------

downloadbtn = customtkinter.CTkButton(master=app, text="Download",
                                      command=run_app,
                                      fg_color="white",
                                      text_color="black",
                                      corner_radius=25,
                                      hover_color="#757575", width=200, cursor="hand1", text_font=btns)
downloadbtn.place(relx=0.65, rely=0.42, anchor=tkinter.CENTER)

# ---------------------Download audio Button-----------------------

audiodown = customtkinter.CTkButton(master=app, text="Download MP3",
                                    command=audio,
                                    fg_color="white",
                                    text_color="black",
                                    corner_radius=25,
                                    hover_color="#757575", width=200, cursor="hand1", text_font=btns)
audiodown.place(relx=0.355, rely=0.42, anchor=tkinter.CENTER)

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
app.mainloop()
