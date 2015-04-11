from django.utils.deconstruct import deconstructible

from storages.backends import s3boto


@deconstructible  # pylint: disable=abstract-method
class PublicStorage(s3boto.S3BotoStorage):
    """
    Public storage for tools, screenshots, and user profile images.
    """
    def __init__(self, *args, **kwargs):
        kwargs['acl'] = 'public-read'
        kwargs['querystring_auth'] = False

        super(PublicStorage, self).__init__(*args, **kwargs)
