from guizero import App, PushButton

def pushed():
    button.bg="red"

app=App(title="My very first Python app.")
#button=PushButton(app,title="Push me",command=pushed)
button = PushButton(app)
button.title = "hello"

app.update()


app.display()
