import tkinter
import customtkinter
from pytube import YouTube


def downloadMP4():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download()
    except Exception as err:
        finishLabel.configure(text=f"Youtube link is invalid: {err}", text_color="red")
    else:
        finishLabel.configure(text="Download complete", text_color="green")


def downloadMP3():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_audio_only()

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download()
    except Exception as err:
        finishLabel.configure(text=f"Youtube link is invalid: {err}", text_color="red")
    else:
        finishLabel.configure(text="Download complete", text_color="green")



def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    progressPercentage.configure(text=per+"%")
    progressPercentage.update()

    # Update progress bar
    progressBar.set(float(percentage_of_completion) / 100)


# System Setting
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")


# Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Youtube MP4")
title.pack(padx=10, pady=5)

# Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=450, height=40, placeholder_text="insert a video link", textvariable=url_var)
link.pack()

# Finished downloading
finishLabel = customtkinter.CTkButton(app, text="")
finishLabel.pack(padx=10, pady=5)

# Progress percentage
progressPercentage = customtkinter.CTkLabel(app, text="0%")
progressPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download Button
# MP3
downloadmp3 = customtkinter.CTkButton(app, text="Download MP3", command=downloadMP3)
downloadmp3.pack(padx=10, pady=10)

# MP4
downloadmp4 = customtkinter.CTkButton(app, text="Download MP4", command=downloadMP4)
downloadmp4.pack(padx=10, pady=10)

# Run app
app.mainloop()

