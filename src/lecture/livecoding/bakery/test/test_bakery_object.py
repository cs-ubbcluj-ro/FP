from unittest import TestCase

from lecture.livecoding.bakery.domain.bakery_object import BakeryObject


class TestBakeryObject(TestCase):
    """
    Observations about writing PyUnit tests:
        -> PyUnit is a member of the xUnit testing tools (the first was probably JUnit for Java)
        -> Unit tests should be placed in their own directory/package (usually called "test")
        -> Unit test classes must be derived from unittest.TestCase (gives us access to assertXXX methods)
        -> test method names must start with "test_"
        -> test methods are run separately from running the program

        Test discovery:
            -> the testing framework must be able to autoamtically find and run all unit tests
            -> right-click on test package -> Run all tests ...

        How do I know I've written enough tests? !?
        => we use "code coverage" (how much of the application's source code, expressed in percents, was executed
        while running the tests)
            - the idea is not to miss classes, functions, code sections
        => more code coverage is generally better than less, but not perfect :(
        => 100% code coverage does not mean the application does not have bugs :(
    """

    def test_bakery_object_1(self):
        obj = BakeryObject(100, "White bread 1kg")
        self.assertEqual(100, obj.id)
        self.assertEqual(obj.name, "White bread 1kg")

    def test_bakery_object_2(self):
        obj = BakeryObject(101, "Bagels 500g")
        self.assertEqual(101, obj.id)
        self.assertEqual(obj.name, "White bread 1kg")
