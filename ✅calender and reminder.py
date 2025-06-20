import calendar
import datetime

reminders = {}

def display_calendar(year, month):
    """Display the calendar for the given year and month."""
    print(f"\n📅 Calendar for {calendar.month_name[month]} {year}")
    print(calendar.month(year, month))


def add_reminder(year, month):
    """Add a reminder for a specific day."""
    while True:
        try:
            day = int(input("Enter the day of the month to set a reminder (1-31): "))
            if 1 <= day <= calendar.monthrange(year, month)[1]:
                break
            else:
                print(f"Invalid day! Enter between 1 and {calendar.monthrange(year, month)[1]}.")
        except ValueError:
            print("Invalid input! Please enter a number.")
        except EOFError:
            print("Input terminated. Exiting.")
            return False

    try:
        reminder_text = input("Enter the reminder: ")
    except EOFError:
        print("Input terminated. Exiting.")
        return False

    date_key = f"{year}-{month:02d}-{day:02d}"

    if date_key in reminders:
        reminders[date_key].append(reminder_text)
    else:
        reminders[date_key] = [reminder_text]

    print(f"✅ Reminder set for {date_key}: {reminder_text}")
    return True


def view_reminders(year, month):
    """View all reminders for a given month."""
    print(f"\n📌 Reminders for {calendar.month_name[month]} {year}:")
    found = False

    for day in range(1, calendar.monthrange(year, month)[1] + 1):
        date_key = f"{year}-{month:02d}-{day:02d}"
        if date_key in reminders:
            print(f"{date_key}: {', '.join(reminders[date_key])}")
            found = True

    if not found:
        print("No reminders set for this month.")


def delete_reminder(year, month):
    """Delete all reminders for a specific day."""
    while True:
        try:
            day = int(input("Enter the day to delete reminders from (1-31): "))
            if 1 <= day <= calendar.monthrange(year, month)[1]:
                break
            else:
                print(f"Invalid day! Enter between 1 and {calendar.monthrange(year, month)[1]}.")
        except ValueError:
            print("Invalid input! Please enter a number.")
        except EOFError:
            print("Input terminated. Exiting.")
            return False

    date_key = f"{year}-{month:02d}-{day:02d}"

    if date_key in reminders:
        print(f"Reminders on {date_key}: {', '.join(reminders[date_key])}")
        try:
            confirm = input("Are you sure you want to delete all reminders for this day? (y/n): ").lower()
        except EOFError:
            print("Input terminated. Exiting.")
            return False

        if confirm == 'y':
            del reminders[date_key]
            print("🗑️ Reminders deleted.")
        else:
            print("Deletion canceled.")
    else:
        print("No reminders found for this day.")

    return True


def main():
    """Main loop to run the reminder calendar app."""
    current_date = datetime.datetime.now()
    year = current_date.year
    month = current_date.month

    while True:
        display_calendar(year, month)

        print("\nOptions:")
        print("1. Set a reminder")
        print("2. View reminders")
        print("3. Delete a reminder")
        print("4. Change month/year")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))
        except (ValueError, EOFError):
            print("Invalid or terminated input. Exiting.")
            break

        if choice == 1:
            if not add_reminder(year, month):
                break
        elif choice == 2:
            view_reminders(year, month)
        elif choice == 3:
            if not delete_reminder(year, month):
                break
        elif choice == 4:
            try:
                year = int(input("Enter year (e.g., 2025): "))
                month = int(input("Enter month (1-12): "))
                if not (1 <= month <= 12):
                    print("Invalid month! Reverting to current month/year.")
                    year, month = current_date.year, current_date.month
            except ValueError:
                print("Invalid input! Reverting to current month/year.")
                year, month = current_date.year, current_date.month
            except EOFError:
                print("Input terminated. Exiting.")
                break
        elif choice == 5:
            print("👋 Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()
