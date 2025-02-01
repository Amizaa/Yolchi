# Yolchi - Transportation and Cargo system


Welcome to **Yolchi**, a comprehensive transportation system designed to streamline the logistics and transportation process for both drivers and shippers. Built with Django, HTML, CSS, Bootstrap, and JavaScript, Yolchi provides a user-friendly interface and robust functionality to meet the needs of its users.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Apps](#apps)
  - [Yol](#yol)
  - [Yuk](#yuk)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **User  Authentication**: Secure login and registration for drivers and shippers.
- **Driver App (Yol)**: 
  - View available shipments
  - Register and Change personal information
  - Accept or decline shipment requests
  - See and Print waybill
- **Shipper App (Yuk)**: 
  - Create and manage shipment requests
  - Track shipment progress
- **Responsive Design**: Built with Bootstrap for a seamless experience on all devices.
- **Real-time Updates**: JavaScript integration for live updates on shipment status.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Database**: SQLite
- **Version Control**: Git

## Installation

To set up the Yolchi project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Amizaa/Yolchi.git
   cd yolchi_system

2. **Install the required packages**:
   ```bash
   pip install -r requirements.txt

3. **Run the deployment server**:
    ```bash
    python manage.py runserver

4. **Access the application**:
Open your web browser and go to http://127.0.0.1:8000/.

## Usage

Once the application is running, you can register as a driver or shipper. Explore the features of Yol and Yuk to manage your transportation needs effectively.

## Apps

### Yol

The **Yol** app is designed specifically for drivers. It allows them to:

- View and accept shipment requests
- Track their current shipments
- Update shipment status in real-time

### Yuk

The **Yuk** app is tailored for shippers. It provides functionalities to:

- Create new shipment requests
- Monitor driver availability
- Track the progress of their shipments

## Contributing

We welcome contributions to Yolchi! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any inquiries or feedback, please reach out to:

- **Your Name** - [Amirreza Noruzi](mailto:amirrezanoruziiii@gmail.com)
- **GitHub**: [Amizaa](https://github.com/Amizaa)

Thank you for checking out Yolchi! We hope you find it useful for your transportation needs.