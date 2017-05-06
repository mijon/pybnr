class testClass():

    def setup_method(self):
        print('setting up method')

    def teardown_method(self):
        print('tearing down')


    def test_this(self):
        assert 2**2 == 4

    def test_this_too(self):
        assert 3**2 == 9
