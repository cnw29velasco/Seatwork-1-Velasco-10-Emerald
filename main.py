

from pyscript import document, display

names = ['Logan Anaque', 'Gavin Ruiz', 'Jacob Minguillo', 'Jhoanna Evnagelista']

def check_name(e):

    
    names = ['Logan Anaque', 'Gavin Ruiz', 'Jacob Minguillo', 'Jhoanna Evnagelista']

    document.getElementById("output1").innerHTML=" "

    first = document.getElementById('first').value
    last = document.getElementById('last').value

    full = first + " " + last
    realname = full in names

    message = {

        True: "Your name is part of ICT club!",
        False: "Your name is not on the list of members"


    }

    display(message[realname], target="output1")