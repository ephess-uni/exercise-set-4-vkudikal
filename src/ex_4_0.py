""" ex_4_0.py """
try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def get_shutdown_events(logfile):
    """
    Your docstring here.  Replace the pass keyword below with your implementation
    """
    """creating a variable called no_of_lines and assigning a empty list to it"""
    no_of_lines = list()
    with open(logfile, 'r') as lf:
        logs_data = lf.read()   #reading data using read function
    for line in logs_data.splitlines():
        if 'Shutdown initiated' in line :
            #using append function to add lien to no_of_lines
            no_of_lines.append(line)
    return no_of_lines


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f"{get_shutdown_events(FILENAME)=}")
