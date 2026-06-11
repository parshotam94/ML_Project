## End to end machine learning project

Steps:

First Create folder and copy its path like *C:\Users\prsho\OneDrive\Desktop\ML Projects*

Now open *Anaconda prompt* and type *cd C:\Users\prsho\OneDrive\Desktop\ML Projects*

then type *code .*-> this will open VS Code instance

To create virtual environment: *conda create -p venv python==3.8 -y*    (-y for confirmation Yes)
To activate this: *conda activate venv/*

To sync git repository with it:
*git init*
*git add README.md*
*git commit -m "add readme"*
*git remote origin main url*
*git push origin main*

create .gitignore file on Github and select type = Python 
then *git pull origin main*

create folder *src* and inside it create *__init__.py* and also create file *setup.py* and it will create your project as package

inside requirements.txt *-e .* will be used to indicate that there is setup.py file.(it acts as mapper)

now create folder *components* and inside it create "__init__.py" This is going to store all modules that we are going to create like data ingestion, data transformation, model_trainer etc and create files also

create another folder pipeline and it will contain pipeline code

create files inside src logger.py(for logs), exception.py(for custom exception), utils.py(for other)

and to check logger.py is working well. type *python src/logger.py* this will create log file

now take dataset and do stuff

go on .gitignore file and in environments write .artifacts







