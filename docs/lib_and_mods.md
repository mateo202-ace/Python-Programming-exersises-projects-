# Python Libraries and Modules: Commonly Used Features

### sys
- **Commonly used for**: Accessing system-specific parameters and functions, like command-line arguments or exiting the program.

- **Purpose**: Provides access to system-specific parameters and functions.
    - `sys.exit()`: Stops the program from running, optionally with a status code.
    - `sys.argv`: A list that holds the command-line arguments given to the script.
    - `sys.path`: A list of locations Python looks in to find modules.
    - `sys.stderr`: Used to show error messages, like a special error log.



### os
- **Commonly used for**: Interacting with the operating system, such as file and directory manipulation, environment variables, and process management.

- **Purpose**: Provides a way of using operating system-dependent functionality.
    - `os.getcwd()`: Returns the current working directory.
    - `os.listdir()`: Lists all files and directories in the specified path.
    - `os.environ.get()`: Retrieves the value of an environment variable.
    - `os.open()`: Opens a file and returns a file descriptor.
    - `os.close()`: Closes a file descriptor.
    - `os.remove()`: Deletes a file from the filesystem.
    - `os.getpid()`: Returns the process ID of the current process.
    - `os.system()`: Executes a system command in the shell.
    - `with os.scandir() as entries`: Opens a directory for iteration using a context manager.
    - `with open('file.txt', 'r') as file`: Opens a file safely using a context manager.



### re
- **Commonly used for**: Working with regular expressions to search, match, and manipulate strings.

- **Purpose**: Provides support for regular expressions in Python.
    - `re.match()`: Matches a pattern at the beginning of a string.
    - `re.search()`: Searches for a pattern anywhere in the string.
    - `re.sub()`: Replaces occurrences of a pattern with a specified string.
    - `re.findall()`: Finds all occurrences of a pattern in a string.
    - `re.split()`: Splits a string by the occurrences of a pattern.
    - `re.compile()`: Compiles a regular expression pattern for reuse.
    - `re.escape()`: Escapes special characters in a string to treat them as literals.




### psutil
- **Commonly used for**: Monitoring and managing system resources like CPU, memory, and processes.

- **Purpose**: Provides information on system utilization (CPU, memory, etc.).
    - `psutil.cpu_percent()`: Returns the CPU usage percentage.
    - `psutil.disk_usage()`: Provides disk usage statistics.
    - `psutil.net_io_counters()`: Returns network I/O statistics.
    - `psutil.process_iter()`: Iterates over all running processes.
    - `psutil.sensors_temperatures()`: Retrieves hardware temperature sensors data.
    - `psutil.boot_time()`: Returns the system boot time as a timestamp.




### cryptography
- **Commonly used for**: Implementing secure encryption and decryption, managing keys, and working with cryptographic protocols.

- **Purpose**: Implements cryptographic recipes and primitives.
    - `Fernet.generate_key()`: Generates a new encryption key.
    - `Fernet.encrypt()`: Encrypts data using a Fernet key.
    - `Fernet.decrypt()`: Decrypts data encrypted with a Fernet key.




### yara
- **Commonly used for**: Writing and running rules to identify and classify malware or suspicious files.

- **Purpose**: Used for pattern matching and malware research.
    - `yara.compile()`: Compiles a YARA rule or set of rules.
    - `yara.match()`: Matches compiled rules against a file or data.




### socket
- **Commonly used for**: Creating and managing network connections, like building servers or clients for communication.

- **Purpose**: Provides low-level networking interface.
    - `socket.socket()`: Creates a new socket object.
    - `socket.bind()`: Binds the socket to an address and port.
    - `socket.listen()`: Listens for incoming connections.
    - `socket.connect()`: Connects the socket to a remote address.
    - `socket.send()`: Sends data through the socket.
    - `socket.recv()`: Receives data from the socket.
    - `socket.close()`: Closes the socket connection.




### scrapy
- **Commonly used for**: Web scraping and crawling to extract data from websites.

- **Purpose**: A web scraping framework for extracting data from websites.
    - `scrapy.Request()`: Creates a request object for a URL.
    - `scrapy.Spider`: Defines a spider for crawling and scraping data.
    - `scrapy.Item`: Defines a container for scraped data.
    - `scrapy.Field`: Specifies fields for an item.
    - `scrapy.crawler.CrawlerProcess`: Runs a Scrapy spider programmatically.
    - `scrapy.settings.Settings`: Configures Scrapy settings.




### requests
- **Commonly used for**: Sending HTTP requests like GET, POST, and handling responses easily.

- **Purpose**: Simplifies HTTP requests in Python.
    - `requests.get()`: Sends a GET request to a URL.
    - `requests.post()`: Sends a POST request to a URL.
    - `requests.put()`: Sends a PUT request to a URL.




### beautifulsoup4
- **Commonly used for**: Parsing and navigating HTML or XML documents to extract specific data.

- **Purpose**: Parses HTML and XML documents for web scraping.
    - `BeautifulSoup()`: Creates a BeautifulSoup object for parsing.
    - `.find()`: Finds the first occurrence of a tag or element.
    - `.find_all()`: Finds all occurrences of a tag or element.
- **Module Syntax**: `from bs4 import BeautifulSoup`



### NumPy
- **Commonly used for**: Numerical computations and array manipulations.

- **Purpose**: Provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on them.
    - `numpy.array`: Creates arrays.
    - `numpy.mean`: Computes the mean of an array.
    - `numpy.linspace`: Generates evenly spaced numbers over a range.
- **Example**:
    ```python
    import numpy as np
    arr = np.array([1, 2, 3])
    print(arr.mean())  # Output: 2.0
    ```

### Pandas
- **Commonly used for**: Data manipulation and analysis.

- **Purpose**: Provides data structures and functions for working with structured data like tables.
    - `pandas.DataFrame`: Creates and manipulates tabular data.
    - `pandas.read_csv`: Reads data from CSV files.
    - `pandas.groupby`: Groups data for aggregation.
- **Example**:
    ```python
    import pandas as pd
    data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
    df = pd.DataFrame(data)
    print(df)
    ```

### Matplotlib
- **Commonly used for**: Data visualization and plotting.

- **Purpose**: Provides tools for creating static, animated, and interactive visualizations in Python.
    - `matplotlib.pyplot.plot`: Plots data points.
    - `matplotlib.pyplot.show`: Displays the plot.
    - `matplotlib.pyplot.hist`: Creates histograms.
- **Example**:
    ```python
    import matplotlib.pyplot as plt
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.show()
    ```

### Requests
- **Commonly used for**: Sending HTTP requests and handling responses.

- **Purpose**: Simplifies HTTP requests in Python.
    - `requests.get`: Sends a GET request to a URL.
    - `requests.post`: Sends a POST request to a URL.
    - `requests.json`: Parses JSON responses.
- **Example**:
    ```python
    import requests
    response = requests.get('https://api.github.com')
    print(response.status_code)
    ```

### Flask
- **Commonly used for**: Building web applications and APIs.

- **Purpose**: A lightweight web framework for creating web applications in Python.
    - `Flask`: Creates a Flask application.
    - `@app.route`: Defines routes for the application.
    - `app.run`: Runs the Flask server.
- **Example**:
    ```python
    from flask import Flask
    app = Flask(__name__)
    
    @app.route('/')
    def home():
        return "Hello, Flask!"
    
    if __name__ == '__main__':
        app.run()
    ```

### TensorFlow
- **Commonly used for**: Machine learning and deep learning.

- **Purpose**: Provides tools for building and training machine learning models.
    - `tensorflow.constant`: Creates constant tensors.
    - `tensorflow.keras`: Builds and trains machine learning models.
    - `tensorflow.Variable`: Defines trainable variables.
- **Example**:
    ```python
    import tensorflow as tf
    x = tf.constant(5)
    y = tf.constant(6)
    print(x + y)  # Output: tf.Tensor(11, shape=(), dtype=int32)
    ```

### Scikit-learn
- **Commonly used for**: Machine learning and data analysis.

- **Purpose**: Provides simple and efficient tools for data mining and machine learning.
    - `sklearn.linear_model.LinearRegression`: Performs linear regression.
    - `sklearn.ensemble.RandomForestClassifier`: Implements a random forest classifier.
    - `sklearn.model_selection.train_test_split`: Splits data into training and testing sets.
- **Example**:
    ```python
    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    print(model)
    ```
