from __future__ import unicode_literals

from .helpers import SeleniumTestCase


class NamespaceInterpretationTest(SeleniumTestCase):

    def test_namespaces_after_pjaxr(self):
        self.browser_get_reverse('index')
        self.assertTitle('index-title')
        self.assertContent('index-content')
        self.assertBodyNamespace('md.index')

        about_link = self.browser.find_element_by_css_selector('#about-link')
        about_link.click()

        self.wait.until(lambda browser: browser.title == 'about-title')
        self.assertTitle('about-title')
        self.assertContent('about-content')
        self.assertCurrentNamespace('md.about')

        project_link = self.browser.find_element_by_css_selector('#project-link')
        project_link.click()

        self.wait.until(lambda browser: browser.title == 'project-title')
        self.assertTitle('project-title')
        self.assertContent('project-content')
        self.assertCurrentNamespace('md.project.index')  # multiline namespace - prove for #24
