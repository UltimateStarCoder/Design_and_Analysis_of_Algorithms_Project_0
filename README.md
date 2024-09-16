# Design and Analysis of Algorithms Project 0

## Setting Up the Virtual Environment

To ensure that all dependencies are managed properly, it's recommended to use a virtual environment. Follow the steps below to create and activate a virtual environment:

### Creating the Virtual Environment

1. Open your terminal.
2. Navigate to your project directory:
    ```
    cd your_project_directory
    ```
3. Create a virtual environment:
    ```
    python3 -m venv venv
    ```

### Activating the Virtual Environment

- On macOS and Linux:
    ```
    source venv/bin/activate
    ```
- On Windows:
    ```
    .\venv\Scripts\activate
    ```


    ### Upgrading and Updating Python

    To ensure you have the latest features and security updates, it's a good idea to upgrade and update your Python installation.

    #### On macOS and Linux:

    1. Upgrade Python using Homebrew:
        ```sh
        brew update
        brew upgrade python
        ```

    #### On Windows:

    1. Download the latest Python installer from the [official Python website](https://www.python.org/downloads/).
    2. Run the installer and follow the instructions to upgrade your Python installation.


### Installing Dependencies

Once the virtual environment is activated, you can install the necessary dependencies:
```sh
pip install -r requirements.txt
```

### Deactivating the Virtual Environment

When you're done working, you can deactivate the virtual environment:
```sh
deactivate
```

