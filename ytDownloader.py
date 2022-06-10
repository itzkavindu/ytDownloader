import webbrowser

import customtkinter
import tkinter
from pytube import YouTube

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("700x500")
app.title("YTDownloader")

ytdwntitle = ("BebasNeue", 25)
finished = ("IndieFlower", 15)
btns = ("RobotoMono", 10)
creditfnt = ("Cantarell", 10)


def create_toplevel():
    window = customtkinter.CTkToplevel()
    window.geometry("400x200")

    # create label on CTkToplevel window
    finishedwind = customtkinter.CTkLabel(window, text="Successfully Downloaded", text_font=finished)
    finishedwind.pack(side="top", fill="both", expand=True, padx=40, pady=40)
    window.title('YTDOWNLOADER - Successfully Downloaded')


def run_app():
    link = entry.get()
    yt = YouTube(link)

    print()
    print("Title          : ", yt.title)
    print("Number of views: ", yt.views)
    print("Length of video: ", yt.length)
    print("Rating of video: ", yt.rating)

    ys = yt.streams.get_highest_resolution()

    print()
    print(yt.title, "is Now Downloading...")
    ys.download(output_path=label.get())
    print()
    print("---Download completed---")
    create_toplevel()


def confirm():
    link = entry.get()
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


def developer():
    webbrowser.open_new(r"https://github.com/itzkavindu/")


def openweb():
    webbrowser.open_new(r"https://github.com/itzkavindu/ytDownloader")


frame = customtkinter.CTkFrame(master=app,
                               width=600,
                               height=150,
                               corner_radius=10,
                               border_width=7,
                               border_color="black",
                               fg_color="#757575")
frame.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

mainlab = customtkinter.CTkLabel(master=app, text="YTDOWNLOADER", text_font=ytdwntitle)
mainlab.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

confirmbtn = customtkinter.CTkButton(master=app, text="Confirm", command=confirm, fg_color="white", text_color="black",
                                     corner_radius=25, hover_color="#757575", width=200, text_font=btns)
confirmbtn.place(relx=0.5, rely=0.49, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="Download",
                                 command=run_app,
                                 fg_color="white",
                                 text_color="black",
                                 corner_radius=25,
                                 hover_color="#757575", width=200, cursor="hand1", text_font=btns)
button.place(relx=0.5, rely=0.42, anchor=tkinter.CENTER)

entry = customtkinter.CTkEntry(master=app,
                               placeholder_text="YouTube Link | Enter the link of the YouTube video you wish to "
                                                "Download",
                               width=550, justify="center")
entry.place(relx=0.1, rely=0.2)

label = customtkinter.CTkEntry(master=app,
                               placeholder_text="Destination | If you do not add a destination the video will be "
                                                "saved in the default location",
                               width=550,
                               justify="center")
label.place(relx=0.1, rely=0.3)
githubrepo = customtkinter.CTkButton(master=app, text="YTDownloader on GitHub", command=openweb, corner_radius=50,
                                     cursor="hand1", fg_color="white", text_color="#171515", hover_color="#757575",
                                     width=900, text_font=creditfnt)
githubrepo.place(relx=0.5, rely=0.9, anchor="center")

dev = customtkinter.CTkButton(master=app, text="YTDownloader by Kavindu Nimsara 2022", width=800, fg_color="black",
                              text_color="white", command=developer, hover_color="grey", cursor="heart",
                              text_font=creditfnt)
dev.place(relx=0.5, rely=0.95, anchor=tkinter.CENTER)

app.mainloop()
