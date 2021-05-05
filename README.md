# Gramoday

Task :
Write a python script to fetch data of prices for the year 2020 (date wise from 1st Jan’2020 to 31st Dec’2020) for district “Agra” of Uttar Pradesh from the data sources.

1. Link Generator : https://colab.research.google.com/drive/1zInU1kkKUUseQLAuQcmnYZ1p1OyAqE7F?authuser=2#scrollTo=hf2QgeerW4Av
This is an interactive way to type the values from selected mapping of Key and their Values for various paramters,
For demonstration purposes , we have suppied the example for one particular task combim=nation only but it can be leveraged to any combination with minimal to no intervention.
![image](https://user-images.githubusercontent.com/24694205/117212991-ab38b300-ae18-11eb-8759-75f8276c7a56.png)
While supplying date values, we need to ensure that we are using the exact same format as provided in image else the link will not be functional.
![image](https://user-images.githubusercontent.com/24694205/117213321-16828500-ae19-11eb-92d1-1cd37ecbeedf.png)
Use the highlighted button to copy the generated link which is basically the combination of all are supplied options for the parameters.

2. Second part is to paste the link from 1. to our next selenium script that will download the excel file. 
![image](https://user-images.githubusercontent.com/24694205/117213689-94469080-ae19-11eb-9855-09fdd2a56fc8.png)
Paste the link in the download function.
To run this we need to ensure that we have firefox installed with its corresponding webdriver
```driver=webdriver.Firefox(executable_path='G:/geckodriver-v0.24.0-win64/geckodriver.exe')```	
Update the executable path accordingly.

3. Upload the Excel sheet to Google Drive.
4. Visualization and Analysis for Prediction : https://colab.research.google.com/drive/1nqWiWUMi_n-IPii2eJnt4JzcOrepEVVq?authuser=2#scrollTo=u1z_ftaFRhMu
   Mount your drive and provide the path ![image](https://user-images.githubusercontent.com/24694205/117214415-69107100-ae1a-11eb-9c4e-bcea97626c3b.png)
