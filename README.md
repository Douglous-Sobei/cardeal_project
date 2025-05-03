# Car Sales Web Application

This is a web application built using Django framework for managing and showcasing cars for sale. The application allows car business owners to list their cars, manage inventory, and interact with potential buyers. Users can browse through the latest cars, search and filter based on model or price, and make inquiries about the cars they're interested in.

## Features

- **Car Listings**: Car owners can list their cars on the website, providing details such as model, price, year, mileage, and description.
- **Search and Filter**: Users can search for cars based on model, price range, or other criteria, making it easy to find the desired vehicle.
- **Dynamic Page Navigation**: The website offers dynamic page numbers for browsing through a large number of car listings, enhancing user experience.
- **Notification System**: Users receive success or error notifications for actions like car inquiries, login attempts, or registration.
- **Authentication**: The application provides login and registration forms for users, ensuring security and personalized experiences.
- **Social Login Integration**: Users can log in using their Google or Facebook accounts, simplifying the authentication process.
- **Responsive Design**: The website is designed to be responsive, ensuring optimal viewing experience across various devices.

## Setup

1. **Clone the Repository**: Clone this repository to your local machine by running:

   ```
   git clone https://github.com/Douglous-Sobei/cardeal_project
   ```

2. **Install Dependencies**: Navigate to the project directory and install the required dependencies using pip:

   ```
   pip install -r requirements.txt
   ```

3. **Database Setup**: Configure the database settings in `settings.py` and run migrations to create the necessary database schema:

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Static and Media Files**: Configure static and media files settings in `settings.py` and collect static files:

   ```
   python manage.py collectstatic
   ```

5. **Run the Application**: Start the Django development server by running:

   ```
   python manage.py runserver
   ```

   You can then access the application locally at [http://localhost:8000](http://localhost:8000).

## Deployment

The application is deployed on Railway, providing a scalable and reliable platform for hosting Django applications. You can access the deployed application at [https://cardealership-project-production.up.railway.app/](https://cardealership-project-production.up.railway.app/).

## Contributors

- [Douglous Sobei](https://github.com/Douglous-Sobei)

## License

This project is licensed under the [MIT License](LICENSE).
