import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore

# auth stuff to connect to admin SDK
cred = credentials.Certificate("serviceCredentials.json")
firebase_admin.initialize_app(cred)

# firestore connection
store = firestore.client()

# two collection references
licences_ref = store.collection(u'business-licences')
owners_ref = store.collection(u'business-owners')

# all of our business licences
licences = licences_ref.stream()

# how many fields we changed
update_count = 0

for licence in licences:
    # grab the id of our account
    ref_to_owner = licence.to_dict()['ACCOUNT_NUMBER']

    # licence obj to update
    licence_ref = licences_ref.document(licence.id)

    # get the owner record if acct num matches
    results = owners_ref.where(u'ACCOUNT_NUMBER', u'==', ref_to_owner).stream()

    # res is our owner record
    for res in results:
        print(f'UPDATING FIELD: {licence.id}')
        update_count += 1
        licence_ref.update({
            u'BUSINESS_OWNER': res.to_dict()
        })

print(f'updated {update_count} fields')
