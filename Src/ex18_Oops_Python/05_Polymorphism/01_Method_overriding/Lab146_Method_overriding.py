class BaseTest:
    def run(self):
        print('BaseTest')
class LoginTest(BaseTest):
    def run(self):
        print('LoginTest run')

t=LoginTest()
t.run()

