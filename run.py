import torch
import hydra
#from easyocr import easyocr
import easyocr


@hydra.main(config_path="config", config_name="main")
def main(cfg):
    img_path = cfg.img_path

    reader = easyocr.Reader(["ja", "en"], gpu=False)

    result = reader.readtext(img_path)
    print("finish")

if __name__ == "__main__":
    main()