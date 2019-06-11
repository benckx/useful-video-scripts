import os
import subprocess

from PIL import Image, ImageDraw, ImageFont

black = (0, 0, 0)
white = (255, 255, 255)
font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 28, encoding="unic")
fps = 24
minutes = 5
frames_directory = 'frames'


def main():
  os.mkdir(frames_directory)
  nbr_of_frames = fps * minutes * 60

  for i in range(1, nbr_of_frames + 1):
    frame_idx = '{:010d}'.format(i)
    frame_file = frame_idx + '.png'
    sec = (i / fps)

    img = Image.new('RGB', (640, 360), color=white)
    draw = ImageDraw.Draw(img)
    draw.text((50, 50), "frame: {}".format(frame_idx), font=font, fill=black)
    draw.text((50, 100), "timestamp: {}".format(sec), font=font, fill=black)
    img.save(frames_directory + '/' + frame_file)

  command = 'ffmpeg -framerate {} -f image2 -i {}/%*.png -c:v libx264 -crf 25 -pix_fmt yuv420p {}'.format(fps, frames_directory, 'output.mp4')
  subprocess.run(command, shell=True)

if __name__ == "__main__":
  main()
