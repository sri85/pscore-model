from gousto_model.pages.base_page import BasePage
from gousto_model.pages.locators import Locators


class RecipePage(BasePage):
    def load(self, url=None):
        """

        Parameters
        ----------
        url: URL that needs to be loaded.

        Returns True if the webdriver was able to load the page successfully.
        -------

        """

        if url is None:
            url = self.config.get_homepage()

        self.driver.get(url)

        return self

    def is_loaded(self):
        """
        Checks whether the healthy recipes page is loaded within 10 seconds, else return False
        """

        self.driver.wait.until_visible(Locators.GOUSTO_HEADER, timeout=10,
                                       message='Recipe Page did not load as expected')
        self.driver.wait.until_visible(Locators.GOUSTO_FOOTER, timeout=10,
                                       message='Recipe page did not load as expected')
        return True

    def select_delivery_date(self):
        """

        Allows the user to select the desired delivery date

        """
        self.driver.find_element(*Locators.SELECT_DELIVERY_DATE).click()

    def get_delivery_date(self):
        """

        Returns: the selected delivery date
        -------

        """
        delivery_date = self.driver.find_element(*Locators.SELECT_DELIVERY_DATE).text
        return delivery_date

    @staticmethod
    def get_checkout_url():
        """

        Returns: URL for checkout
        -------

        """
        return 'https://www.gousto.co.uk/checkout'

    def check_delivery_date_matches_selected_date(self, expected_date):
        """

        Parameters
        ----------
        expected_date: Data to be matched in the checkout cart

        Returns Boolean , True if the user selected date matches the delivery date selected by the user, else False.
        -------

        """
        delivery_date = self.driver.find_element(*Locators.DELIVERY_DATE)
        return delivery_date.text == expected_date

    def add_recipe(self):
        """

       Method to add a desired recipe to the checkout page

        """
        self.driver.find_element(*Locators.ADD_BUTTON).click()

    def check_added_recipe(self):
        """

        Returns True if the recipe was added successfully it checks for the text in the Recipe to be "ADDED"
        -------

        """
        return self.driver.find_element(*Locators.ADDED_BUTTON).text == 'ADDED'

    def remove_recipe(self):
        """

       Method to remove the recipe.

        """
        self.driver.find_element(*Locators.REMOVE_BUTTON).click()

    def show_info(self):
        """

        Opens the description of a recipe and checks for some basic info of a recipe is displayed properly

        """
        self.driver.find_element(*Locators.MAIN_RECIPE).click()
        self.driver.find_element(*Locators.RECIPE_INFO).is_displayed()

    def close_info(self):
        """

        Method to close the modal dialog of recipe box

        """
        self.driver.find_element(*Locators.BUTTON_CLOSE).click()

    def checkout(self):
        """

        Method to proceed to checkout

        """
        self.driver.find_element(*Locators.CHECKOUT_BUTTON).click()

    def checkout_page(self):
        """

        Returns True if the user is in checkout page.
        -------

        """
        checkout_url = RecipePage.get_checkout_url()
        return self.driver.current_url == checkout_url

    def toggle_portions(self):
        """

        Returns Allows user to toggle portions from 2 to 4.
        -------

        """
        self.driver.find_element(*Locators.PORTION_TOGGLE_BUTTON).click()

    def verify_portion_text(self, portions):
        """

        Parameters
        ----------
        portions : Pass the portions that you expect to be in the checkout cart

        Returns True if the portions matches the user entered.
        -------

        """
        return self.driver.find_element(*Locators.PORTION_TEXT).text.strip() == '{} Portions'.format(portions)

    def add_two_more_portions(self):
        """

        Allows user to increment the portions by clicking on the "Add 2 more portions" button.

        """
        self.driver.find_element(*Locators.ADD_MORE_RECIPES).click()

    def verify_alert_message(self):
        """

        Returns True if the alert message is displayed.
        -------

        """
        return self.driver.find_element(*Locators.ERROR_ALERT).is_displayed()


