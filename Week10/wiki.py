import wikipedia

var = input("Search Keyword: ")
print(wikipedia.search("Monty"))

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)