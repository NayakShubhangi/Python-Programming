import sys


class OptionsNotSelected(Exception):
    pass


def process_options(options, selected_options):
    all_selected = all(option in selected_options for option in options)
    if all_selected:
        print(f"All options selected: {', '.join(selected_options)}")
    else:
        raise OptionsNotSelected("All options aren't selected")


if __name__ == "__main__":
    try:
        print(f"Arguments received: {sys.argv}")
        if len(sys.argv) != 3:
            print("Error: Not enough arguments provided.")
            sys.exit(1)
        options = sys.argv[1].split(',')
        selected_options = sys.argv[2].split(',')
        print(f"Options: {options}")
        print(f"Selected Options: {selected_options}")
        process_options(options, selected_options)
    except OptionsNotSelected as e:
        print(e)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)