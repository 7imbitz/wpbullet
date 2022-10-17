import argparse # Parser for command-line options, arguments and sub-commands
from core import scanner # Importing scanner.py from core package
import signal # Set handlers for asynchronous events (SIGPIPE,SIGINT)
import sys # System-specific parameters and functions


def signal_handler(sig, frame): 
    sys.exit(0) # Raise a SystemExit exception, signaling an intention to exit the interpreter (Set exit to TRUE)


# Register signal handler
signal.signal(signal.SIGINT, signal_handler) # if SIGINT was caught, exit the program

# main function
def main():
    parser = argparse.ArgumentParser(description='Specify scan parameters.') # Argparse description

    # Argparse argument
    # Argparse path to analyze
    parser.add_argument('--path', type=str, dest='path', help='Path to plugin to analyze')
    # Argparse module to enable
    parser.add_argument('--enabled', type=str, dest='enabled', help='Modules to enable', default="")
    # Argparse module to disable
    parser.add_argument('--disabled', type=str, dest='disabled', help='Modules to disable', default="")
    # Argparse cleanup after scanning
    parser.add_argument('--cleanup', type=bool, dest='cleanup', help='Clean .temp folder after scanning remotely downloaded plugin', default=False)
    # Argparse for output json
    parser.add_argument('--report', type=bool, dest='report', help='Saves JSON report inside reports folder', default=False)

    # Collecting argument from argparse, assign to args
    args = parser.parse_args()

    if args.path is None: # If no args was given
        argparse.ArgumentParser.print_usage(parser)        # Print args usage
        exit(1) # exit the system

    scanner.scan(args)# scanner.py from core package was used with the args given (if any)

if __name__ == '__main__': # https://realpython.com/if-name-main-python/
    main() # execute main function define in line 15
