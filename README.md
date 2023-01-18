# EasyOCR_sample

## Installation
1. Launch Colab Server to run EasyOCR.

2. Copy-paste to the terminal the command below to connect Colab Server

```
ssh root@*.tcp.ngrok.io -p *****
```

3. Use the following command to generate a new key pair, and check a new SSH key.
```
ssh-keygen
cat ~/.ssh/id_rsa.pub
```

4. [Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

5. Clone this repository, and change directory.
```
git clone git@github.com:keihsgw0605kgsm/easyocr_sample.git
cd easyocr_sample
```

6. Install python libraries

```
make build
```

## Run
1. Set target image in `config/main.yaml`
2. Run EasyOCR
```
python run
```