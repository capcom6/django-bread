<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
![Codecov](https://img.shields.io/codecov/c/github/capcom6/django-bread?style=for-the-badge)
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/capcom6/django-bread">
    <img src="assets/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Django Bread</h3>

  <p align="center">
    Web app for managing and storing bread machine recipes.
    <br />
    <!-- <a href="https://github.com/capcom6/django-bread"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/capcom6/django-bread">View Demo</a> -->
    ·
    <a href="https://github.com/capcom6/django-bread/issues">Report Bug</a>
    ·
    <a href="https://github.com/capcom6/django-bread/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
- [About The Project](#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#usage)
  - [User Features](#user-features)
  - [Administrative Features](#administrative-features)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

The Django Bread web application is designed to provide users with a convenient platform for managing and storing their bread machine recipes. Whether you are a seasoned baker or just starting out, this application offers a user-friendly interface to create, edit, and organize your favorite bread machine recipes.

With this application, you can easily enter the ingredients, instructions, and even upload photos of your delicious creations. The intuitive search and filtering options enable you to quickly find specific recipes based on various criteria such as recipe name or ingredients.

We believe that this application will be a valuable tool for anyone passionate about baking bread with their bread machine.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python](https://img.shields.io/badge/Python-3.9%20%7C%203.10%20%7C%203.11-000000?style=for-the-badge)](https://www.python.org/downloads/)
* [![Django](https://img.shields.io/badge/Django-4.2-000000?style=for-the-badge)](https://www.djangoproject.com/)
* [![Pillow](https://img.shields.io/badge/Pillow-10.3-000000?style=for-the-badge)](https://python-pillow.org/)
* [![Django Storages](https://img.shields.io/badge/django_storages-1.12-000000?style=for-the-badge)](https://django-storages.readthedocs.io/en/latest/)
* [![Django REST Framework](https://img.shields.io/badge/djangorestframework-3.15-000000?style=for-the-badge)](https://www.django-rest-framework.org/)
* and others, see [requirements.txt](requirements.txt)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Follow the instructions below to get the Django Bread web application up and running on your local machine.

### Prerequisites

* Python 3.8+: Make sure you have Python installed on your system. You can download the latest version of Python from the official Python website.
* MySQL: You will need a MySQL database server up and running. You can download MySQL from the official MySQL website.

### Installation

1. Pull the Docker image:

   ```
   docker pull capcom6/django-bread
   ```

2. Run the Docker container:

   ```
   docker run -p 8000:8000 capcom6/django-bread
   ```

   This will start the Docker container and map port 8000 of the container to port 8000 of your local machine.

3. Access the Docker container's command line:

   Open a new terminal window and run the following command to access the running Docker container:

   ```
   docker exec -it <container_id> bash
   ```

   Replace `<container_id>` with the ID of the running Docker container. You can find the container ID by running `docker ps`.

4. Create a superuser:

   Inside the Docker container's command line, run the following command to create a superuser:

   ```
   python manage.py createsuperuser
   ```

   Follow the prompts to provide a username, email (optional), and password for the superuser.

5. Exit the Docker container's command line:

   Once the superuser is created, you can exit the Docker container's command line by running the `exit` command.

6. Access the application:

   Open your web browser and visit `http://localhost:8000/admin` to access the Admin Page.

### Configuration

This project uses environment variables for configuration. Below is a list of the environment variables used in the project:

- `SECRET_KEY`: The secret key used for cryptographic signing in Django.
- `DEBUG`: A boolean variable that determines whether the application is running in debug mode. - `WEBSITE_HOSTNAME`: The hostname or domain name that the application is allowed to serve.

- `DB_NAME`: The name of the database used for the default database connection.
- `DB_USER`: The username for authenticating the default database connection.
- `DB_PASSWORD`: The password for authenticating the default database connection.
- `DB_HOST`: The hostname or IP address of the database server. The default value is `127.0.0.1`.
- `DB_PORT`: The port number where the database server is listening. The default value is `3306`.

- `CACHE_DISABLE`: A boolean variable that determines whether caching is disabled.

- `STORAGE_DRIVER`: The driver used for file storage (`file`, `s3` or `azure`).
- `STORAGE_PHOTO_DRIVER`: The driver used specifically for storing photos. It overrides the `STORAGE_DRIVER` setting for photo-related storage.
- `STORAGE_PHOTO_LOCATION`: The location or directory/prefix where photos are stored.
- 
- `AZURE_ACCOUNT_NAME`: The name of the Azure storage account used when the `STORAGE_DRIVER` is set to `azure`.
- `AZURE_ACCOUNT_KEY`: The access key for the Azure storage account.
- `AZURE_CONTAINER`: The name of the container in the Azure storage account where files are stored.

- `AWS_S3_REGION_NAME`: The AWS S3 region name when using the AWS S3 storage driver.
- `AWS_S3_ENDPOINT_URL`: The endpoint URL for the AWS S3 storage service.
- `AWS_STORAGE_BUCKET_NAME`: The name of the AWS S3 bucket where files are stored.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

The Django Bread app offers a user-friendly interface for managing recipes, with additional administrative capabilities through the Django Admin module. Here's how you can utilize the app:

### User Features

1. **Viewing Recipes**: Upon visiting the app's home page, you will find a collection of recipes displayed in recipe cards. Each card provides a glimpse of the recipe, including the title and an accompanying photo. You can scroll through the recipe cards to explore various options.

2. **Detailed Recipe View**: To access more information about a specific recipe, simply click on its corresponding recipe card. This action will take you to the detailed view of the recipe, where you can find the complete set of instructions, ingredients, and any additional notes provided by the recipe creator. Additionally, the detailed view offers the ability to leave comments and engage with other users.

3. **Commenting on Recipes**: As a user, you have the option to provide feedback, ask questions, or share your experiences by leaving comments on recipes. Navigate to the recipe's detailed view and scroll down to the comment section. Enter your comment, and upon submission, it will be visible to other users. This feature fosters a sense of community and encourages interaction among users.

### Administrative Features

1. **Admin Section**: The app provides a dedicated administration section based on the Django Admin module. Access to this section is restricted to users with administrative privileges. From the admin section, you can perform various administrative tasks, such as creating, editing, and deleting recipes and related catalogs. This capability allows you to manage the content available on the app and ensure its accuracy and relevance.

2. **Moderating User Comments**: As an admin, you have the ability to moderate and manage user comments. In the admin section, you can review and take appropriate actions on comments, such as approving, editing, or deleting them. This feature helps maintain a respectful and engaging environment within the app.

<!-- _For more examples, please refer to the [Documentation](https://example.com)_ -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] **Searching and Filtering**: Implement a search functionality to allow users to search for specific recipes based on keywords, ingredients, or categories.
- [ ] **Registration and Login**: Introduce user registration and login functionality to enable personalized user experiences and the ability to save favorites and contribute recipes.
- [ ] **Creating User's Recipes**: Provide users with the ability to create and manage their own recipes, allowing them to share their unique bread machine creations with the community.
- [ ] **Favorites**: Implement a favorites feature that enables users to save recipes they enjoy for quick access and reference.
- [ ] **Share Recipes**: Enable users to easily share recipes with others through various sharing options, such as social media links or email.
- [ ] **Likes**: Add a like functionality to allow users to express their appreciation for recipes and provide feedback to recipe creators.
- [ ] **Mark as Baked**: Introduce a feature that allows users to mark recipes as baked once they have successfully prepared them, providing a sense of accomplishment and helping users track their baking progress.
- [ ] **Personal Notes for Recipes**: Enable users to add personal notes or modifications to recipes, allowing them to customize and adapt recipes to their individual preferences.
- [ ] **Cost Calculation**: Develop a feature that calculates the cost of bread based on the ingredient costs specified in the recipe.
- [ ] **Rating and Reviews**: Implement a rating system that allows users to rate and provide reviews for recipes, enabling others to make informed decisions about trying a particular recipe.
- [ ] **Recipe Tags**: Introduce a categorization system using tags to help users easily navigate and discover recipes based on their preferences.
- [ ] **Recipe Recommendations**: Develop a recommendation engine that suggests recipes to users based on their previous interactions, such as their liked recipes, favorites, or baking history.
- [ ] **Recipe Versioning**: Enable users to create multiple versions or variations of the same recipe, allowing them to experiment and iterate on their bread machine creations.
- [ ] **Print-Friendly Recipes**: Provide a printer-friendly view of recipes that users can easily print out for offline reference while baking.
- [ ] **Integration with Measurement Conversions**: Incorporate a measurement conversion tool that allows users to switch between different measurement systems (e.g., metric and imperial) for ingredients and quantities.
- [ ] **User Notifications**: Implement a notification system to keep users informed about recipe updates, new comments, or interactions related to their recipes or profile.
- [ ] **Language Localization**: Add support for multiple languages to cater to a broader user base and enhance accessibility.
- [ ] **API Integration**: Develop an API that allows other applications or platforms to retrieve recipe data, facilitating integration with third-party services or enabling the creation of companion applications.

See the [open issues](https://github.com/capcom6/django-bread/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the Apache-2.0 license. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/capcom6/django-bread](https://github.com/capcom6/django-bread)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
<!-- ## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/capcom6/django-bread.svg?style=for-the-badge
[contributors-url]: https://github.com/capcom6/django-bread/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/capcom6/django-bread.svg?style=for-the-badge
[forks-url]: https://github.com/capcom6/django-bread/network/members
[stars-shield]: https://img.shields.io/github/stars/capcom6/django-bread.svg?style=for-the-badge
[stars-url]: https://github.com/capcom6/django-bread/stargazers
[issues-shield]: https://img.shields.io/github/issues/capcom6/django-bread.svg?style=for-the-badge
[issues-url]: https://github.com/capcom6/django-bread/issues
[license-shield]: https://img.shields.io/github/license/capcom6/django-bread.svg?style=for-the-badge
[license-url]: https://github.com/capcom6/django-bread/blob/master/LICENSE.txt
[product-screenshot]: assets/screenshot.png
[http-alert]: assets/http-alert.png
[tcp-alert]: assets/tcp-alert.png
[Golang]: https://img.shields.io/badge/Golang-000000?style=for-the-badge&logo=go&logoColor=white
[Golang-url]: https://go.dev/
