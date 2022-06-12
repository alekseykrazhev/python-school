# functions to work with csv map and get distances for certain car type

def get_distance_from_csv(filename: str) -> [dict, dict]:
    """
    This function takes a csv file and returns a list of distances
    :param filename: csv file
    :return: list of distances, list of cities
    """
    with open(filename, 'r') as file:
        rdata = file.readlines()     # read raw data (str)
    data = {}
    keys = []
    for record in rdata:
        values = record.split(',')
        if values[0] not in keys:
            keys.append(values[0].strip())
        if values[1] not in keys:
            keys.append(values[1].strip())
        if values[0].strip() not in data.keys():
            data[values[0].strip()] = [1, values[1].strip(), float(values[2]), float(values[3])]
        else:
            data[values[0].strip()][0] += 1
            data[values[0].strip()] += [values[1].strip(), float(values[2]), float(values[3])]
        if values[1].strip() not in data.keys():
            data[values[1].strip()] = [1, values[0].strip(), float(values[2]), float(values[3])]
        else:
            data[values[1].strip()][0] += 1
            data[values[1].strip()] += [values[0].strip(), float(values[2]), float(values[3])]
    return data, keys


def count_complexity(data: dict, car: list, keys: list) -> dict:
    """
    This function counts the complexity of the route for certain car type
    :param keys: list of cities
    :param car: car type
    :param data: dictionary of distances
    :return: complexity of the route
    """
    complexity = {}

    for key in keys:
        # formula: S * ([1] / 100) * (cof / [0])
        complexity[key] = {}
        city = 1
        distance = 2
        comp = 3
        for key1 in keys:
            complexity[key][key1] = float('Inf')
        if key not in data.keys():
            continue
        for i in range(data[key][0]):
            complexity[key][data[key][city]] = data[key][distance] * (car[1] / 100) * (data[key][comp] / car[0])
            city += 3
            distance += 3
            comp += 3

    return complexity

