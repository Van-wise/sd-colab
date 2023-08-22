# -*- coding: utf-8 -*-
import os
import base64
import subprocess
from urllib.parse import urlparse
from IPython.display import clear_output

webui_dir = f'/content/sd'
gwebui_dir = f'/content/drive/MyDrive/sd'

def download(url, model_dir):
    filename = os.path.basename(urlparse(url).path)
    pth = os.path.abspath(os.path.join(model_dir, filename))
    if not os.path.exists(pth):
        print('Downloading: ' + os.path.basename(url))
        cmd = f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M -d {model_dir} -o {filename} {url}"
        subprocess.run(cmd, shell=True, check=True)
    else:
        print(f"[1;32mThe model {filename} already exists[0m")

def cndown_sd15_colab():
    os.system(f"curl -o CN_models.txt https://raw.githubusercontent.com/Van-wise/sd-colab/main/cndown_colab.txt")
    mdldir = f"{webui_dir}/extensions/sd-controlnet/models"

    if os.path.exists("CN_models.txt"):
        with open("CN_models.txt", 'r') as f:
            mdllnk = f.read().splitlines()

    if os.path.exists('CN_models.txt'):
        os.system('rm CN_models.txt')

    for lnk in mdllnk:
        download(lnk, mdldir)
        clear_output()

def cndown_sd15_drive():
    os.system(f"curl -o CN_models.txt https://raw.githubusercontent.com/Van-wise/sd-colab/main/cndown_colab.txt")
    mdldir = f"{gwebui_dir}/extensions/sd-controlnet/models"

    if os.path.exists("CN_models.txt"):
        with open("CN_models.txt", 'r') as f:
            mdllnk = f.read().splitlines()

    if os.path.exists('CN_models.txt'):
        os.system('rm CN_models.txt')

    for lnk in mdllnk:
        download(lnk, mdldir)
        clear_output()

def cndown_sdxl_colab():
    os.system(f"curl -o CN_models.txt https://raw.githubusercontent.com/Van-wise/sd-colab/main/cndown_colab.txt")
    mdldir = f"{webui_dir}/extensions/sd-controlnet/models"

    if os.path.exists("CN_models.txt"):
        with open("CN_models.txt", 'r') as f:
            mdllnk = f.read().splitlines()

    if os.path.exists('CN_models.txt'):
        os.system('rm CN_models.txt')

    for lnk in mdllnk:
        download(lnk, mdldir)
        clear_output()

def cndown_sdxl_drive():
    os.system(f"curl -o CN_models.txt https://raw.githubusercontent.com/Van-wise/sd-colab/main/cndown_colab.txt")
    mdldir = f"{gwebui_dir}/extensions/sd-controlnet/models"

    if os.path.exists("CN_models.txt"):
        with open("CN_models.txt", 'r') as f:
            mdllnk = f.read().splitlines()

    if os.path.exists('CN_models.txt'):
        os.system('rm CN_models.txt')

    for lnk in mdllnk:
        download(lnk, mdldir)
        clear_output()