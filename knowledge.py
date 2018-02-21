##dict of response for each type of intent
import random


startsearch_response_dict = {
    "delhi":'<Here is a list of top 5 startups in Delhi based on the funding amount: <UL><li>Snapdeal</li><li>Hike</li><li>Oyo</li><li>Delhivery</li><li>OyoRooms</li></ul>For more info: <a href=\"http://www.github.com/lkamat\">Startups in Mumbai</a>',
    "bangalore":'Here is a list of top 5 startups in Bangalore based on the funding amount: <UL><li>Paytm</li><li>Flipkart</li><li>Ola</li><li>Ola Cabs</li><li>Paytm Marketplace</li></ul>For more info: <a href=\"http://www.github.com/lkamat\">Startups in India</a>',
    "mumbai":'Here is a list of top 5 startups in Mumbai based on the funding amount: <UL><li>CarTrade</li><li>Fractal Analytics</li><li>BookMyShow</li><li>FreeCharge</li><li>Cartrade</li></ul>For more info: <a href=\"http://www.github.com/lkamat\">Startups in India</a>',
    "faq_link":'You can check out the list of startups here <a href=\"http://www.github.com/lkamat\">Startups in India</a>'
}


startupinfo_respose_dict = {
    "investors":'Here are the top 5 investors: <UL><li>Undisclosed Investors</li><li>Kalaari Capital</li><li>Indian Angel Network</li><li>Info Edge (India) Ltd</li><li>Brand Capital</li></ul>For more info: <a href=\"http://www.github.com/lkamat\">Startups in India</a>',
    "startups":'Top 5 startups based on funding.<UL><li>Paytm</li><li>Flipkart</li><li>Ola</li><li>Ola Cabs</li><li>Oyo Rooms</li></ul> For more info: <a href="http://www.github.com/lkamat">Startups in India</a>',
    "industries":'Top 5 industries based on funding.<UL><li>Consumer Internet</li><li>Technology </li><li>ecommerce </li><li>Logistics </li><li>Education</li></ul>For more info: <a href="http://www.github.com/lkamat">Startups in India</a>',
    "categories":'Top 5 categories based on funding.<UL><li>Food Delivery Platform</li><li>Online lending platform</li><li>eOnline Pharmacy</li><li>Online Learning Platform</li><li>ECommerce Marketplace</li></ul>For more info: <a href="http://www.github.com/lkamat">Startups in India</a>',
    "city": 'Top 5 cities with the most startup funding:<UL><li>Bangalore</li><li>Mumbai</li><li>New Delhi</li><li>Gurgaon</li><li>Pune</li></ul>For more info: <a href="http://www.github.com/lkamat">Startups in India</a>',
    "type": 'Startup funded by investment type:<UL><li>Private Equity</li><li>Seed Funding </li><li>Debt Funding </li></ul>Fo rmore info: <a href="http://www.github.com/lkamat">Startups in India</a>',
    "faq_link":'You can check out the list of startups here <a href="http://www.github.com/lkamat">Startups in India</a>'
}


GREETING_RESPONSES = ["sup bro", "hey", "*nods*", "how can i help?", "what kind of food are you craving for today","<h1>hello</h1>"]
GOODBYE_RESPONSES = ["bye", "cya", "take care", "good", "bye bye","<h1>BYEo</h1>"]
AFFIRM_RESPONSES = ["indeed", "OK", "that's right", "great", "cool"]


def greeting():
    """If any of the words in the user's input was a greeting, return a greeting response"""
    return random.choice(GREETING_RESPONSES)

def goodbye():
    """If any of the words in the user's input was a goodbye, return a goddbye response"""
    return random.choice(GOODBYE_RESPONSES)

def affirm():
    """If any of the words in the user's input was a goodbye, return a goddbye response"""
    return random.choice(AFFIRM_RESPONSES)


def startup_search(entities):
    if entities == []:
        return "Could not find out specific information about this ..." +  startsearch_response_dict["faq_link"]
    if len(entities) >= 1:
        return startsearch_response_dict[entities[0]['value']]
    return "Sorry.." + startsearch_response_dict["faq_link"]

def startup_info(entities):
    if entities == []:
        return "Could not find out specific information about this ..." +  startupinfo_response_dict["faq_link"]
    if len(entities) >= 1:
        return startupinfo_response_dict[entities[0]['value']]
    return "Sorry.." + startupinfo_response_dict["faq_link"]

def invest_info(entities):
    if entities == []:
        return "Could not find out specific information about this ..." +  investinfo_response_dict["faq_link"]
    if len(entities) >= 1:
        return investinfo_response_dict[entities[0]['value']]
    return "Sorry.." + investinfo_response_dict["faq_link"]

def indust_info(entities):
    if entities == []:
        return "Could not find out specific information about this ..." +  industryinfo_response_dict["faq_link"]
    if len(entities) >= 1:
        return industryinfo_response_dict[entities[0]['value']]
    return "Sorry.." + industryinfo_response_dict["faq_link"]


