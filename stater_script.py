import requests
import json

tag_url = 'http://localhost:8000/api/v1/productAPI/tag/'
category_url = 'http://localhost:8000/api/v1/productAPI/category/'
category_collection_url = 'http://localhost:8000/api/v1/productAPI/collection/'
attribute_url = 'http://localhost:8000/api/v1/productAPI/attribute/'
department_url = 'http://localhost:8000/api/v1/productAPI/department/'
category_pair_url = 'http://localhost:8000/api/v1/productAPI/categorypair/'

f = open('./data_script.json')

data = json.load(f)

def create_tags(tag):
  created_tag = requests.post(tag_url, data=tag)
  if created_tag.status_code != 201:
    print(tag)

for tag in data['tags']:
  create_tags(tag)

tags = {}
all_tags = requests.get(tag_url)
for tag in all_tags.json():
  tags[tag.get("Name")] = tag.get("Id")


requests.post(attribute_url, data={"Name": "Color"})

categories = {}
def create_categories(category, parent_id=None):
  category_tags = []
  if 'Tags' in category and len(category['Tags']):
    for category_tag in category['Tags']:
      category_tags.append(tags[category_tag])
  data = {
    "Name": category['Name'],
    "ParentId": parent_id,
    "Attributes": category['Attributes'],
    "Tags": category_tags, 
  }
  created_category = requests.post(category_url, data=data)
  if created_category.status_code == 201:
    categories[created_category.json().get("Name")] = created_category.json().get("Id")
    if ('children' in category):
      for child_category in category['children']:
        create_categories(child_category, created_category.json().get("Id"))
  else:
    print(data)

for category in data['categories']:
  create_categories(category)

all_categories = requests.get(category_url)
for category in all_categories.json():
  categories[category.get("Name")] = category.get("Id")

def create_category_pairs(category_pair):
  category_pair_tags = []
  for category_tag in category_pair['Tags']:
    category_pair_tags.append(tags[category_tag])

  category_pair_categories = []
  for category in category_pair['Categories']:
    category_pair_categories.append(categories[category])

  data = {
    "Name": category_pair['Name'],
    "Alias": category_pair['Alias'],
    "Categories": category_pair_categories,
    "Tags": category_pair_tags,
  }

  created_category_pair = requests.post(category_pair_url, json=data)
  if created_category_pair.status_code != 201:
    print(data)

for category_pair in data['category_pairs']:
  create_category_pairs(category_pair)

category_pairs = {}
all_category_pair = requests.get(category_pair_url)
for category_pair in all_category_pair.json():
  category_pairs[category_pair.get("Name")] = category_pair.get("Id")


def create_category_collection(collection):
  collection_category_pair = []
  if 'CategoryPairs' in collection and len(collection['CategoryPairs']):
    for category_pair in collection['CategoryPairs']:
      collection_category_pair.append(category_pairs[category_pair])
  collection_categories = []
  for category in collection['collection_categories']:
    category_tags = []
    if 'Tags' in category:
      for category_tag in category['Tags']:
        category_tags.append(tags[category_tag])
    tmp = {
      "Tags": category_tags,
      "CategoryId": categories[category["Name"]],
    }
    if "Alias" in category:
      tmp["Alias"] = category["Alias"]
    collection_categories.append(tmp)
  data = {
    "Name": collection['Name'],
    "Alias": collection['Alias'],
    "CategoryPairs": collection_category_pair,
    "collection_categories": collection_categories,
  }
  created_collection = requests.post(category_collection_url, json=data)
  if created_collection.status_code != 201:
    print(data)

for collection in data['category_collection']:
  create_category_collection(collection)

category_collections = {}
all_category_collection = requests.get(category_collection_url)

for collection in all_category_collection.json():
  category_collections[collection.get("Name")] = collection.get("Id")


def create_department(department):
  category_collection = []
  for collection_name in department['Collections']:
    category_collection.append(category_collections[collection_name])
  data = {
    "Name": department["Name"],
    "Collections": category_collection
  }
  created_department = requests.post(department_url, json=data)
  if created_department.status_code != 201:
    print(data)

for department in data["departments"]:
  create_department(department)

f.close()
