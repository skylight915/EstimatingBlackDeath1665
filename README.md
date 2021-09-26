# EstimatingBlackDeath1665
A code deveveloped to estimate the total death of the Black Death outbreak in 1664 and allow user inputs 

## Sources used
- Two text files containing historical figures of rat populations and population density in the studied area provided by Dr. Turner. 
- Initial coefficients indicating the relationship between the total deaths on the one hand, and rat population and population density on the other. 
- Equation provided by Dr. Turner: Death per parish = (0.8 x 'rat population') x (1.3 x population density in parish)

## Development ideas
- **Display all the three maps within a same figure:** while I have written the code for it (included also in the submitted notebook) by importing the cv2 library and using fig() and add_subplot() functions, the displayed figure is not ideal, because each map is surrounded by a frame with coordinates...
- **Create a GUI and sliders:** they allow users to choose values for coefficients set within a range and the map of death_average will change accordingly.


## Development history
The intention is to document changes from one version to another here.
### Origin
This code began its development during the course **[Programming for Geographical Information Analysis: Core Skills](https://www.geog.leeds.ac.uk/courses/computing/study/core-python/)**. It includes the following development steps specifically:
1. Read in two text files and make them into two 2-D lists, which allows later to display two raster maps of average rats caught and population density per 100m x 100m square;
2. Import NP library and intersect the two previous lists to create a new array containing information on average deaths per 100m x 100m square;
3. Sum the values of the newly-created array (death_average) and print out the result of total deaths;
4. Save the array of average deaths as a text file by making it a matrix first, in which each line equivalent with a line on the map;
5. Import Matplot library, display all the three 2-D lists on screen, add titles and save them into separate png documents;
6. Create command lines for user inputs on the two coefficients by using the function input();
7. Calculate the total deaths based upon user inputs and print out the result. 


## Outputs:
- Three maps as png documents.
- The result of the total deaths of the Black Death Outbreak in 1665 based upon defaulted coefficient.
- The result of the total deaths of the Black Death Outbreak in 1665 based upon user inputs. 


## Contributions
Welcome

## LICENSE
- [APACHE LICENSE, VERSION 2.0](https://www.apache.org/licenses/LICENSE-2.0)

## Acknowledgement
Thanks Dr. Andy Turner for prompt support during the writing of this code.
