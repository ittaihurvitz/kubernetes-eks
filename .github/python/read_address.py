
import requests
from argparse import ArgumentParser


class ParseAddress:
    def __init__(self, text: str):
        """
        Get input of multiline text.
        Parse the 'Address:' value from this text.
        """
        self.text = text

    def find_address_line(self):
        """
        Finds line containing the word "Address:" and truncates the rest of line.
        :return: truncated line.
        """
        lines = self.text.splitlines()  # Split the text into individual lines
    
        for line in lines:
            # Check if "Address" is in the line
            if 'Address:' in line:
                truncated = line.split('Address:', 1)[1]
                return truncated.strip()
        
        return ""


class BrowseAddress():
    """
    browse to the input url
    """

    def __init__(self, url: str):
        """
        Get input of multiline text.
        Parse the 'Address' value from this text.
        """
        self.url = url

 
    def run(self):
        full_url = "http://" + self.url
        response = requests.get(full_url)
        if response.status_code == 200:
            print("OK")
        else:
            raise Exception("Failed to browse the url.")
        


# Main function
if __name__ == "__main__":
    debug = False

    parser = ArgumentParser()
    parser.add_argument("--input_text")

    args = parser.parse_args()
    
    extractor = ParseAddress(args.input_text)
    address = extractor.find_address_line()
    
    if address:
        print(address)

        # remark: when running debug the job will fail due to untreated multiline
        if debug:
            checker = BrowseAddress(address)
            checker.run()
    else:
        print("Address was not found")
    