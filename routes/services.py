from trains.models import Train


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in graph.keys():
            for next_ in graph[vertex] - set(path):
                if next_ == goal:
                    yield path + [next_]
                else:
                    stack.append((next_, path + [next_]))


def get_graph(qs):
    graph = dict()

    for q in qs:
        graph.setdefault(q.from_city_id, set())
        graph[q.from_city_id].add(q.to_city_id)

    return graph


def sort_routes(routes):
    sorted_routes = []
    if len(routes) == 1:
        sorted_routes = routes
    else:
        times = sorted(list(set(r['total_time'] for r in routes)))
        for t in times:
            for r in routes:
                if t == r['total_time']:
                    sorted_routes.append(r)

    return sorted_routes


def get_routes(form) -> dict:
    qs = Train.objects.all().select_related('from_city', 'to_city')
    graph = get_graph(qs)
    data = form.cleaned_data

    from_city = data['from_city']
    to_city = data['to_city']
    cities = data['cities']
    travelling_time = data['travelling_time']
    all_routes = list(dfs_paths(graph, from_city.id, to_city.id))

    if not len(all_routes):
        raise ValueError('Маршрута, удовлетворяющего условиям не существует')
    if cities:
        _cities = [city.id for city in cities]
        my_routes = []
        for r in all_routes:
            if all(city in r for city in _cities):
                my_routes.append(r)
        if not my_routes:
            raise ValueError('Маршрут через указанные города невозможен')
    else:
        my_routes = all_routes

    final_routes = []
    all_trains = dict()
    for q in qs:
        all_trains.setdefault((q.from_city_id, q.to_city_id), [])
        all_trains[(q.from_city_id, q.to_city_id)].append(q)

    for r in my_routes:
        tmp = dict()
        tmp['trains'] = []
        total_time = 0
        for i in range(len(r) - 1):
            qs = all_trains[(r[i], r[i + 1])]
            total_time += qs[0].travel_time
            tmp['trains'].append(qs[0])
        tmp['total_time'] = total_time

        if total_time <= travelling_time:
            final_routes.append(tmp)

    if not final_routes:
        raise ValueError('Время в пути больше заданного')

    return {'form': form, 'routes': sort_routes(final_routes), 'cities': {
        'from_city': from_city.name, 'to_city': to_city.name
    }}
