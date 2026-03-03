# Iterates through a mixed list, identifying emails, doubling numeric values,
# and printing everything else as-is.
def process_data(data_list):
    for item in data_list:
        if "@" in item:
            print("Email:", item)
        else:
            try:
                num = int(item)
                print("Number:", num * 2)
            except:
                print("Other:", item)