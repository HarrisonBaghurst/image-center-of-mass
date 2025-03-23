# Image center of mass 
This program is designed to find the center of mass of a black and white png image assuming it is cut from a sheet of equal thickness material. This is output visually through a returned image with a line indicating its cetner of mass. This also gives the option of including a backplate in the calculation. If you do include a backplate it assumes that backplate is present behind all of the black lines. It is also assumed that the backplate is half of the thickness of the front plate. 

# How to use 
- Download 'main.exe'
- In the same directory as the .exe file, create two folders named 'inputs' and 'outputs' 
- In the inputs folder, place your .png images
- Run 'main.exe' and either input 'y' or 'n' to include or exclude a backplate in the calculation 
- Once the menu closes, look in the outputs folder to find the line indicating the center of mass 

# Image format 
The image needs to be in the correct format: 
- A .png file of any width and height 
- Include an alpha value for each pixel 
- In black and white if no backplate is included in the calcuation 
- In black, white and green if a backplate is included 
Note: Black, white and green works for the no backplate calculation but black and white will not work for the backplate calculation 
