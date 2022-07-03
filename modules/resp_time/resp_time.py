import json
import requests
from ...utils import config
# temp_log = []
# response = requests.get("https://google.com")
# print(response.elapsed.total_seconds())
# while True:
#     try:
#         with open('log.json', 'r') as file_object:
#             data = json.load(file_object)
#     except:
#         with open('log.json', 'w') as file_object:  # open the file in write mode
#             json.dump(temp_log, file_object)
#         continue
#     break
# new_data = list(data)
# print(new_data)
# new_data.append(response.elapsed.total_seconds())
# with open('log.json', 'w') as file_object:  #open the file in write mode
#     json.dump(new_data, file_object)

#     print(new_data)


class responseTracker(config):

    """Main class for managing response-time logic"""

    def __init__(self):
        """TODO: to be defined. """
        pass

    def loadData(self):
        """Loads data from disk"""
        pass
        print(self.ass)
    def dumpData(self):
        """Writes data to disk"""
        pass
    def cacheLogic(self):
        """Check if file exists and if it is empty, old, or outdated"""
        pass

resp = responseTracker()
resp.loadData()
