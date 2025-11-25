class APIBase:

    def api_auth(self):
        print("authntcating API")

class DBBase:
    
    def db_connection(self):
        print("db connection")

class TestHybrid(APIBase, DBBase):

    def run(self):
        self.api_auth()
        self.db_connection()
        print("Test Case RUN")

tc1=TestHybrid()
tc1.run()