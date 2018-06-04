n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    persons = []
    for _ in range(n):
       person = str(input().strip())
       persons.append(person)
    size = len(persons)
    max_topics_numbers = 0
    teams = 0
    for i in range(0, size):
        for j in range(i + 1, size):
            topics = str("{0:b}".format((int(persons[i], 2) | int(persons[j], 2))))
            if topics.count("1") > max_topics_numbers:
                max_topics_numbers = topics.count("1")
                teams = 1
            else:
                if topics.count("1") == max_topics_numbers:
                    teams += 1
    print(max_topics_numbers)
print(teams)
