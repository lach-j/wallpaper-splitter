# wallpaper-splitter

Wallpaper splitting tool created for desktop environments that do not support multi-monitor spanning wallpapers.

## Installation

```
pip install -r requirements.txt
```

## Usage
```
usage: wallpaper-splitter.py [-h] [--out OUT] [--extension EXTENSION] [--align-horizontal {left,centre,right}] [--align-vertical {top,centre,bottom}] [--use-config] input-file

positional arguments:
  input-file            path to the image to be split

options:
  -h, --help            show this help message and exit
  --out OUT, -o OUT     path of the directory to save output files (default: name of input file)
  --extension EXTENSION, -x EXTENSION
                        file extension of output images (default: match input file)
  --align-horizontal {left,centre,right}, -hz {left,centre,right}
                        horizontal alignment of values (default: centre)
  --align-vertical {top,centre,bottom}, -v {top,centre,bottom}
                        vertical alignment of values (default: centre)
  --use-config, -c      use if the config.json file should be used
```