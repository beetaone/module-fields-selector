"""
This file implements module's main logic.
Data processing should happen here.

Edit this file to implement your module.
"""

from logging import getLogger
import os

log = getLogger("module")

__ACTION__ = os.getenv("ACTION", "keep")
if os.getenv("FIELDS"):
    __FIELDS__ = [field.strip() for field in os.getenv("FIELDS").split(',')]
else:
    __FIELDS__ = None

def getSelectedData(data):
    selected_data = {}

    for field in list(data.keys()):
        if (field in __FIELDS__ and __ACTION__ == "keep") or (not field in __FIELDS__ and __ACTION__ == "remove"):
            selected_data[field] = data[field]

    return selected_data

def module_main(received_data: any) -> [any, str]:
    """
    Process received data by implementing module's main logic.
    Function description should not be modified.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        any: Processed data that are ready to be sent to the next module or None if error occurs.
        str: Error message if error occurred, otherwise None.

    """

    log.debug("Processing ...")

    try:
        if type(received_data) == list:
            processed_data = []
            for data in received_data:
                processed_data.append(getSelectedData(data))
        else:
            processed_data = getSelectedData(received_data)

        return processed_data, None

    except Exception as e:
        return None, f"Exception in the module business logic: {e}"
