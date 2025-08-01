"""
estimate time: 40min
actual time:
"""
import datetime
from prac_07.project import Project

def main():
    """Main program: Loads default items, displays menus and handles user operations"""
    print("Welcome to Pythonic Project Management")
    default_file = "projects.txt"
    projects = load_projects(default_file)
    print(f"Loaded {len(projects)} projects from {default_file}")

    exit_program = False
    while not exit_program:
        print("\n-(L)oad projects -(S)ave projects -(D)isplay projects -(F)ilter projects by date "
              "-(A)dd new project -(U)pdate project -(Q)uit")
        choice = input(">>> ").strip().upper()

        if choice == 'L':
            filename = input("Enter filename to load from: ")
            try:
                projects = load_projects(filename)
                print(f"Loaded {len(projects)} projects from {filename}")
            except FileNotFoundError:
                print(f"Error: File '{filename}' not found!")

        elif choice == 'S':
            filename = input("Enter filename to save to: ")
            save_projects(filename, projects)
            print(f"Saved {len(projects)} projects to {filename}")

        elif choice == 'D':
            display_projects(projects)

        elif choice == 'F':
            filter_projects_by_date(projects)

        elif choice == 'A':
            add_new_project(projects)

        elif choice == 'U':
            update_project(projects)

        elif choice == 'Q':
            save_choice = input(f"Would you like to save to {default_file}? (yes/no): ").strip().lower()
            if save_choice in ['yes', 'y']:
                save_projects(default_file, projects)
                print(f"Saved to {default_file}")
            else:
                print("Not saving to default file.")
            print("Thank you for using custom-built project management software.")
            exit_program = True

        else:
            print("Invalid option! Please try again.")

def load_projects(filename):
    """Load the Project data from the specified file and return the list of Project objects"""
    projects = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        header = lines[0].strip().split('\t')
        for line in lines[1:]:
            line = line.strip()
            parts = line.split('\t')
            name = parts[0]
            # Convert the date string to a Date object
            start_date = datetime.datetime.strptime(parts[1], '%d/%m/%Y').date()
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion = int(parts[4])
            # Create a Project object and add it to the list
            projects.append(Project(name, start_date, priority, cost_estimate, completion))
    return projects

def save_projects(filename, projects):
    """Save the project list to the specified file"""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            start_date_str = project.start_date.strftime('%d/%m/%Y')
            line = (f"{project.name}\t{start_date_str}\t{project.priority}\t"
                    f"{project.cost_estimate}\t{project.completion_percentage}\n")
            file.write(line)

def display_projects(projects):
    """Display both unfinished and completed projects, sorted by priority"""
    incomplete = [p for p in projects if not p.is_completed()]
    incomplete_sorted = sorted(incomplete, key=lambda x: x.priority)

    completed = [p for p in projects if p.is_completed()]
    completed_sorted = sorted(completed, key=lambda x: x.priority)

    print("Incomplete projects:")
    for p in incomplete_sorted:
        print(p)
    print("Completed projects:")
    for p in completed_sorted:
        print(p)

def filter_projects_by_date(projects):
    """Filter items by date (only display items with a start date later than the input date)"""
    date_str = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.datetime.strptime(date_str, '%d/%m/%Y').date()
    except ValueError:
        print("Invalid date format! Please use dd/mm/yyyy.")
        return

    filtered = [p for p in projects if p.start_date > filter_date]
    filtered_sorted = sorted(filtered, key=lambda x: x.start_date)

    for p in filtered_sorted:
        print(p)


def add_new_project(projects):
    """Add new items to the list"""
    print("Let's add a new project")
    name = input("Name: ")
    date_str = input("Start date (dd/mm/yyyy): ")
    start_date = datetime.datetime.strptime(date_str, '%d/%m/%Y').date()
    priority = int(input("Priority: "))
    cost_input = input("Cost estimate: $").strip()
    cost_estimate = float(cost_input)
    completion = int(input("Percent complete: "))

    projects.append(Project(name, start_date, priority, cost_estimate, completion))

def update_project(projects):
    """Update the completion degree and/or priority of the project"""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        choice = int(input("Project choice: "))
        if not (0 <= choice < len(projects)):
            print("Invalid choice!")
            return
    except ValueError:
        print("Please enter a number!")
        return

    project = projects[choice]
    print(f"Selected: {project}")

    new_percent = input("New Percentage: ").strip()
    if new_percent:
        project.completion_percentage = int(new_percent)

    new_priority = input("New Priority: ").strip()
    if new_priority:
        project.priority = int(new_priority)

main()