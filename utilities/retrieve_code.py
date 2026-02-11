import json
import time
from selenium.common import WebDriverException


def retrieve_phone_code(driver) -> str:
    """
    Retrieve SMS verification code from browser performance logs.
    
    This function extracts the phone verification code that is sent
    during the phone number confirmation process. It searches through
    the browser's performance logs to find the API response containing
    the code.
    
    Args:
        driver: Selenium WebDriver instance with performance logging enabled
        
    Returns:
        String containing the SMS verification code
        
    Raises:
        WebDriverException: If code cannot be retrieved from logs
        
    Note:
        Requires Chrome driver with performance logging capability enabled:
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
    """

    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code
