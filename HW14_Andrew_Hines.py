#Andrew Hines
#HW 14
#04/29/2025
import re
from html.parser import HTMLParser
from urllib.request import urlopen
from tkinter import *
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# Define parser class
class MyHTMLParser(HTMLParser):
    """ Subclass of HTMLParser that extracts clean data from HTML, tracks word
      frequency, and dumps text to a file"""

    def __init__(self):
        """ Initialize parser and creates an empty list to store data"""
        super().__init__()
        self.emails = []

    def handle_data(self, data):
        """ Handle the text data and collect emails"""
        email_pattern = r'[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
        """looks for email regular expression"""
        words = data.split()
        for word in words:
            match = re.search(email_pattern, word)
            if match:
                self.emails.append(match.group().lower())

    def collect_emails(self):
        return '\n'.join(self.emails)
    """returns a list of emails found in the HTML document"""
# Define button click action
def click():
    url = text_entry.get()
    try:
        response = urlopen(url)
        content = response.read()
        html_doc = content.decode().lower()
        parser = MyHTMLParser()
        parser.feed(html_doc)
        output.delete(1.0, END)  # Clear previous output
        output.insert(END, parser.collect_emails())
    except Exception as e:
        output.delete(1.0, END)
        output.insert(END, f"Error: {e}")

# Set up GUI
window = Tk()
window.title("Email Finder")
window.configure(background="green")
"""creates a window with a title and background color"""

Label(window, text="Enter URL:", bg="green", font="none 12 bold").grid(row=0, column=0, sticky=W)
text_entry = Entry(window, width=40, bg="white", fg = "black")
text_entry.grid(row=1, column=0, sticky=W)
"""creates a label and entry box for the user to enter a URL"""

Button(window, text="SUBMIT", command=click).grid(row=2, column=0, sticky=W)
"""creates a button that calls the click function when clicked"""

output = Text(window, width=50, height=10, wrap=WORD, background="white", fg = "black")
output.grid(row=3, column=0, padx=10, pady=10)
"""creates a text box to display the emails found"""

window.mainloop()
"""starts the GUI event loop"""
