import unittest
from sorted_set import SortedSet

class TestConstruction(unittest.TestCase):

    def test_empty(self):
        s = SortedSet([])

    def test_from_sequence(self):
        s = SortedSet([7,8,9,10])

    def test_with_duplicates(self):
        s = SortedSet([8,8,8,9])

    def test_from_iterable(self):
        def gen2468():
            yield 2
            yield 4
            yield 6
            yield 8

        g = gen2468()
        s = SortedSet(g)

    def test_default_empty(self):
        s = SortedSet()


class TestContainerProtocol(unittest.TestCase):

    def setUp(self):
        self.s = SortedSet([6,7,3,9])

    def test_positive_contained(self):
        self.assertTrue(6 in self.s)

    def test_negative_contained(self):
        self.assertFalse(5 in self.s)

    def test_positive_not_contained(self):
        self.assertTrue(5 not in self.s)

    def test_negative_not_contained(self):
        self.assertFalse(6 not in self.s)


class TestSizedProtocol(unittest.TestCase):

    def test_empty(self):
        s = SortedSet()
        self.assertEqual(len(s), 0)

    def test_one(self):
        s = SortedSet([42,])
        self.assertEqual(len(s), 1)

    def test_n(self):
        s = SortedSet([1,2,3,4,5,6,7,8,9,10])
        self.assertEqual(len(s), 10)

    def test_w_duplicates(self):
        s = SortedSet([42,42,42])
        self.assertEqual(len(s), 1)


class TestIteratorProtocol(unittest.TestCase):

    def setUp(self):
        self.s = SortedSet([1,2,3,4,4])
    
    def test_iter(self):
        i = iter(self.s)
        self.assertEqual(next(i), 1)
        self.assertEqual(next(i), 2)
        self.assertEqual(next(i), 3)
        self.assertEqual(next(i), 4)
        self.assertRaises(StopIteration, lambda: next(i))

    def test_for_loop(self):
        i = 0
        expected = [1,2,3,4]
        for item in self.s:
            self.assertEqual(item, expected[i])
            i += 1


class TestSequenceProtocol(unittest.TestCase):

    def setUp(self):
        self.s = SortedSet([4, 1, 2, 3, 1])

    def test_index_zero(self):
        self.assertEqual(self.s[0], 1)

    def test_index_three(self):
        self.assertEqual(self.s[3], 4)

    def test_index_out_of_bounds(self):
        with self.assertRaises(IndexError):
            self.s[4]

    def test_index_minus_one(self):
        self.assertEqual(self.s[-1], 4)

    def test_index_minus_four(self):
        self.assertEqual(self.s[-4], 1)

    def test_index_minus_out_of_bounds(self):
        with self.assertRaises(IndexError):
            self.s[-5]

    def test_slice_from_start(self):
        self.assertEqual(self.s[:3], SortedSet([1,2,3]))

    def test_slice_to_end(self):
        self.assertEqual(self.s[2:], SortedSet([3,4]))

    def test_slice_middle(self):
        self.assertEqual(self.s[1:3], SortedSet([2,3]))

    def test_slice_empty(self):
        self.assertEqual(self.s[10:], SortedSet([]))

    def test_full_slice(self):
        self.assertEqual(self.s[:], self.s)

    def test_reversed(self):
        s = SortedSet([1,2,1,3,4])
        r = reversed(s)
        self.assertEqual(next(r), 4)
        self.assertEqual(next(r), 3)
        self.assertEqual(next(r), 2)
        self.assertEqual(next(r), 1)
        with self.assertRaises(StopIteration):
            next(r)

    def test_index_positive(self):
        s = SortedSet([1,2,1,3,4])
        self.assertEqual(s.index(2), 1)

    def test_index_negative(self):
        s = SortedSet([1,2,1,3,4])
        with self.assertRaises(ValueError):
            s.index(5)

    def test_count_zero(self):
        s = SortedSet([1,2,1,3,4])
        self.assertEqual(s.count(5), 0)

    def test_count_one(self):
        s = SortedSet([1,2,1,3,4])
        self.assertEqual(s.count(1), 1)


class TestReprProtocol(unittest.TestCase):

    def test_repr_empty(self):
        s = SortedSet()
        self.assertEqual(repr(s), "SortedSet([])")

    def test_repr_values(self):
        s = SortedSet([4, 1, 2, 1, 3])
        self.assertEqual(repr(s), "SortedSet([1, 2, 3, 4])")

    
class TestEqualityProtocol(unittest.TestCase):

    def test_positive_equal(self):
        self.assertTrue(SortedSet([1,2,3]) == SortedSet([1,2,3]))

    def test_negative_equal(self):
        self.assertFalse(SortedSet([1,2,3]) == SortedSet([4,5,6]))

    def test_type_mismatch(self):
        self.assertFalse(SortedSet([1,2,3]) == [4,5,6])

    def test_identical(self):
        s = SortedSet([1,2,3])
        self.assertTrue(s == s)


class TestInequalityProtocol(unittest.TestCase):

    def test_positive_unequal(self):
        self.assertTrue(SortedSet([1,2,3]) != SortedSet([4,5,6]))

    def test_negative_unequal(self):
        self.assertFalse(SortedSet([1,2,3]) != SortedSet([3,2,1]))

    def test_type_mismatch(self):
        self.assertTrue(SortedSet([1,2,3]) != [1,2,3])

    def test_identical(self):
        s = SortedSet([2,3,4])
        self.assertTrue(s == s)


class TestConcatenateProtocol(unittest.TestCase):
    
    def test_concatenate_different(self):
        s = SortedSet([1,2,3])
        t = SortedSet([4,5,6])
        self.assertEqual(s + t, SortedSet([1,2,3,4,5,6]))

    def test_concatenate_same(self):
        s = SortedSet([1,2,3])
        t = SortedSet([1,2,3])
        self.assertEqual(s + t, SortedSet([1,2,3]))

    def test_concatenate_overlap(self):
        s = SortedSet([1,2,3])
        t = SortedSet([2,3,4])
        self.assertEqual(s + t, SortedSet([1,2,3,4]))


class TestMultiplicationProtocol(unittest.TestCase):

    def setUp(self):
        self.s = SortedSet([1,2,3])

    def test_multiply_by_zero_right(self):
        self.assertEqual(0 * self.s, SortedSet())

    def test_multiply_by_nonzero_right(self):
        self.assertEqual(100 * self.s, self.s)

    def test_multiply_by_zero_left(self):
        self.assertEqual(self.s * 0, SortedSet())

    def test_multiply_by_nonzero_left(self):
        self.assertEqual(self.s * 100, self.s)




if __name__ == "__main__":
    unittest.main()