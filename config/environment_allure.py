class EnvironmentAllure:
    @staticmethod
    def create_environment(browser):
        with open('environment.properties', 'w', encoding='utf-8') as file:
            file.write("allure-report.version = 2.23.1" + '\n'+"python_version=3.12" + '\n')
            if browser == "chrome":
                file.write("browser=Chrome")
            elif browser == "firefox":
                file.write("browser=Firefox")