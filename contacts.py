import json

def loadContacts():
    try:
        with open("contacts.json",'r') as file:
            contacts=json.load(file)
    except FileNotFoundError:
        contacts=[]
    return contacts

def savecontacts(contacts):
    with open("contacts.json",'w') as file:
        json.dump(contacts,file,indent=4)

def addcontacts():
    name=input("Enter the name: ")
    number=input("enter the number: ")
    email=input("enter the email: ")
    for contact in contacts:
        if contact['number']==number:
            print("the number is aleayed exists")
            return
    contact={'name': name,'number': number,'email': email}
    contacts.append(contact)
    savecontacts(contacts)
    print("success saved")

def deleteContacts():
    name=input("Enter the name of the contact that you need to delete it: ")
    for contact in contacts:
        if contact['name']==name:
            contacts.remove(contact)
            savecontacts(contacts)
            print("succes deleted")
            return
    print("the contact is not found")

def editContacts():
    name=input("Enter the name of the contact that you need to edit it: ")
    for contact in contacts:
        if contact['name']==name:
            print("the contact details are:")
            print(f"name:{contact['name']}")
            print(f"number: {contact['number']}")
            print(f"email: {contact['email']}")
            print(f"if you don't need to edit any thing leave empty")
            newname=input("Enter the new name: ")
            newnumber=input("Enter the new number: ")
            newemail=input("Enter the new email: ")
            if newname:
                contact['name']=newname 
            if newnumber:
                contact['number']=newnumber
            if newemail:
                contact['email']=newemail

            savecontacts(contacts)
            print("success edit")
            return
    print("the contact is not found")

def searchcontacts():
    name=input("Enter the name of the contact that you need to sereach for: ")
    for contact in contacts:
        if contact['name']==name:
            print("the contact details are:")
            print(f"name:{contact['name']}")
            print(f"number: {contact['number']}")
            print(f"email: {contact['email']}")

    print("the contact is not found")

def showContacts():
    if not contacts:
        print("not contacts found")
    else:
        for contact in contacts:
            print(f"name:{contact['name']}")
            print(f"number: {contact['number']}")
            print(f"email: {contact['email']}")
            print("------------------------")
            


contacts=loadContacts()

while True:
    print("###########choose one of those:##############")
    print("1-add ")
    print("2-edit ")
    print("3-delete ")
    print("4-search ")
    print("5-show ")
    print("6-quit ")
    choise=input("Enter you choise here: ")
    if choise=='1':
        addcontacts()
    elif choise=='2':
        editContacts()
    elif choise=='3':
        deleteContacts()
    elif choise=='4':
        searchcontacts()
    elif choise=='5':
        showContacts()
    elif choise=='6':
        break

    else:
        print("invial choise ")