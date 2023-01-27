from simplepycli import PyCLIApp

app = PyCLIApp()

@app.command("egg", "Prints egg to the console")
def egg(params):
  print("egg")

@app.command("echotwice", "Echos the string passed in as a paramater twice")
def echotwice(params):
  for i in range(2):
    print(params)

app.run()