from doors_kata import doors100
door_list = []
doors = doors100()

if __name__ == '__main__':

    def test_should_create_100_doors():
        doors.create_100_doors(door_list)
        assert len(door_list) == 100

    def test_pass_by_doors():
        doors.pass_by_door(door_list)