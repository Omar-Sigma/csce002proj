# CSCE002 Project: Advanced GUI Scientific Calculator

We are two students at the Nile University.

In this project, we are creating an advanced gui calculator that employs many features of modern scientific calculators.

## Features include:-

1.  Basic operations.
2.  Other operations, such as exponentiation, factorials, permutations and combinations, etc.
3.  Scientific functions (Exponential, logarithimc, trigonometric, hyperbolic)
4.  The ability to work with the four main number systems and Degrees
5.  The functionality for user-defined variables.
6.  Being able to use previous answers and copy them to clipboard.
7.  Being able to add notes.
8.  A user-friendly interface.
9.  A "Help" section.
10. A minimal size.

One important feature that differentiaties this calculator from others is the fact that there are no upper limits
on the magnitude of the operations. It is totally dependent on the resources of the user.

Future possible additions:-
1. The ability to perform multiple heavy operations concurrently is being considered.
2. Adding differentiation and integration capabilities.
3. Adding root finding.
4. Adding a linear system of equations solver.
5. Adding a differential equations solver.

## Dependencies:-

1. A standard Python3 with pip (for installing ttkthemes and sympy).
2. ttkthemes.
3. Sympy.
4. Pyinstaller for freezing the application. (spec files are included with icons)
5. Venv (Virtual environments). To run pyinstaller in it.

## Currently available executables:-
    
1. Windows 10 executable. (Tested on Windows 7)
2. Linux executable. (Tested on Debian 10)

        Note: for linux executables, set permissions first by typing:-
            chmod +x binaryname
        e.g.:-
            chmod +x PowerCalc
            
        then, to run:-
            ./binary name
        e.g.:-
            ./PowerCalc
            
### Regarding mac executables:-
    
For a Mac executable, you can help out development by installing pyinstaller and freezeing the application on a mac.

## The two developers of the project are:-

1. Abdelrahman Ahmed AbdelkarimRagab
2. Omar Mohamed Abdelmonem Elsayed

### Abdelrahman Ahmed AbdelkarimRagab.

Role: Main Developer.

Wrote gui code and important functions. 

His work was useful as both direct parts of the code and as a blueprint.

Wrote the first working functions that have been added upon.

Helped with formatting the gui and providing good suggestions.

#### Some of the functions he added:-
I. The first versions of the evaluate function.
II. A function for clearing previous answers. 
III. A function that inserts the corresponding symbol to the input field.
IV. 4 functions that designs the 4 toggle buttons (bin, hex, dec, oct)
V. A function that closes all other toggle buttons when the user clicks on any toggle button.
VI. A toggle button switching function. Creating a seperate .py file for this file.


### Omar Mohamed Abdelmonem Elsayed

Role: Owner and maintainer of the Repo. Main Developer.

Wrote gui code and other important functions.

Added modifications on Abdelrahman's work. Added several functions. Main designer of the GUI.

Added classes for better code organization and smoother development.

#### Some of the functions he added:-
I. The input clear functions.
II. The variable and variable checking and clearing functions.
III. A function that modifies user-friendly input to executable input and writes the number in hex, binary and oct forms, and provides support for degrees, radians, and permutations/combinations capabilities.
IV. A function that shows the result in decimal format.
V. functions to navigate the user to and from the help and about sections in addition to scrollbars.
VI. Adding various imports to the code. Creating the help text file. Editing some of abdelrahman???s functions.
How to use the software

# Regards.

Abdelrahman Ahmed AbdelkarimRagab.

Omar Mohamed Abdelmonem Elsayed.
