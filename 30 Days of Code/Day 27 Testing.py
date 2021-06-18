def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx

class TestDataEmptyArray():
    def get_array():
        #returns an empty array
        return ''
        
class TestDataUniqueValues():
    
    def get_array():
        #returns an array of size at least 2 with all unique elements
        #pass
        test_array = [1,2]
        return test_array 
    
    def get_expected_result():
        #returns the expected minimum value index for this array
        #pass
        return 0
    
class TestDataExactlyTwoDifferentMinimums:
    
    def get_array():
        #returns an array where the minimum value occurs at exactly 2 indices
        #pass
        test_array = [1,2,3,1]
        return test_array

    def get_expected_result():
        #returns the expected index
        #pass 
        return 0




def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False


def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")

