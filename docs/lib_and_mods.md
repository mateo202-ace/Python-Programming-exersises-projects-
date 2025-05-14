# Python Libraries and Modules: Commonly Used Features

### sys
- **Commonly used for**: Accessing system-specific parameters and functions, like command-line arguments or exiting the program.

- **Purpose**: Provides access to system-specific parameters and functions.
    - `sys.exit()`: Exits the program with an optional exit status.
    - `sys.argv`: Provides a list of command-line arguments passed to the script.



### os
- **Commonly used for**: Interacting with the operating system, such as file and directory manipulation, environment variables, and process management.

- **Purpose**: Provides a way of using operating system-dependent functionality.
    - `os.getcwd()`: Returns the current working directory.
    - `os.listdir()`: Lists all files and directories in the specified path.
    - `os.environ.get()`: Retrieves the value of an environment variable.



### re
- **Commonly used for**: Working with regular expressions to search, match, and manipulate strings.

- **Purpose**: Provides support for regular expressions in Python.
    - `re.match()`: Matches a pattern at the beginning of a string.
    - `re.search()`: Searches for a pattern anywhere in the string.
    - `re.sub()`: Replaces occurrences of a pattern with a specified string.




### psutil
- **Commonly used for**: Monitoring and managing system resources like CPU, memory, and processes.

- **Purpose**: Provides information on system utilization (CPU, memory, etc.).
    - `psutil.cpu_percent()`: Returns the CPU usage percentage.
    - `psutil.virtual_memory()`: Provides details about system memory usage.




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




### scrapy
- **Commonly used for**: Web scraping and crawling to extract data from websites.

- **Purpose**: A web scraping framework for extracting data from websites.
    - `scrapy.Request()`: Creates a request object for a URL.
    - `scrapy.Spider`: Defines a spider for crawling and scraping data.




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








## 1. NumPy
- **Commonly Used Modules/Functions**:
    - `numpy.array`: Create arrays.
    - `numpy.mean`: Compute the mean of an array.
    - `numpy.linspace`: Generate evenly spaced numbers over a range.
- **Example**:
        ```python
        import numpy as np
        arr = np.array([1, 2, 3])
        print(arr.mean())  # Output: 2.0
        ```

## 2. Pandas
- **Commonly Used Modules/Functions**:
    - `pandas.DataFrame`: Create and manipulate tabular data.
    - `pandas.read_csv`: Read data from CSV files.
    - `pandas.groupby`: Group data for aggregation.
- **Example**:
        ```python
        import pandas as pd
        data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
        df = pd.DataFrame(data)
        print(df)
        ```

## 3. Matplotlib
- **Commonly Used Modules/Functions**:
    - `matplotlib.pyplot.plot`: Plot data points.
    - `matplotlib.pyplot.show`: Display the plot.
    - `matplotlib.pyplot.hist`: Create histograms.
- **Example**:
        ```python
        import matplotlib.pyplot as plt
        plt.plot([1, 2, 3], [4, 5, 6])
        plt.show()
        ```

## 4. Requests
- **Commonly Used Modules/Functions**:
    - `requests.get`: Perform GET requests.
    - `requests.post`: Perform POST requests.
    - `requests.json`: Parse JSON responses.
- **Example**:
        ```python
        import requests
        response = requests.get('https://api.github.com')
        print(response.status_code)
        ```

## 5. Flask
- **Commonly Used Modules/Functions**:
    - `Flask`: Create a Flask application.
    - `@app.route`: Define routes for the application.
    - `app.run`: Run the Flask server.
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

## 6. TensorFlow
- **Commonly Used Modules/Functions**:
    - `tensorflow.constant`: Create constant tensors.
    - `tensorflow.keras`: Build and train machine learning models.
    - `tensorflow.Variable`: Define trainable variables.
- **Example**:
        ```python
        import tensorflow as tf
        x = tf.constant(5)
        y = tf.constant(6)
        print(x + y)  # Output: tf.Tensor(11, shape=(), dtype=int32)
        ```

## 7. BeautifulSoup
- **Commonly Used Modules/Functions**:
    - `BeautifulSoup`: Parse HTML or XML documents.
    - `.find`: Find the first matching tag.
    - `.find_all`: Find all matching tags.
- **Example**:
        ```python
        from bs4 import BeautifulSoup
        html = "<html><body><h1>Hello</h1></body></html>"
        soup = BeautifulSoup(html, 'html.parser')
        print(soup.h1.text)  # Output: Hello
        ```

## 8. Scikit-learn
- **Commonly Used Modules/Functions**:
    - `sklearn.linear_model.LinearRegression`: Perform linear regression.
    print(os.getcwd())  # Prints the current working directory
    ```
