from flask import Flask

app = Flask(__name__)

myReflections = {}

myReflections["78"] = {"link" : "https://replit.com/@DavidAtReplit/Day-075-Solution#index.html", "Reflection" : "Was a bit of a head scratcher, but I got there in the end. Even if I was a bit lazy with the css 😭"}

myReflections["79"] = {"link" : "https://replit.com/@DavidAtReplit/Day-075-Solution#index.html", "Reflection" : "Oh. Easy. Done. Boom"}

@app.route('/<pageNumber>')
def index(pageNumber):
  global Reflections
  page = ""
  f = open("template/reflection.html", "r")
  page = f.read()
  f.close()

  
  page = page.replace("{day}", pageNumber)
  page = page.replace("{date}", myReflections[pageNumber]["link"])
  page = page.replace("{reflection}", myReflections[pageNumber]["Reflection"])
  return page


app.run(host='0.0.0.0', port=81)
