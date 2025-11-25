class TestSuite:

    def info(self):
        print("grandfather")

class BaseTest(TestSuite):

    def setup(self):
        print("BaseTest")

class UITest(BaseTest):

    def run(self):
        self.info()
        self.setup()
        print("run test case")
        
test = UITest()
test.run()