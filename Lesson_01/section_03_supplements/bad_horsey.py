

class Horse:

    def __init__(self):
        self.legs = 4
        self.head = 'horse head'
        self.assign_body()

    def assign_body(self):
        self.body = 'horse body'

    def make_noise(self):
        print("NeeEEeeeIIiigh!!")

    def gallop(self):
        print("Galloping!")


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
    print(F"{bojack.head=}")
    print(F"{bojack.body=}")
    print(F"{bojack.legs=}")
    bojack.make_noise()
    bojack.gallop()

    print("\nHollyhock the shetland pony")
    hollyhock = ShetlandPony()
    print(F"{hollyhock.head=}")
    print(F"{hollyhock.body=}")  # ! raises exception here
    print(F"{hollyhock.legs=}")
    hollyhock.make_noise()
    hollyhock.gallop()
