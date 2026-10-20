from pyscript import document

club_members = [
    "Carding Batungbakal", 
    "Bogart Sarmiento", 
    "Tina Moran", 
    "Samantha Mercado",
    "Princess Mae Flores",
    "Alyssa Castillo",
    "Sebastian Flores",
    "Patricia Aquino",
    "Lorenzo Navarro",
    "Danielle Mercado",
    "Elijah Torres",
    "Beatrice Lim",
    "Matthew Gonzales",
    "Nicole Valdez",
    "Adrian Manalo",
    "Gabrielle Tan",
    "Rojiniah Tungul",
    "Luisito Balajadia"
    ]

def check_member(e):
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()

    full_name = first_name + " " + last_name

    result = document.getElementById("result")
    message = document.getElementById("message")

    result.style.display = "block"

    if full_name in club_members:
        message.innerHTML = f"Congratulations {full_name}! You are now part of the Social Science club."
    else:
        message.innerHTML = f"Sorry {full_name}, your name is not on the list."

