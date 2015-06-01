from django.test  import TestCase

from farinha.models import Snippet

class SnippetTestCase(TestCase):
    def setUp(self):
        pass

    def test_empty_snippet(self):
        s = Snippet()
        s.save()
        self.assertEqual(str(s), "")

    def test_title_snippet(self):
        s = Snippet(title="testing")
        s.save()
        self.assertEqual(str(s), "testing")

    def test_alias_snippet(self):
        s = Snippet(alias="testing")
        s.save()
        self.assertEqual(str(s.alias), "testing")

    def test_header_snippet(self):
        s = Snippet(header="testing")
        s.save()
        self.assertEqual(str(s.header), "testing")

    def test_body_snippet(self):
        s = Snippet(body="testing")
        s.save()
        self.assertEqual(str(s.body), "testing")

    def test_footer_snippet(self):
        s = Snippet(footer="testing")
        s.save()
        self.assertEqual(str(s.footer), "testing")
