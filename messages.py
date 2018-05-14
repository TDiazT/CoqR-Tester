def interpreting(filename):
    return "Interpreting tests in {0:s}".format(filename)


def running_interpreter(interpreter):
    return "Running {0:s} interpreter...".format(interpreter)


def finished_in(time):
    return "Finished in {0:f} seconds".format(time)


def processing_output(language):
    return "Processing {0:s} output".format(language)


def processed_finished_with_output(output):
    return "Done, you may find the results in {0:s}".format(output)


RUNNING_R_INTERPRETER_MSG = running_interpreter("R")
RUNNING_COQ_INTERPRETER_MSG = running_interpreter("Coq")
SENDING_RESULTS = 'Sending results to server'
SENT_SUCCESSFULLY = 'Sent successfully'
ERROR_SENDING = 'There was an error sending the report to server'
PROCESS_FINISHED_MSG = "Done!"
COMPARING_MSG = "Comparing"
GENERAL_STATS_HEADER = "---------- GENERAL STATS ----------"
