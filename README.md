# All That Music
Welcome to All That Music, a web application for music lovers who want to organize and explore their collection of albums, artists, and songs in an easy and efficient way.

## Project Description
All That Music allows users to:
v1.0 its already deployed on https://allthatmusic.pythonanywhere.com/

- Create and manage artist profiles.
- Explore and manage albums and songs.
- Integrate information from streaming platforms like Deezer.
- Save song lyrics and links to YouTube videos.

## Key Features

- Artist Management: Create artist profiles with biographies, photos, and social media links.
- Album and Song Exploration: Browse and discover albums and songs, and search for new releases.
- Integration with Streaming Platforms: Connect to Deezer for up-to-date information and direct music access.
- Lyrics Management: Save the lyrics of your favorite songs for quick access.

## Installation
To install and run the project locally, follow these steps:

1. Clone the repository
> git clone https://github.com/josejonnathan/AllThatMusic.git
2. Navigate to the project directory: 
> cd all-that-music
3. Create and activate a virtual environment:
> python3 -m venv venv
> source venv/bin/activate  # unix
> 
> venv\Scripts\activate # windows
4. Install the required dependencies:
> pip install -r requirements.txt
5. Apply the migrations to set up the database:
> python manage.py migrate
6. Start the Django development server:
> python manage.py runserver
7. Open a web browser and navigate to http://127.0.0.1:8000/

8. (Optional) if you want to populate the database with a sample data run the following line before run the server
>python manage.py loaddata SampleDB.json

## Contribution
If you would like to contribute to the project, follow these steps:

1. Fork the repository.
2. Create a branch for your changes:
>git checkout -b my-branch
3. Make your changes and commit them:
>git add .
>git commit -m "Description of change"
4. Push your branch to the remote repository:
>git push origin my-branch
5. Open a Pull Request explaining your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.


