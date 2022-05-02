# Welcome to Predictd

Hello! Thank you for visiting the Predictd project.
I developed this project as part of my undergraduate final year project at Queen Mary University of London.

Predictd is a web tool that allows you to use machine learning to predict a user's MBTI type, based on their LinkedIn profile. It allows functionality to manage the data that would be appropriate in the context of the workplace.


# Installation Instructions
	Prerequisites:
	You must have Python 3.9 installed.
	You must have a LinkedIn and Gmail account.
	You must have a valid Chromedriver install under 'apps/home/chromedriver' (the provided version is for Mac only)
		(Get Chromedriver at §https://chromedriver.chromium.org/downloads)
	You must be using Google Chrome.
	Your Chromedriver and Google Chrome versions should be compatible with each other.

 1. Clone this [project](https://github.com/andricozach/Predictd.git) using your favourite IDE (PyCharm recommend) using VCS
 2. Install all of the libraries listed under **requirements.txt** [Go to file](https://github.com/andricozach/Predictd/find/master)
 3. Configure a Python 3.9 environment (Add Configuration -> Add New -> Django Server - Apply -> Ok)
 4. Run the project by pressing the green play icon
 5. The project is now running! You can access it at: http://127.0.0.1:8000/
 6. Next, navigate to 'Classifier/mbti-personality-types-classification-73-accuracy.ipynb' and Run All cells (this takes approximately 7 minutes to load)
 7. While you wait, navigate to 'core/settings.py' and find lines 130-141.
 8. Where fields are = 'REDACTED', set the appropriate EMAIL  and LINKEDIN variables with your own account login details. Notice: Gmail must be used for nonLINKEDIN variables).
 9. [Follow this guide to enable less secure apps in Gmail](https://support.google.com/accounts/answer/6010255?hl=en#zippy=%2Cif-less-secure-app-access-is-on-for-your-account)
 10. Save changes
 11. Predictd is now fully configured and working!

Note: Installations across different machine configurations may vary slightly and be fiddly for no apparent reason. Please use your discretion when following the installation instructions.

# References and Acknowledgements

A Bootstrap template was used to create this project. However, it was heavily modified to meet the requirements of this project. The original template can be found below.
https://www.creative-tim.com/learning-lab/bootstrap/overview/soft-ui-dashboard

Please see the licence disclaimer for the 'Soft UI Dashboard Bootstrap' template from Creative Tim.

MIT License

Copyright (c) 2022  [Creative Tim](https://creative-tim.com/)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



The code contained in the 'Classifier' directory was modified for the purpose of building a classification API for this project. However, it should be fully credited that this code belongs to the author (Khalid Z, 2022) and can be found at: https://www.kaggle.com/code/zeyadkhalid/mbti-personality-types-classification-73-accuracy

All the files contained in the 'Classifier' directly relating to the classifier are used directly or modified belong to their respective authors as listed below:

MBTI Personality Types Classification 73% Accuracy - ZEYAD KHALID
https://www.kaggle.com/code/zeyadkhalid/mbti-personality-types-classification-73-accuracy

MBTI Personality Types 500 Dataset - ZEYAD KHALID
https://www.kaggle.com/datasets/zeyadkhalid/mbti-personality-types-500-dataset

MBTI Pretrained Models - ZEYAD KHALID
https://www.kaggle.com/datasets/zeyadkhalid/mbti-pretrained-models

(MBTI) Myers-Briggs Personality Type Dataset - MITCHELL J
https://www.kaggle.com/datasets/datasnaek/mbti-type
