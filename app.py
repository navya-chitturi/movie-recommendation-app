import streamlit as st # This line brings in the Streamlit tool, which helps us build web apps.

# --- CSS Styling for the Streamlit Application ---
# This block uses st.markdown with unsafe_allow_html=True to inject custom CSS.
# This allows for fine-grained control over the app's appearance, creating a cinematic theme.
st.markdown("""
    <style>
    /* Overall Application Styling */
    .stApp {
        /* Sets a picture as the background of our app */
        background-image: url('https://images.unsplash.com/photo-1542204165-65bf26472b9b?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
        
        /* Makes sure the background picture covers the whole screen */
        background-size: cover;
        
        /* Keeps the background picture in place when you scroll */
        background-attachment: fixed;
    }

    /* Styling for the Main Heading (e.g., "🎬 Movie Recommendation") */
    h2 {
        color: #E6B800; /* Makes the text a dark gold color */
        text-align: center; /* Puts the text in the middle */
        margin-bottom: 30px; /* Adds space below the title */
        
        /* Adds a black outline around the text to make it stand out more */
        -webkit-text-stroke: 1px black; /* For web browsers like Chrome/Safari */
        text-stroke: 1px black; /* Standard way to add text outline */
    }

    /* Styling for smaller titles, like "Your Personalized Recommendations" */
    h3 {
        color: #F0F0F0; /* Makes the text a soft white color */
        text-align: center; /* Puts the text in the middle */
        margin-top: 30px; /* Adds space above the title */
        margin-bottom: 20px; /* Adds space below the title */
        
        /* Adds a tiny black outline to make the text a bit clearer */
        -webkit-text-stroke: 0.5px black;
        text-stroke: 0.5px black;
    }

    /* Styling for each movie's information box */
    .movie-box {
        display: flex; /* Arranges items (like poster and details) in a row */
        
        /* Sets a dark, slightly see-through background for the box */
        background-color: rgba(0,0,0,0.75); /* It's 75% black, 25% transparent */
        padding: 15px; /* Adds internal spacing within the box */
        margin-bottom: 20px; /* Adds space between movie boxes */
        border-radius: 12px; /* Makes the corners of the movie box rounded */
        color: white; /* Sets the default text color inside this box to white */
    }

    /* Styling for the movie poster section within the box */
    .poster {
        flex: 0 0 100px; /* Sets the poster's width to 100 pixels */
        margin-right: 20px; /* Adds space to the right of the poster */
    }

    /* Styling for the image of the movie poster */
    .poster img {
        border-radius: 8px; /* Makes the poster image corners rounded */
        max-width: 100px; /* Ensures the image isn't wider than 100 pixels */
        height: auto; /* Keeps the image's original look (proportions) */
    }

    /* Styling for the text details next to the poster */
    .details {
        flex: 1; /* Allows this section to fill up the remaining space */
    }

    /* Styling for the movie's main title inside the box */
    .title {
        font-size: 20px; /* Sets the text size */
        font-weight: bold; /* Makes the text bold */
        color: #FFD700; /* Makes the title a bright gold color */
    }

    /* Styling for the movie's rating */
    .rating {
        color: gold; /* Makes the rating text gold */
        margin-bottom: 5px; /* Adds a little space below the rating */
    }
    </style>
""", unsafe_allow_html=True) # This line is needed to tell Streamlit to use our custom HTML/CSS.

# --- Main App Content ---

# Displays the main heading "Movie Recommendation" on the app.
st.markdown("<h2>🎬 Movie Recommendation</h2>", unsafe_allow_html=True)

# Creates a dropdown menu (select box) for users to pick a user ID.
# The selected ID (1, 2, 3, 4, or 5) will be saved in the 'user_id' variable.
user_id = st.selectbox("Choose a User", [1, 2, 3, 4, 5])

# --- Movie Recommendation Data ---
# This is where we store all the movie information.
# It's set up so that each user ID (1, 2, 3, etc.) has its own list of movies.
# Each movie then has details like its title, year, poster picture, etc.
user_recommendations = {
    1: [ # Movies recommended for User 1
        {
           "title": "Brave", # Movie title
            "year": 2012, # Release year
            "duration": "1h 33m", # Length of the movie
            "rating": 7.1, # Movie rating (out of 10)
            "poster": "https://upload.wikimedia.org/wikipedia/en/9/96/Brave_Poster.jpg", # Link to the movie poster image
            "description": "Merida defies tradition to change her fate.", # Short summary
            "director": "Brenda Chapman, Mark Andrews", # Director(s) of the movie
            "stars": "Kelly Macdonald, Emma Thompson" # Main actors
        },
        # ... more movies for User 1 ...
        {
            "title": "Coco",
            "year": 2017,
            "duration": "1h 45m",
            "rating": 8.4,
            "poster": "https://upload.wikimedia.org/wikipedia/en/9/98/Coco_%282017_film%29_poster.jpg",
            "description": "Miguel enters the Land of the Dead to uncover his family's history.",
            "director": "Lee Unkrich",
            "stars": "Anthony Gonzalez, Gael García Bernal"
        },
        {
            "title": "Frozen",
            "year": 2013,
            "duration": "1h 42m",
            "rating": 7.4,
            "poster": "https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg",
            "description": "Queen Elsa accidentally plunges her kingdom into eternal winter.",
            "director": "Chris Buck, Jennifer Lee",
            "stars": "Kristen Bell, Idina Menzel"
        },
    ],
    2: [ # Movies recommended for User 2
        {
            "title": "3 Idiots",
            "year": 2009,
            "duration": "2h 50m",
            "rating": 8.4,
            "poster": "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
            "description": "Two friends search for their missing college friend.",
            "director": "Rajkumar Hirani",
            "stars": "Aamir Khan, Kareena Kapoor"
        },
        {
            "title": "Moana",
            "year": 2016,
            "duration": "1h 47m",
            "rating": 7.6,
            "poster": "https://upload.wikimedia.org/wikipedia/en/2/26/Moana_Teaser_Poster.jpg",
            "description": "A brave girl sets sail to save her people in Polynesia.",
            "director": "Ron Clements, John Musker",
            "stars": "Auli'i Cravalho, Dwayne Johnson"
        },
        {
            "title": "Luca",
            "year": 2021,
            "duration": "1h 35m",
            "rating": 7.4,
            "poster": "https://upload.wikimedia.org/wikipedia/en/3/33/Luca_%282021_film%29.png",
            "description": "A sea monster experiences an unforgettable summer in Italy.",
            "director": "Enrico Casarosa",
            "stars": "Jacob Tremblay, Jack Dylan Grazer"
        },
    ],
    3: [ # Movies recommended for User 3
        {
            "title": "Interstellar",
            "year": 2014,
            "duration": "2h 49m",
            "rating": 8.6,
            "poster": "https://m.media-amazon.com/images/I/91kFYg4fX3L._AC_UF1000,1000_QL80_.jpg",
            "description": "Explorers journey through space and time to save Earth.",
            "director": "Christopher Nolan",
            "stars": "Matthew McConaughey, Anne Hathaway"
        },
        {
            "title": "Avengers: Endgame",
            "year": 2019,
            "duration": "3h 1m",
            "rating": 8.4,
            "poster": "https://upload.wikimedia.org/wikipedia/en/0/0d/Avengers_Endgame_poster.jpg",
            "description": "The Avengers unite for one last stand against Thanos.",
            "director": "Russo Brothers",
            "stars": "Robert Downey Jr., Chris Evans"
        },
        {
            "title": "Toy Story 3",
            "year": 2010,
            "duration": "1h 43m",
            "rating": 8.3,
            "poster": "https://upload.wikimedia.org/wikipedia/en/6/69/Toy_Story_3_poster.jpg",
            "description": "Woody, Buzz, and the gang face an uncertain future.",
            "director": "Lee Unkrich",
            "stars": "Tom Hanks, Tim Allen"
        },
    ],
    4: [ # Movies recommended for User 4
        {
            "title": "Ratatouille",
            "year": 2007,
            "duration": "1h 51m",
            "rating": 8.1,
            "poster": "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
            "description": "A rat dreams of becoming a great chef in Paris.",
            "director": "Brad Bird",
            "stars": "Patton Oswalt, Lou Romano"
        },
        {
            "title": "Soul",
            "year": 2020,
            "duration": "1h 40m",
            "rating": 8.0,
            "poster": "https://upload.wikimedia.org/wikipedia/en/3/39/Soul_%282020_film%29_poster.jpg",
            "description": "A musician's soul gets separated from his body before his big break.",
            "director": "Pete Docter",
            "stars": "Jamie Foxx, Tina Fey"
        },
        {
            "title": "Inside Out",
            "year": 2015,
            "duration": "1h 35m",
            "rating": 8.2,
            "poster": "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",
            "description": "A young girl's emotions come to life as she navigates a big move.",
            "director": "Pete Docter",
            "stars": "Amy Poehler, Phyllis Smith"
        },
    ],
    5: [ # Movies recommended for User 5
        {
            "title": "Up",
            "year": 2009,
            "duration": "1h 36m",
            "rating": 8.2,
            "poster": "https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
            "description": "A widowed balloon salesman flies his house to South America.",
            "director": "Pete Docter, Bob Peterson",
            "stars": "Edward Asner, Jordan Nagai"
        },
        {
            "title": "Finding Nemo",
            "year": 2003,
            "duration": "1h 40m",
            "rating": 8.1,
            "poster": "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",
            "description": "A clownfish sets out to find his missing son.",
            "director": "Andrew Stanton",
            "stars": "Albert Brooks, Ellen DeGeneres"
        },
        {
            "title": "The Shawshank Redemption",
            "year": 1994,
            "duration": "2h 22m",
            "rating": 9.3,
            "poster": "https://m.media-amazon.com/images/I/51NiGlapXlL._AC_.jpg",
            "description": "Two imprisoned men bond over years, finding redemption through acts of decency.",
            "director": "Frank Darabont",
            "stars": "Tim Robbins, Morgan Freeman"
        },
    ],
}

# --- Displaying Recommendations ---

# Creates a button labeled "Show Recommendations"
# The code inside this 'if' block will only run when the button is clicked.
if st.button("Show Recommendations"):
    # Displays a subheading "Your Personalized Recommendations" when the button is pressed.
    st.markdown("<h3>🍿 Your Personalized Recommendations</h3>", unsafe_allow_html=True)
    
    # Goes through each movie in the recommendations list for the chosen user.
    for movie in user_recommendations[user_id]:
        # For each movie, it creates a movie box using custom HTML and fills it with movie data.
        # This uses an f-string to easily insert Python variables (like movie details) into the HTML.
        st.markdown(f"""
            <div class="movie-box">
                <div class="poster">
                    <img src="{movie['poster']}" width="100">
                </div>
                <div class="details">
                    <div class="title">{movie['title']} ({movie['year']})</div>
                    <div class="rating">⭐ {movie['rating']} | ⏱ {movie['duration']}</div>
                    <div>{movie['description']}</div>
                    <div><b>Director:</b> {movie['director']}</div>
                    <div><b>Stars:</b> {movie['stars']}</div>
                </div>
            </div>
        """, unsafe_allow_html=True) # unsafe_allow_html=True is needed to tell Streamlit to display our custom HTML.