# makeitrain

**EPIC**
```
As a user
So I can make it rain
I want to predict the movement of the FTSE 100 Index
```
**USER STORIES**
 ```
 As a user
 So I can know to buy or short
 I want to receive an output of up or down
 ```

 ```
 As a user
 So I have confidence in the prediction
 I want to see the percentage accuracy displayed
 ```

 ```
 As a user
 So I can minimize my investment risk
 I want the prediction to have a minimum accuracy of 75%
 ```

### How to use
```
download miniconda
https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh

- install miniconda
bash Miniconda3-latest-MacOSX-x86_64.sh

- if you are using ZSH add miniconda path to ~/.zprofile
export PATH="$HOME/miniconda3/bin:$PATH"
- and then source the file the enable the changes
source ~/.zprofile

- create a new conda environment
conda env create makeitrain

- activate the newely created environment
source activate makeitrain

- install the needed dependecies
pip install -r requirements.txt
```
