import torch
import hydra
import easyocr
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np
import pathlib
import datetime


def make_save_dir(save_path):
    now = datetime.datetime.now()

    current_time =  now.strftime("%Y-%m-%d-%H-%M")
    save_path = pathlib.Path(os.path.join(save_path, current_time))

    if not save_path.exists():
        save_path.mkdir()
    
    return save_path


def save_result_img(img, result, save_path):
    plt.rcParams["font.family"] = "IPAGothic"
    print(matplotlib.rcParams['font.family'])
    fig = plt.figure(figsize = (40,40))
    ax = plt.axes()
    ax.imshow(img)
    ax.axis("off")
    for t in result:
        try:
            bbox = np.array(t[0])
            ax.text(bbox[0,0], bbox[0,1], t[1], size=30, color="black")
            r = patches.Rectangle(
                xy=(bbox[0,0], bbox[0,1]),
                width=(bbox[2,0] - bbox[0,0]),
                height=(bbox[2,1] - bbox[0,1]),
                ec="g",
                fill=False,
                linewidth=10.0
            )
            ax.add_patch(r)
        except:
            continue
    plt.savefig(os.join.path(save_path, "result.png"))


@hydra.main(config_path="config", config_name="main")
def main(cfg):
    img_path = cfg.img_path
    save_path = cfg.save_path
    img = Image.open(img_path)

    save_path = make_save_dir(save_path)

    reader = easyocr.Reader(["ja", "en"], gpu=torch.cuda.is_available())
    result = reader.readtext(img_path)
    save_result_img(img, result, save_path)

    print("finish")


if __name__ == "__main__":
    main()