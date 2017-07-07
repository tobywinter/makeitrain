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
- Download miniconda
  https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh

- Install miniconda
  bash Miniconda3-latest-MacOSX-x86_64.sh

- If you are using ZSH add miniconda path to ~/.zprofile
  export PATH="$HOME/miniconda3/bin:$PATH"
- And then source the file the enable the changes
  source ~/.zprofile

- Create a new conda environment
  conda env create makeitrain

- Activate the newely created environment
  source activate makeitrain

- Install the needed dependecies
  pip install -r requirements.txt
```
