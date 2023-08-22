from flask import Flask

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def index():
    return "Go to /portfolio or /linktree, not here!"


@app.route('/portfolio')
def portfolio():
    page = f"""<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>My Portfolio</title>
  <link href="/static/css/portfolio.css" rel="stylesheet" type="text/css" />
</head>

<body>

  <h1>David's Portfolio</h1>
  <h2>Day 56 Solution</h2>
  <p>So, day 56 was all about using csv reading and file and folder manipulation to make 100 files in dozens of folders. This was tricky because the names of the folders and files were based on the top 100 streaming songs and so weren't simple to encode.</p>
<a href="https://replit.com/@DavidAtReplit/Day-056-Solution#main.py"><img src="static/images/56.png" width="500px"></a>
  
  <script src="script.js"></script>

 <!--
  This script places a badge on your repl's full-browser view back to your repl's cover
  page. Try various colors for the theme: dark, light, red, orange, yellow, lime, green,
  teal, blue, blurple, magenta, pink!
  -->
  <script src="https://replit.com/public/js/replit-badge.js" theme="blue" defer></script> 
</body>

</html>
"""
    return page
  
@app.route('/linktree')
def linktree():
    page = f"""<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>replit</title>
  <link href="static/css/linktree.css" rel="stylesheet" type="text/css" />
</head>

<body>
  <img src="static/images/davidmorgan.jpg" width="50px">
<h1>David Morgan</h1>
  <p class="about">The baldest nerd you've ever met!</p>
  <h3>Socials</h3>
  <ul>
    <li><a href="">Twitter (@LessonHacker)</a></li>
    <li><a href="">YouTube (LessonHacker)</a></li>
    <li><a href="">replit (@DavidAtReplit)</a></li>
  </ul>



  
  <script src="script.js"></script>

 <!--
  This script places a badge on your repl's full-browser view back to your repl's cover
  page. Try various colors for the theme: dark, light, red, orange, yellow, lime, green,
  teal, blue, blurple, magenta, pink!
  -->
  <script src="https://replit.com/public/js/replit-badge.js" theme="blue" defer></script> 
</body>

</html>
"""
    return page

app.run(host='0.0.0.0', port=81)
