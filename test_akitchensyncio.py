"""Unit tests for akitchensyncio."""

import unittest
import asyncio
import operator
from akitchensyncio import wrap_future, transform_future, iawait

async def return_later(x):
    await asyncio.sleep(0.01)
    return x

@wrap_future
async def return_later2(x):
    await asyncio.sleep(0.01)
    return x

class TestAll(unittest.TestCase):

    def test_iawait(self):
        self.assertEqual(iawait(return_later(42)), 42)

    def test_wrap_future(self):
        p = return_later2(object())
        self.assertTrue(asyncio.isfuture(p))
        self.assertTrue(iawait(p) is iawait(p))

    def test_transform_future(self):
        p = transform_future(operator.itemgetter(1), return_later("abc"))
        self.assertTrue(asyncio.isfuture(p))
        self.assertEqual(iawait(p), "b")

if __name__ == '__main__':
    unittest.main()
