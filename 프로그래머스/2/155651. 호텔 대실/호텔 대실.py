def solution(book_time):
    book_time_sort = sorted([[int(i[0].split(':')[0])*60+int(i[0].split(':')[1]),int(i[1].split(':')[0])*60+int(i[1].split(':')[1])] for i in book_time])

    rooms = []
    for customer in book_time_sort:
        for idx, room in enumerate(rooms):
            if room[1]+10 <= customer[0]:
                rooms[idx] = customer
                break
        else:
            rooms.append(customer)
    
    return len(rooms)