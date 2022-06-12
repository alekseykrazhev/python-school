# Final Task Python School project by Aleksey Krazhevskiy

from WorkWithCsv import get_distance_from_csv, count_complexity
from GetMinimalPath import get_best_route


if __name__ == '__main__':
    # автопарк: тип машины, проходимость, расход топлива
    cars = {'car': [3, 10], 'bus': [1, 15], 'truck': [2, 12], 'suv': [6, 18]}

    cities_list, keys = get_distance_from_csv('map.csv')

    start_city = input('Enter start city:')
    end_city = input('Enter final city:')
    visit_cities = list(input('Enter list of cities to visit (through a space):').split())
    car_type = input('Enter type of car to use (car, bus, truck, suv):')

    # test data
    """
    start_city = 'Gomel'
    end_city = 'Rome'
    visit_cities = ['Brest', 'London', 'Frankfurt', 'Moscow', 'Paris']
    car_type = 'simple'
    """

    if car_type not in cars.keys():
        print(f"Car {car_type} is not in the list of cars")
        exit()

    if start_city not in keys or end_city not in keys:
        print(f"City {start_city} or {end_city} not found")
        exit()

    if start_city == end_city:
        print('Start and end city are the same')
        exit()

    for city in visit_cities:
        if city not in keys:
            print(f"City {city} is not in the map")
            exit()

    car = cars[car_type]
    routes = count_complexity(cities_list, car, keys)

    get_best_route(routes, start_city, end_city, visit_cities)
