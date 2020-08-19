# She Said Pizza
It's a simple pizza ordering app

Technologies used
----------
- Python backend
- Django web framework
- Sqlite database current development
- HTML/CSS

Installation
-----------
Clone this repo to your machine.
We need to create a virtual environment in our copy of the repository, so that the technologies you download to make Instagram Miner work don't interfere with any other technologies you may have installed on your computer.
Make sure that the virtual environment is in the parent directory(ehere the requirements.txt is there)

##### step 1 : ` $ virtualenv env `
##### step 2 : Next, type ` $ source env/bin/activate ` to create a "bubble" around the workspace. <br> For Windows type ` env\Scripts\activate`

##### To deactivate type `deactivate`
##### step 3: <p><br>We now need to install all the libraries and technologies that appear in the file ` requirements.txt `. From the ` MyPizzaz/ ` directory (which you should still be in), simply type the following into your Terminal:
</p>

` (env) $ pip install -r requirements.txt `
##### step 4: Make Migrations
` > py manage.py makemigrations`
` > py manage.py migrate`
##### step 5: Create Superuser
` > py manage.py createsuperuser`
##### step 6: Run Development Server
` > py manage.py runserver`
##### step 7: Add Data In Admin Page
` add the pizzaas in your store`
##### step 8: Go To URL
` http://127.0.0.1:8000/sspizza/ `

Created By
-----------
-[SUHAS.K.SHETTY](https://github.com/DarkSchokolade)
-[HARIHARAN PARTHIBAN](https://github.com/StealthAdder)