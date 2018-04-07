
import subprocess

COMMAND_LINE_FIND = "find . -name '*.py' | xargs grep '{}'"
COMMAND_LINE_LINES = "find . -name '*.py' | xargs wc -l"


def _run(command_line):
    yuki_process = subprocess.Popen(
        command_line,
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
        )
    yuki_stdout, yuki_stderr = yuki_process.communicate()
    print(yuki_stdout.decode("utf-8"))


def find(keyword):
    _run(COMMAND_LINE_FIND.format(keyword))


def lines_of_code():
    _run(COMMAND_LINE_LINES)
