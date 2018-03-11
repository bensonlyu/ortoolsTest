# ortoolsTest
This repository contains Benson's tests and modified codes based on the Google Optimization Tool, the ortools package.

More tests will be implemented to solve problems such as routing, bin packing, network flows, assignment, scheduling, puzzles, etc. in the next month.

*by Benson, 03/10/2018*

To use the .py codes, please follow the steps below.
 1. Verify that you have Python 2.7+, 3.5, or 3.6, by `python --version` and pip 9.01 or higher by `pip -V`. If not, please update the pip by `install --upgrade pip`.
 2. Install the ortools using pip by `pip install --upgrade ortools`. 
 3. Test the ortools' dependencies using the check_python_deps.py. If there were any issues with ortools version tag, please check out [#384](https://github.com/google/or-tools/issues/384) and [#489]( https://github.com/google/or-tools/issues/489). You can also manually install .whl or .egg files from [6.4.4495](https://pypi.python.org/pypi/ortools/6.4.4495) and change the version tag to "6.4.4495" in the \__init\__.py under the ortools package.
 4. Test these .py codes to see their results.
 5. For more sample .py projects created by Google, please check out [ortools sample](https://github.com/google/or-tools/releases/download/v6.4/or-tools_python_examples_v6.4.4495.zip).

*by Benson, 03/11/2018*
