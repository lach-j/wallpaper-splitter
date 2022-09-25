from PIL import Image
import json
from pathlib import Path
import argparse
import os

def main(args):
    filename, file_extension = os.path.splitext(args.inputfile)
    extension = args.extension if args.extension else file_extension


    im = Image.open(args.inputfile)
    width, height = im.size

    with open("config.json", "r") as config_file:
        screens = json.load(config_file)

    screen_width = 0
    screen_height = 0
    
    for screen in screens:
        curr_width = screen["x"] + screen["width"]
        if curr_width > screen_width:
            screen_width = curr_width
        curr_height = screen["y"] + screen["height"]
        if curr_width > screen_height:
            screen_height = curr_height

    image_ratio = width/height
    screen_ratio = screen_width/screen_height

    if (screen_ratio > image_ratio):
        resize_w = screen_width
        resize_h = resize_w / image_ratio
    else:
        resize_h = screen_height
        resize_w = resize_h * image_ratio

    im = im.resize((round(resize_w), round(resize_h)))

    x_offset = 0
    y_offset = 0

    if (screen_width < resize_w):
        if args.align_horizontal == "centre":
            x_offset = round(resize_w/2 - screen_width/2)
        elif args.align_horizontal == "left":
            x_offset = 0
        else:
            x_offset = resize_w - screen_width

    if (screen_height < resize_h):
        if args.align_vertical == "centre":
            y_offset = round(resize_h/2 - screen_height/2)
        elif args.align_vertical == "top":
            y_offset = 0
        else:
            y_offset = resize_h - screen_height

    for screen in screens:
        left = screen["x"] + x_offset
        top = screen["y"] + y_offset
        right = left + screen["width"]
        bottom = top + screen["height"]
        name = screen["name"]
    
        im1 = im.crop((left, top, right, bottom))

        basename = args.out if args.out else filename

        Path(basename).mkdir(parents=True, exist_ok=True)

        im1.save(f"{basename}/{name}.{extension}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('inputfile', type=str, metavar="input-file", help="path to the image to be split")
    parser.add_argument('--out', '-o', type=str, help="path of the directory to save output files (default: name of input file)")
    parser.add_argument('--extension', '-x', type=str, help="file extension of output images (default: match input file)")
    parser.add_argument('--align-horizontal', '-hz', type=str, default="centre", choices=["left", "centre", "right"], help="horizontal alignment of values (default: centre)")
    parser.add_argument('--align-vertical', '-v', type=str, default="centre", choices=["top", "centre", "bottom"], help="vertical alignment of values (default: centre)")
    args = parser.parse_args()
    
    main(args)