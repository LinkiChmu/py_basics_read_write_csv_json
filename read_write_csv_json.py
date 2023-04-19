import json


def json_to_dict(path):
    purchase = {}
    with open(path, 'r') as f:
        f.readline()
        for line in f:
            dict_ = json.loads(line)
            key = dict_['user_id']
            value = dict_['category']
            purchase[key] = purchase.setdefault(key, '') + value

        return purchase


def write_csv_add_column_existing_purchase(read_from, write_to, purchases):
    with open(read_from, 'r') as f:
        with open(write_to, 'w') as f2write:
            f.readline()
            for i, line in enumerate(f):
                line = line.strip().split(',')

                if purchases.get(line[0]):
                    row = f'{line[0]},{line[1]},{purchases.get(line[0])}\n'
                    f2write.write(row)


def main():
    purchases = json_to_dict('data/purchase_log.txt')
    print(purchases['1840e0b9d4'])

    write_csv_add_column_existing_purchase('data/visit_log.csv', 'data/funnel.csv', purchases)


main()
