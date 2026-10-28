
"""Manage fitness class bookings and roster exports."""

import json
from pathlib import Path

class_capacity = {"Yoga": 3, "HIIT": 2, "Spin": 4}
rosters = {}


def book_class(member_id, class_name, attendance_log=None):
    """Book a member into a class if capacity permits."""
    if attendance_log is None:
        attendance_log = []

    if class_name not in rosters:
        rosters[class_name] = []

    capacity = class_capacity.get(class_name, 0)
    if len(rosters[class_name]) >= capacity:
        print("Class full:", class_name)
        return False

    rosters[class_name].append(member_id)
    attendance_log.append(f"{member_id} -> {class_name}")
    return True


def cancel_booking(member_id, class_name):
    """Cancel an existing booking."""
    try:
        rosters[class_name].remove(member_id)
    except (KeyError, ValueError):
        print("Nothing to cancel")


def set_capacity(class_name, seats):
    """Set a non-negative class capacity."""
    if seats < 0:
        print("Capacity cannot be negative")
        return False
    class_capacity[class_name] = seats
    return True


def add_members(class_name, count):
    """Add the requested number of guest members."""
    if count < 0:
        print("Guest count cannot be negative")
        return

    for index in range(count):
        book_class(f"GUEST-{index}", class_name)


def export_roster(file="gym_schedule.json"):
    """Export rosters to a JSON file."""
    with open(file, "w", encoding="utf-8") as roster_file:
        json.dump(rosters, roster_file, indent=4)


def clear_old_exports(prefix="old_"):
    """Delete matching old JSON files from the current directory."""
    for file_path in Path(".").iterdir():
        if (
            file_path.is_file()
            and file_path.name.startswith(prefix)
            and file_path.suffix == ".json"
        ):
            try:
                file_path.unlink()
            except OSError as error:
                print(f"Could not delete {file_path}: {error}")


def show_rosters():
    """Print each class and its roster."""
    for class_name, members in rosters.items():
        print(class_name, ":", ", ".join(str(member) for member in members))


def main():
    """Run the fitness booking demonstration."""
    book_class("M1", "Yoga")
    book_class("M2", "Yoga")
    book_class("M3", "Yoga")
    book_class("M4", "Yoga")
    book_class(55, "HIIT")
    book_class("M5", "Pilates")
    set_capacity("Spin", -2)
    add_members("Spin", 3)
    cancel_booking("M9", "Boxing")

    try:
        guest_count = int(
            input("How many walk-in guests for HIIT? (Enter for 1): ") or "1"
        )
        add_members("HIIT", guest_count)
    except ValueError:
        print("Please enter a valid whole number.")

    clear_old_exports()
    export_roster()
    show_rosters()


if __name__ == "__main__":
    main()
