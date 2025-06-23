from moviepy.editor import VideoFileClip

clip = VideoFileClip("/Users/yut0takagi/Develop/kokkai-analytics/ src/画面収録 2025-06-23 18.26.37.mov")
clip = clip.subclip(0, 20)  # 必要なら最初の5秒だけ抽出
clip.write_gif("output.gif")