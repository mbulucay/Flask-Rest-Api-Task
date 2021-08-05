
class Company():
    def __init__(self, name, catchPhrase, bs):
        self.name = name
        self.catchPhrase = catchPhrase
        self.bs = bs

    def __str__(self):
        return self.name + " " + self.catchPhrase + " " + self.bs

class Geo:
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng       
    
    def __str__(self):
        return self.lat + " " + self.lng


class Address():
    def __init__(self, street, suite, city, zipcode, geo:Geo):
        self.street = street
        self.suite = suite
        self.city = city
        self.zipcode = zipcode
        self.geo = geo

    def __str__(self):
        return self.street + " " + self.suite + "\n" + self.city + " " + self.zipcode + "\n" + str(self.geo)



class User():

    def __init__(self, id, name, username, email, 
                address:Address, phone, website, company:Company):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.address = address
        self.phone = phone
        self.website = website
        self.company = company


class Album():

    def __init__(self, userId, id, title):
        self.userId = userId
        self.id = id
        self.title = title
        

        