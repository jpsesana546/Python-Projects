from doors_kata import doors100
door_list =[]

def test_should_create_100_doors():
    doors = doors100()
    doors.create_100_doors(door_list)
    assert len(door_list) == 100