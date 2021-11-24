## <center>Cats and Dogs</center>
### <center>A Simple Convnet for Image Identification</center>

<center><img src= "https://github.com/ripitup-github/cats-and-dogs/blob/master/demo.png"></center>


## Overview
- Train examples : `20000`
- Validation examples: `2500`
- Validation accuracy: `96.1%`
- Test examples: `2500`
- Test accuracy: `97.3%`

## Requirements
- Anaconda
- NVDIA GPU (**Recommed**)

## How to install (only for Windows)
- Make sure you use **Administrator** powershell, then:
- `git clone https://github.com/ripitup-github/cats-and-dogs.git`
- `cd ./cats_and_dogs`
- `conda env -create -f environment.yml`

## After Installation, You Might Want To

### NOTE: before you run any commend, make sure your conda environment is activated, like this:

### `(deep_learning) PS C:\Users\Attendre>`

### Train convnet
- Do `python cats_and_dogs.py`

### Run predict
- Put images into `test` folder
- Do `python predict.py`
- After it, you can find there is a extra folder `predicted`
- In `predicted`  folder, **cats** and **dogs** images are categorical separate in two subfolders `cats` and `dogs`
