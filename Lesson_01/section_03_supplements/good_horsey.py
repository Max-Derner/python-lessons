

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


if __name__ == "__main__":
    print("\nBoJack the horse")
    bojack = Horse()
    print(f"{bojack.body=}")
    print(f"{bojack.head=}")
    print(f"{bojack.legs=}")
    bojack.make_noise()
    bojack.gallop()

    print("\nEddie the eagle")
    eddie = Eagle()
    print(f"{eddie.body=}")
    print(f"{eddie.head=}")
    print(f"{eddie.wings=}")
    eddie.make_noise()
    eddie.fly()

    print("\nGazza the Hippogriff")
    gazza = Hippogriff()
    print(f"{gazza.body=}")
    print(f"{gazza.head=}")
    print(f"{gazza.legs=}")
    print(f"{gazza.wings=}")
    gazza.make_noise()
    gazza.fly()
    gazza.gallop()

    print("\nHollyhock the shetland pony")
    hollyhock = ShetlandPony()
    print(f"{hollyhock.body=}")
    print(f"{hollyhock.head=}")
    print(f"{hollyhock.legs=}")
    hollyhock.make_noise()
    hollyhock.gallop()
