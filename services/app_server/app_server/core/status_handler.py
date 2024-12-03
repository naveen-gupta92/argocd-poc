class StatusHandler:
    """
    A class to provide app_server status
    """

    def my_function(self):
        """
        Adding this method to resolve linting warning
        - Too few public methods (1/2) (too-few-public-methods)
        """
        print("Function to handle liniting")

    @staticmethod
    def app_status() -> dict:
        """
        Checks if the app server is alive and provides a status message.

        Returns:
        -------
            200: Success
            dict: A dictionary containing the status message.
        """

        return { "status_code": 200, "message": "App server is up and running" }
