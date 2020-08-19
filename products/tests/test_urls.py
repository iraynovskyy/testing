from django.urls import reverse, resolve


# here should be all tests for urls...
class TestUrls:

    def test_detail_url(self):
        path = reverse('detail', kwargs={'pk': 1}) # we need to path one value for a parameter in path as it has pk in it.
        assert resolve(path).view_name == 'detail'