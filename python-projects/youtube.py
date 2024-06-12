from pytube import YouTube
import tkinter as tk  # 2D graphics library
from tkinter import filedialog


def download_video(url, save_path):
    try:
        yt = YouTube(url)  # Get instance of YouTube video
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print(e)


def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder


# Ensures we are directly running this file
if __name__ == "__main__":
    # Instantiates TK module and creates TK window
    root = tk.Tk()
    root.withdraw()  # Hide window

    video_url = input("Please enter a YouTube url: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Started download...")
        download_video(video_url, save_dir)
    else:
        print("Invalid save location.")
