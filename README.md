# CineWhiz - Personalised Movie Recommendation System  
This software helps you get movie recommendations based on natural language prompts. The system intelligently understands the prompt and identifies the implicit filters as well as search terms. If the prompt is "Time travel movies directied by Christopher Nolan", system will automatically search for time-travel movies and then filter the movies directed by Christopher Nolan. Similar filters also exist for actors, genres, ratings, year of release etc. 

## GUI Demo and Example
The GUI is very simple and looks like this.
<img width="846" alt="image" src="https://github.com/suhas4122/CineWhiz/assets/83380535/aa444e14-45d5-4267-8a4f-007b5c4773c3">
On typing the search term and pressing enter the results are displayed.
### Example
<img width="846" alt="image" src="https://github.com/suhas4122/CineWhiz/assets/83380535/018b08b9-348b-4018-bde1-e8eeb5d76d3a">
<img width="846" alt="image" src="https://github.com/suhas4122/CineWhiz/assets/83380535/44dac61f-8418-4709-b38e-d623b22c5648">

## Running Instructions
- Install Docker and other pre-requisite softwares
- Get an API key from OpenAI and add it to config.py file
- Install required packages
  ```
  pip install -r requirements.txt
  ```
- Initialise docker image and this command from the main folder
  ```
  sudo docker run --name redis-stack-server -p 6380:6379 -v ./data/embeddings/:/data redis/redis-stack-server:latest
  ```
- Scrape movie data: Use scrape_imdb.py file to scrape more movie data if required, to scrape put names of all the required movies in a csv file and run the python file. Please note data of around 6000 movies already exists.
- Make the vector store and database
  ```
  python3 -m models.setup
  ```
- Run the streamlit app
  
  ```
  streamlit run app.py
  ```
