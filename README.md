# Login Page and User Management

![GitHub stars](https://img.shields.io/github/stars/MuhammedBasith/LoginPage?style=social)
![GitHub forks](https://img.shields.io/github/forks/MuhammedBasith/LoginPage?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/MuhammedBasith/LoginPage?style=social)

This repository contains multiple versions of a Python login page project, each showcasing a different method of user management, all implemented through a command-line interface (CLI).

## Table of Contents

- [About](#about)
- [Versions](#versions)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## About

This project provides various implementations of a login page and user management system, all built with Python. Each version demonstrates a different approach to user management, including databases, shelves, and normal I/O, all accessible via the command line.

## Versions

### 1. Database Version

- Implements user management using a SQLite database.
- Users can create accounts, and their credentials are stored securely.
- Provides login functionality with password hashing.

### 2. Shelves Version

- Manages user data using Python's built-in `shelve` module.
- Users can create accounts, and their data is stored as key-value pairs.
- Implements a basic login system.

### 3. Normal I/O Version

- Stores user data in text files.
- Users can create accounts, and their credentials are stored as plain text.
- Demonstrates a simple login system.

Choose the version that best suits your needs or explore them all to understand the different approaches to user management through the command line.

## Getting Started

To get started with any of the versions, follow these steps:

1. Clone this repository:

   ```sh
   git clone https://github.com/MuhammedBasith/LoginPage.git
   ```

2. Navigate to the version directory you want to explore, e.g., `DatabaseVersion`, `ShelvesVersion`, or `NormalIOVersion`.

3. Run the respective version's Python script.

   ```sh
   python login.py
   ```

## Usage

1. Launch the chosen version's script as mentioned in the "Getting Started" section.
2. Follow the command-line instructions to create an account and log in.

Feel free to customize and extend any of the versions to suit your specific project requirements.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Open a pull request to the `main` branch of this repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Happy coding!
