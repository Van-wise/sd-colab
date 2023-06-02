# -*- coding: utf-8 -*-
import os
import base64
import subprocess
from urllib.parse import urlparse
from IPython.display import clear_output

sdw = base64.b64decode(("c3RhYmxlLWRpZmZ1c2lvbi13ZWJ1aQ==").encode('ascii')).decode('ascii')
webui_dir = f'/content/{sdw}'
gwebui_dir = f'/content/drive/MyDrive/{sdw}'

def download(url, model_dir):
    filename = os.path.basename(urlparse(url).path)
    pth = os.path.abspath(os.path.join(model_dir, filename))
    if not os.path.exists(pth):
        print('Downloading: ' + os.path.basename(url))
        cmd = f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M -d {model_dir} -o {filename} {url}"
        subprocess.run(cmd, shell=True, check=True)
    else:
        print(f"[1;32mThe model {filename} already exists[0m")

def cndown_colab():
    os.system(f"curl -o CN_models.txt https://raw.githubusercontent.com/Van-wise/sd-webui-colab/main/on_drive/cndown_colab.txt")
    mdldir = f"{webui_dir}/extensions/sd-webui-controlnet/models"

    if os.path.exists("CN_models.txt"):
        with open("CN_models.txt", 'r') as f:
            mdllnk = f.read().splitlines()

    if os.path.exists('CN_models.txt'):
        os.system('rm CN_models.txt CN_models_v2.txt')

    for lnk in mdllnk:
        download(lnk, mdldir)
        clear_output()

def cndown_drive():
    os.system(f"curl -o CN_models.txt https://raw.githubusercontent.com/Van-wise/sd-webui-colab/main/on_drive/cndown_colab.txt")
    mdldir = f"{gwebui_dir}/extensions/sd-webui-controlnet/models"

    if os.path.exists("CN_models.txt"):
        with open("CN_models.txt", 'r') as f:
            mdllnk = f.read().splitlines()

    if os.path.exists('CN_models.txt'):
        os.system('rm CN_models.txt CN_models_v2.txt')

    for lnk in mdllnk:
        download(lnk, mdldir)
        clear_output()