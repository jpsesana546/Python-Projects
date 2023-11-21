class doors100():

    def __init__(self) -> None:
        door_list = []
        pass

    def create_100_doors(self, door_list) -> None:
        for _ in range(100):
            door_list.append(_)
        return door_list

    def pass_by_door(self, door_list):
        for door in door_list:
            print(f"Door {door}")

    # Create 100 doors
        # Pass through each door
        # Go back to beginning
        # Pass through every other door
        # Go back to beginning
        # repeat
