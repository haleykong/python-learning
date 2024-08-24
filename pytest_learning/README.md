**References**
Pytest Tutorial: https://www.youtube.com/watch?v=cHYq1MRoyI0
Pytest Fixtures: https://www.youtube.com/watch?v=ScEQRKwUePI

*Known Run Environment*
python 3.8.8
pytest 6.2.3


*Run Command*
pytest tests/{script_name} (runs all tests in file)
Flags:
-v for additional information
-s for printing output like print statements
pytest test/{script_name} -k {test_name} (runs specific tests in file)

*Files*
source - module that contains classes and functions for testing
tests - scripts for pytest
