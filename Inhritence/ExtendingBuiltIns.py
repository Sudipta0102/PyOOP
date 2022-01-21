class ContactList(list):
    def search(self, name):
        ''' search method returns a list containing name mentioned in the
        search value in their name'''
        matching_contacts = [] 
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts        

class Contact:
    all_contacts = ContactList()

    def __init__(self, email, name):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


c1 = Contact('a@something.com', 'a')
c2 = Contact('b@something.com', 'b')
c3 = Contact('bb@something.com', 'bb')
c4 = Contact('ab@something.com', 'ab')

#print(Contact.all_contacts)

matched_list = [c.name for c in Contact.all_contacts.search('a')]
print(Contact.all_contacts.search('a'))

print(matched_list)