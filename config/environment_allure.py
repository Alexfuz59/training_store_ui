import platform


class EnvironmentAllure:

    environment = {'OC': platform.platform(),
                   'Python_version': platform.python_version(),
                   'Allure-report.version': '2.23.1'
                   }

    @staticmethod
    def create_environment(browser, env=environment):
        with open('environment.properties', 'w', encoding='utf-8') as file:
            for key, value in env.items():
                file.write(f'{key}: {value}' + '\n')
            if browser == "chrome":
                file.write("Browser: Chrome")
            elif browser == "firefox":
                file.write("Browser: Firefox")
