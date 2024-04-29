""" ex_4_3.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def time_between_shutdowns(logfile):
    """
    Your docstring here.  Replace the pass keyword below with your implementation.
    """
    no_of_lines = get_shutdown_events(logfile)
    first_Shutdown = no_of_lines[0]
    last_Shutdown = no_of_lines[-1]
    first_shutdown_1 = logstamp_to_datetime(first_Shutdown.split()[1])
    second_shutdown = logstamp_to_datetime(last_Shutdown.split()[1])
    return (second_shutdown-first_shutdown_1)

# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
