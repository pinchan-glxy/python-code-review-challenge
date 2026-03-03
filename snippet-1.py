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