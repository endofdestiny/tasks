from selenium import webdriver
import unittest




class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()


    def test_can_start_a_task_list_and_retrieve_it_later(self):
        # Jen has heard about a cool task management app,
        # she checks out it's homepage
        self.browser.get("http://localhost:8000")


        # She notices the page title and header mention tasks
        self.assertIn('Tasks', self.browser.title)
        self.fail("Finish the test")

        # She is invited to enter a to-do item immediately


        # She types "Buy catfood" into the text box


        # When she hits enter, the page updates, and now the page lists
        # "1: Buy catfood" as an item on the tasks list


        # There is still a text box inviting her to add another item
        # She adds "Feed Whiskers the cat"


        # The page updates again, and now she has both items on her list


        # Jen wonders whether the site will remember her list.
        # Then she sees that the site has generated a unique URL for her
        # There is some explanatory text to that effect


        # She visits that URL and her tasks are still there.


        # Happy, she leaves the site


if __name__ == '__main__':
    unittest.main()