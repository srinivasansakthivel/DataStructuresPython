class Cookie:
    def __init__(self, colour):
        self.colour = colour

    def get_colour(self):
        return self.colour

    def set_colour(self, colour):
        self.colour = colour


blue_cookie = Cookie("Blue")
green_cookie = Cookie('Green')

print("Cookie one is : " + blue_cookie.get_colour())
print("Cookie two is : " + green_cookie.get_colour())

blue_cookie.set_colour("White")

print("New colour of blue cookie is : " + blue_cookie.get_colour())
