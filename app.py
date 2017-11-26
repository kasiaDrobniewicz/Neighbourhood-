from unit_controller import UnitController


class Application():

    def __init__(self):
        self.unit_controller = UnitController()

    def main(self):
        self.unit_controller.start()


if __name__ == '__main__':
    application = Application()
    application.main()
