"""
This Python script shortens a URL using the Bitly service. 
It first prompts the user to enter a URL to shorten. 
Then, it uses the TinyURL service to shorten the URL and stores the shortened URL in a variable. 
Finally, it prints the shortened URL to the console. 
This code can be useful for shortening long URLs to make them easier to share or type, 
such as when posting on social media or sending in an email.

"""
# import the pyshorteners library as alias ps
import pyshorteners as ps

# get the url to shorten from the user
url = input('insert random url you would like to shorten: ')

# invoke the shortener method from the pyshorteners library
# store it in a variable shortener
shortener = ps.Shortener()


# shorten the URL in the url variable
# store the shortened url in the short_form_url variable
short_form_url = shortener.tinyurl.short(url)

# print the short_form_url to the console
print('The short_form_url for the provided url_address is', short_form_url)
