# Capstone Project: Beyond the Numbers of Mental Health
This project is created by team **JARDiS**. We are a group of individuals from diverse backgrounds who came together as part of the Eskwelabs Data Science Cohort 11. In our capstone project, we collaborated to create a data-driven presentation on mental health entitled **Beyond the Numbers of Mental Health: Analyzing Reddit Posts on Mental Health in the Philippines and Developing BESHY (Bot for Emotional Support and a Happy You)**.

The project involved utilizing the PRAW library for web scraping, spaCy for data processing, conducting exploratory data analysis, and topic modeling using the HDP algorithm to analyze Reddit posts. The team developed classification models employing XGBoost for classifying the mental health concerns of the users. Additionally, geocoding techniques were employed to provide users with recommendations for the nearest mental health facility based on their location. Finally, the solution was deployed within a Rasa-powered chatbot.

## Project Deployment
[Beyond the Numbers of Mental Health Streamlit](https://jardis-beyond-the-numbers-mental-health.streamlit.app/)

## How to Run Locally
To run the code, please follow these steps:

1. Clone the repository to your local machine.
2. Open your terminal and navigate to the project directory.
3. Install the dependencies using the following command: `pip install -r requirements.txt`.
4. Run the application using the following command: `streamlit run app.py`.
5. The application will open in your browser.

## Recommendations
* Data Collection
    * Include more posts from Reddit through other APIs.
    * Expand to other social media platforms since Reddit users may have characteristics that are specific to them.

* Natural Language Processing
    * Find better ways to pre-process and apply NLP on posts written in the Filipino language.

* Classification Model
    * Find training data that is specifically from the Philippines.

* Chatbot Building
    * Consult with mental health professionals and collaborate with existing initiatives.
    * Make the chatbot able to respond in Filipino for inclusivity.
    * Find ways to improve the chatbot's conversational ability e.g. use other APIs, including therapy and client conversations

![Beyond the Numbers of Mental Health Message](https://github.com/jlrn-rph/eskwelabs-capstone-mental-health/blob/main/assets/message.png)

## Meet the Team
[Austin Loi Carvajal](https://www.linkedin.com/in/austincarvajal/) | [Ron-Ron de Guzman](https://www.linkedin.com/in/ron-ron-de-guzman-b74a5b92/) | [Reynaly Shen Javier](https://www.linkedin.com/in/reynaly-shen-javier/) | [Denise Montecastro](https://www.linkedin.com/in/denise-montecastro-573b34a2/) | [Justin Louise Neypes](https://www.linkedin.com/in/jlrnrph/)

Mentor: Aaron Sta. Clara
