# Q - Create a framework base counter that counts test execution instances:
import unittest


class TestExecutionCounter():
    count = 0

    def __init__(self):
        TestExecutionCounter.count += 1

test1=TestExecutionCounter()
test2=TestExecutionCounter()
test3=TestExecutionCounter()
print(TestExecutionCounter.count)