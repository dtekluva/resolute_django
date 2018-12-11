
def csrf(function, csrf):

    def wrapper():
        print('works')
        function()
    def err():
        print('Not allowed')

    if csrf ==True:
        return wrapper
    else:
        return err

def view(news):
    print("your view was processed", news)

view = csrf(view, True)

view()