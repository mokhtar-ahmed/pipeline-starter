import unittest
from src.main.pipeline import *


def add(num, factor):
    return num + factor


def subtract(num, factor):
    return num - factor


def multiply_by(num, factor):
    return num * factor


def divide_by(num, factor):
    return num / factor


class PipelineTestCase(unittest.TestCase):

    def test_pipeline_run_valid(self):
        pipeline = Pipeline([multiply_by, subtract, divide_by, add])
        value = pipeline.run(5, 10)
        self.assertEqual(value, 14)

    def test_pipeline_run_invalid(self):
        pipeline = Pipeline([multiply_by, subtract, divide_by, add])
        value = pipeline.run(5, 10)
        self.assertNotEqual(value, 16)


if __name__ == '__main__':
    unittest.main()
