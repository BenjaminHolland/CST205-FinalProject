# Tracked Red Ball Music (Tentative Title)

## Team
### Jacob Erickson
* Email: jerickson@csumb.edu
* Github: https://github.com/Jacob-Erickson
* Slack: @jerickson

### Benjamin Holland
* Email: bholland@csumb.edu
* Github: https://github.com/BenjaminHolland
* Slack: @ben.holland

### Joseph Martineau
* Email: jmartineau@csumb.edu
* Github: https://github.com/jmartineau
* Slack: @jmartineau

## Class: CST205 - Multimedia Programming

## December 11, 2017

## Description
This application tracks an object's movement and produces sound based on that object's position.
The need is to develop a new, innovative way to create music. The solution is a website that allows
users to upload video clips where the sound is re-encoded based on an object's location.

## How to Run the Program
The project uses pipenv to manage dependancies, so you will need to install it.
Download the project from GitHub and put it into a directory of your choice.
From there, navigate to that directory with your terminal and follow the instructions below.

Pipenv Install/Usage instructions:
1. from a fresh command line, run "pip install --user pipenv"
2. add the user python script folder to the path. This should be  .../AppData/Roaming/Python36/Scripts, or {python install location}/Scripts if you didn't use the --user argument.
3. restart the shell and navigate to the project folder
4. run "pipenv install". This will install the dependencies for the project.
5. run "pipenv shell". This activates the virtual environment.
NOTE: There is currently a bug that causes this to launch a command prompt instead of powershell. To fix this, once you run step 5, also run "powershell ."
6. run ./launch.ps1. This will launch flask.

Link to GitHub Repo: https://github.com/BenjaminHolland/CST205-FinalProject

## Future Work
For future additions, the user could specify what kind of object they want tracked. At the moment, only red ball tracking
is supported, but it would be nice to have a dropdown menu where the user can choose both the color and object to track.
Additionally, settings to tweak the sound that is produced from tracking that object could be implemented.

