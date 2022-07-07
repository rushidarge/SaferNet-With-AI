# SaferNet-With-AI

Nowadays on social networks where everyone can upload whatever they want without having to count that there might be children watching that or people don't want to watch that. To avoid this we need to come up with a solution that filters based real-time and with high accuracy using chrome extension that filters real-time NSFW (not safe for working) images and replaces them with SFW (safe for working) images.

The government has definitely taken a step in this direction by blocking some websites, but what about social media sites and other sites? They are openly showing NSFW (not safe for work) content on their sites. We can avoid that content using artificial intelligence.

We can use some advanced computer vision techniques to filter out that content. We cannot access social media servers and block content for everyone, but we can add filters on the user side. To add a filter between a website and a user, we can simply use a browser extension, so we can filter content with very low latency, and it is also easy to deploy by using JavaScript.

## Flowchart of Chrome Extension
![Flowchart](https://github.com/rushidarge/SaferNet-With-AI/blob/main/images/U41ntitled%20presentation.jpg)


## To install extension

1. Download the  `Safenet with AI.zip` file to your computer.

2. Extract file

3. Go to `chrome://extensions/` and check the box for Developer mode in the top right.

3. Click on `Load Unpack`.

4. select the unzipped folder to load your extension.

5. You will see smiley in extensions. 

Note : This version support 0.90 or lower version of chrome

## Demo (Working) Before after
### Before
![before](https://github.com/rushidarge/Safenet-with-AI/blob/main/images/before.JPG)

![before](https://github.com/rushidarge/Safenet-with-AI/blob/main/images/before1.JPG)

![img](https://github.com/rushidarge/SaferNet-With-AI/blob/main/images/imageedit_1_3822010435.jpg)

## Install SaferNet with AI Extension
![img](https://github.com/rushidarge/SaferNet-With-AI/blob/main/images/1_WoUNUcCUoXXnlaff5_da8g.png)


### After
![after](https://github.com/rushidarge/Safenet-with-AI/blob/main/images/after.JPG)

![after](https://github.com/rushidarge/Safenet-with-AI/blob/main/images/after2.JPG)


![img](https://github.com/rushidarge/SaferNet-With-AI/blob/main/images/extension%20demo2.JPG)

# Method of implementation
### Data
NSFW (Not safe for working) images I use from [Nudenets](https://github.com/notAI-tech/NudeNet) and for SFW I use images from [unsplash](https://unsplash.com/)

### Model
If we use normal CNN model then the model size will be huge. Even if we train model with 3-5 layers model size gone upto 1 GB.
We want to make it lightweight to work smoothly we use [MobileNet version 3](https://arxiv.org/abs/1704.04861).

## Future Work
- change image source using threading
- Add url change detection
- Try to batch predict
