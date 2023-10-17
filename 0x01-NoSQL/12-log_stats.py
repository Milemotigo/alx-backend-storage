# #!/usr/bin/env python3
# """
# 12. Log stats
# """
# from pymongo import MongoClient

# def nginx_logs_stats():
#     """
#     Connect to the MongoDB server and select the log database
#     Get the total number of documents in the collection
#     Count the number of documents with each HTTP method
#     """

#     try:
#         with MongoClient("mongodb://localhost:27017") as client:
#             db = client.logs
#             collection = db.nginx

#             total_logs = collection.count_documents({})

#             methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
#             method_counts = {method: collection.count_documents({"method": method}) for method in methods}

#             special_query = {"method": "GET", "path": "/status"}
#             special_count = collection.count_documents(special_query)

#             print(f"{total_logs} logs")
#             print("Methods:")
#             for method in methods:
#                 print(f"\t{method}: {method_counts[method]}")
#             print(f"{special_count} status check")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     nginx_logs_stats()
#!/usr/bin/env python3
"""update many to affect changes"""

from pymongo import MongoClient


def nginx_stats_check():
    """provides some stats about Nginx logs stored in MongoDB:"""
    client = MongoClient()
    collection = client.logs.nginx

    doc_count = collection.count_documents({})
    print('{} logs'.format(doc_count))

    methods_list = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods_list:
        method_count = collection.count_documents({"method": method})
        print('\tmethod {}: {}'.format(method, method_count))
    status_count = collection.count_documents({
        "method": "GET", "path": "/status"
    })
    print('{} status check'.format(status_count))


if __name__ == "__main__":
    nginx_stats_check()