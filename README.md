# makeitrain

This is an application using machine learning to predict the future movement of the FTSE100 index. Each day, it will generate it's prediction for the FTSE100 for the next day and the accuracy of its prediction.

![Front-page](http://imgur.com/bR1UsHC)

## User Stories

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

## How To Use
```
download miniconda
https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh

install miniconda
bash Miniconda3-latest-MacOSX-x86_64.sh

if you are using ZSH add miniconda path to ~/.zprofile
export PATH="$HOME/miniconda3/bin:$PATH"

conda env create -f makeitrain.yml
source activate makeitrain


to update the environment
conda env update -f makeitrain.yml
```

## Pending Improvements

## Contributors
[Charlotte](www.github.com/charlieafea)
[Daniele](www.github.com/)
[Kavita](www.github.com/)
[Toby](www.github.com/)
[Ian](www.github.com/)
[Spencer](www.github.com/)
