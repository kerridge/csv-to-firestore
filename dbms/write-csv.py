import csv
import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./serviceCredentials.json")
app = firebase_admin.initialize_app(cred)

# firestore connection
store = firestore.client()

# csv path and name of firestore collection to create
file_path = "data-subsets/business-licences-subset-utf-8.csv"
collection_name = "business-licences"


# basically a method to stop the whole csv from being loaded into memory
def batch_data(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]


def get_data_item(item, data_type):
	# Add other data types you want to handle here
    if data_type == 'int':
        return int(item)
    elif data_type == 'bool':
        return bool(item)
    else:
        return item


# data to return
data = []
# our list of csv coulmn headers to be extracted
headers = []

data_types = []
with open(file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        # extract the line headers
        if line_count == 0:
            for header in row:
                headers.append(header)
            line_count += 1
        else:
            obj = {}
            for idx, item in enumerate(row):
                # obj[headers[idx]] = item
                get_data_item(item, data_types[idx])
            data.append(obj)
            line_count += 1
    print(f'Processed {line_count} lines.')


# loop through and write data to firestore
# a batch is a set of transactions that have been grouped together
for batched_data in batch_data(data, 499):
    batch = store.batch()
    for data_item in batched_data:
        # grab our document reference object
        doc_ref = store.collection(collection_name).document()
        batch.set(doc_ref, data_item)
    batch.commit()

print('Done')