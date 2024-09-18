

class Horse:

    def __init__(self):
        self.legs = 4
        self.head = 'horse head'
        self.__assign_body()

    def __assign_body(self):
        self.body = 'horse body'

    def assign_body(self):
        self.__assign_body()

    def make_noise(self):
        print("NeeEEeeeIIiigh!!")

    def gallop(self):
        print("Galloping!")


class Eagle:

    def __init__(self):
        self.wings = 2
        self.head = 'eagle head'
        self.body = 'eagle body'

    def make_noise(self):
        print("ScreeeEEEeee!!")

    def fly(self):
        print("Flying!")


class Hippogriff(Horse, Eagle):

    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)
        Horse.assign_body(self)


class ShetlandPony(Horse):

    def __init__(self):
        super().__init__()
        self.size = 'smol'

    def assign_body(self):
        return """<body>
          <p>
            Did you know, horses are not made of HTML?
          </p>
        </body>"""


print("\nBoJack the horse")
bojack = Horse()
print(F"{bojack.body=}")
print(F"{bojack.head=}")
print(F"{bojack.legs=}")
bojack.make_noise()
bojack.gallop()

print("\nEddie the eagle")
eddie = Eagle()
print(F"{eddie.body=}")
print(F"{eddie.head=}")
print(F"{eddie.wings=}")
eddie.make_noise()
eddie.fly()


print("\nBuckbeak the Hippogriff")
buckbeak = Hippogriff()
print(F"{buckbeak.body=}")
print(F"{buckbeak.head=}")
print(F"{buckbeak.legs=}")
print(F"{buckbeak.wings=}")
buckbeak.make_noise()
buckbeak.fly()
buckbeak.gallop()

print("\nHollyhock the shetland pony")
hollyhock = ShetlandPony()
print(F"{hollyhock.body=}")
print(F"{hollyhock.head=}")
print(F"{hollyhock.legs=}")
hollyhock.make_noise()
hollyhock.gallop()
