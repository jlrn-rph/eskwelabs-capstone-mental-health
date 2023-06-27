import pandas as pd
import streamlit as st

st.set_page_config(page_title='Beyond the Numbers of Mental Health')

#  Function that loads the data from a CSV file into a Pandas DataFrame
def load_data():
    data = pd.read_csv(
        "./data/Depression.csv",
        encoding='ISO-8859-1'
    )
    return data

def introduction():
    st.image("./assets/title.gif")
    st.image("./assets/intro-1.png")
    st.image("./assets/intro-2.png")
    st.image("./assets/intro-3.png")
    st.image("./assets/intro-4.png")
    st.image("./assets/intro-5.png")

    st.subheader("Objectives of the Study")
    st.image("./assets/objectives.png")

    st.subheader("Methodology")
    st.image("./assets/methodology.png")
    st.markdown(
        """
        The project pipeline includes web scraping the related subreddits using PRAW for data collection, then processing the text data with SpaCy for tokenization, stopword removal, and lemmatization. To discover topics, the HDP model was applied. Classification models are used to determine the  similarity of user concerns to anxiety and/or depression. Lastly, the BESHY chat bot is built with RASA.
        """
    )

    st.image("./assets/about-data.png")
    st.markdown(
        """
        By scraping Reddit data from subreddits like MentalHealthPH, Anxiety, and Depression, we gathered valuable information such as post titles, text content, scores, flairs, creation dates, and comment counts. 

        This data provides insights into popular topics, user engagement, and trends, facilitating comprehensive descriptive analysis.
        """
    )

    data = load_data()
    with st.expander("View Data"):
        st.dataframe(data)
        st.caption("*Source: Reddit*")

    st.image("./assets/scope.png")

def viz_eda():
    st.title("Exloratory Data Analysis")
    st.image("./assets/eda-night.gif")
    st.markdown(
        """
        Nighttime provides an opportunity for individuals to seek support and engage, finding solace and assistance during a quieter and introspective period.Our aim is to gain a better understanding of the experiences related to mental health among Redditors in the Philippines.
        """
    )

    st.image("./assets/eda-mh.gif")
    st.markdown(
        """
        The analysis highlights a prevalence of discussions on mental health disorders, specifically depression and anxiety, emphasizing the urgent need for increased support and dedicated resources to address these conditions.
        """
    )

    st.image("./assets/eda-talk.png")
    st.markdown(
        """
        Filipinos in r/MentalHealthPH demonstrate a strong desire to be heard, engage in discussions, share their experiences, and seek support, as indicated by the prevalent flairs in the subreddit.
        """
    )

    st.image("./assets/eda-info.png")
    st.markdown(
        """
        Filipinos highly value consolidated and timely information about mental healthcare, evident from the significant number of comments in the INFORMATION and DOCTOR RECOMMENDATION flairs. Accessible and up-to-date resources are crucial in meeting Filipinos' informational needs, Empowering informed decisions for their mental well-being.
        """
    )

    st.image("./assets/eda-space.gif")
    st.markdown(
        """
        Filipinos are actively seeking a space where they can discover and share inspiring stories, as indicated by the significant high score of INSPIRATIONAL flair in the subreddit. Creating safe spaces for open discussions fosters a more empathetic and understanding society regarding mental health.
       """
    ) 

    st.subheader("Topic Modeling")
    st.markdown(
        """
        Reddit has become one of the safe spaces for Filipinos living with mental health conditions.
        """
    )

    st.image("./assets/tp-1.png")
    st.markdown(
        """
        The most frequent topic is general life experiences. Users talk about love, their family, about studying and working. And how it’s like to live day-to-day moments with depression and anxiety.

        Second, users describe their struggles with depression in ways like bottling up feelings and feeling helpless. But amidst these struggles, they talk about being “palaban” too.

        The third is about holding on to hope. About finding light through people they can trust, who console them and who advocate for better mental health.
        """
    )

    st.image("./assets/tp-2.png")
    st.markdown(
        """
        Fourth, users share about overthinking, rejection and being offended. But feeling light, lucky and strong to withstand adversities.

        Lastly, they ask about professional help and discuss experiences leading them to need help like mourning and pressure.
        """
    )

    st.image("./assets/tp-3.png")
    st.markdown(
        """
        Getting help and asking for advice seems like a recent trend. Posts that are only recently gaining attention have topics on getting help while posts that have all-time high engagement do not.
        """
    )

    st.image("./assets/tp-4.png")
    st.markdown(
        """
        While mental health has been recognized as important in general, more recent posts are nuanced in recognizing that physical and mental health go together - physical health problems cause mental health problems and mental health problems manifest as physical symptoms.

        These examples of evolving topics show that discussions are essential in encouraging positive attitudes towards mental health.
        """
    )

    st.image("./assets/tp-5.png")
    st.markdown(
        """
        We found some specific worries of Redittors. They worry about paying bills and want to be financially independent. So it’s not fair for them to still worry about the costs of mental healthcare.

        Redittors are also worried about draging their loved ones down. Mental health conditions do have a ripple effect on the family. Thus, support should be given to their loved ones too.
        """
    )

    st.subheader("What can be done?")
    st.image("./assets/tp-6.png")
    st.markdown(
        """
        We recommend that services and customer support should be available at night because that is when people are free.

        There should also be more safe spaces to talk about mental health like this subreddit where people feel listened to and mental health perceptions can improve.
        """
    )

    st.image("./assets/tp-7.png")
    st.markdown(
        """
        Interventions that allow participants to connect with each other should be considered since Filipinos value being social and belonging in a group.

        Next, is to highlight good stories in social media, the news, movies, books and more to help people believe they can get better.
        """
    )

    st.image("./assets/tp-8.png")
    st.markdown(
        """
        Lastly, it should be easy for Filipinos to get help. Seeking help is a difficult step one. Being able to find the best help should not be another challenge. Thus, we built a chatbot that gives users actionable information about mental health services.
        """
    )

def chatbot():
    st.image("./assets/beshy.gif")
    st.markdown(
        """
        We all have that friend that acknowledges our struggle and encourages us to get help. That friend might be one of our best friends we often call beshy. Just like them, to provide emotional support and a happy you, we developed a bot called BESHY.
        """
    )
    st.warning(
        """
        ⚠️ *We want to emphasize that the chatbot is not intended to be a substitute for professional advice, diagnosis, or treatment. It only provides information to get you started with reaching out to a qualified mental health professional. Ensuring privacy and maintaining ethical practices are also essential for our chatbot. We don't save any information from the user for we respect their privacy and solely aim to provide valuable resources and support*.
        """
    )

    st.image("./assets/features.gif")
    st.markdown(
        """
        There are three key activities that you can do with Beshy.
        * First is to recommend a mental health facility based on your location;
        * Second is to flag high-risk, suicidal thoughts through intent classification; 
        * Lastly, flagging anxiety and depression through the use of a classification model. 
        """
    )

    st.video('./assets/feat-1.mp4')
    st.markdown(
        """
        Firstly, BESHY can recommend nearby mental health facilities based on your location. When you inquire about the nearest facility, BESHY will ask for your current location and provide you with the facility's name, address, and contact number. It will also share additional resources for exploring therapy options.
        """
    )

    st.video('./assets/feat-2.mp4')
    st.markdown(
        """
        Secondly, BESHY is equipped with intent classification capabilities to identify high-risk, suicidal thoughts expressed by users. By utilizing Rasa's Natural Language Understanding, BESHY can categorize messages and promptly offer the suicide hotline number and additional resources for those experiencing suicidal thoughts.
        """
    )

    st.video('./assets/feat-3.mp4')
    st.markdown(
        """
        In addition, our team also worked on both depression and anxiety classification models to flag certain thoughts.

        The user will first express their emotional concern.

        Next, BESHY will give an option to the user if they want to know the status of their concern.

        If yes, the model calculates the probability of whether certain thoughts are flagged as depressed or not, and anxious or not. BESHY will then empathize with the user, offer self care strategies and coping techniques specific to depression and/or anxiety. The user may also use BESHY's mental health facility recommender afterward.


        If the user does not want to know, BESHY will provide general emotional support, self-care techniques, stress management, among others
        """
    )

def conclusion():
    st.title("What to improve?")
    st.image('./assets/conclusion-1.png')
    st.markdown(
        """
        For further improvement, we can include more posts from Reddit using other APIs. We can also expand to other social media platforms.
        """
    )

    st.image('./assets/conclusion-2.png')
    st.markdown(
        """
        Next, we can find better ways to pre-process and apply NLP on posts written in  the Filipino language.        
        """
    )

    st.image('./assets/conclusion-3.png')
    st.markdown(
        """
        We can also find more training data that is specifically from the Philippines.
        """
    )

    st.image('./assets/conclusion-4.png')
    st.markdown(
        """
        Lastly, we can consult with mental health professionals and collaborate with existing initiatives. In addition, we can make the chatbot able to respond in Filipino for inclusivity and to further improve the chatbot's conversational ability.
        """
    )

    st.image('./assets/message.png')

# Meet the team
def the_team():
    st.title("The Team")
    st.markdown(
        """
        We are the team **JARDiS**! We are a group of individuals from diverse backgrounds who came together as part of the Eskwelabs Data Science Cohort 11. In our capstone project, we collaborated to create a data-driven presentation on mental health entitled **Beyond the Numbers of Mental Health: Analyzing Reddit Posts on Mental Health in the Philippines and Developing BESHY (Bot for Emotional Support and a Happy You)**. 
        
        The project involved utilizing the PRAW library for web scraping, spaCy for data processing, conducting exploratory data analysis, and topic modeling using the HDP algorithm to analyze Reddit posts. The team developed classification models employing XGBoost for classifying the mental health concerns of the users. Additionally, geocoding techniques were employed to provide users with recommendations for the nearest mental health facility based on their location. Finally, the solution was deployed within a Rasa-powered chatbot.
        """
    )
    st.header("Members")
    st.subheader("[Austin Loi Carvajal](https://www.linkedin.com/in/austincarvajal/)")
    st.markdown(
        """
        * Worked on the classification model for anxiety. Used the TF-IDF vectorizer on posts about anxiety and posts about random thoughts to be able to train and test different models such as XGBoost, Random Forest, and Support Vector Classifier. This was an important part of creating a chatbot to help users understand their feelings.
        * Brainstormed potential analyses and chatbot functionalities that led to the final project objectives. 
        """
    )
    
    st.subheader("[Ron-Ron de Guzman](https://www.linkedin.com/in/ron-ron-de-guzman-b74a5b92/)")
    st.markdown(
        """
        * Performed web scraping of Reddit posts using the Reddit API, ensuring to obtain as much content as possible that led the team to arrive at useful insights later on.
        * Conducted exploratory data analysis and led the creation of visualizations that supported the value of working on mental health and highlighted the ways to do so.
        * Collected mental health resources as part of the information BESHY is able to provide to users. 
        """
    )

    st.subheader("[Reynaly Shen Javier](https://www.linkedin.com/in/reynaly-shen-javier/)")
    st.markdown(
        """
        * Performed topic modeling and analyzed the topics’ content. This includes studying how topics differ across types of posts and across time and emphasizing mental healthcare problems that need to be worked on.
        * Worked on storytelling and exploratory data analysis to ensure the audience understands and appreciates the problem and the solution the team is offering.
        * Generated recommendations on mental healthcare provision and the technical parts of the project.
        """
    )

    st.subheader("[Denise Montecastro](https://www.linkedin.com/in/denise-montecastro-573b34a2/)")
    st.markdown(
        """
        * Led the ideation of the analyses and modeling that needed to be performed for the project, ending up with a clear data pipeline for the team.
        * Performed and guided the web scraping of Reddit posts using the Reddit API that gathered valuable data for the team to analyze and build models on.
        * Worked on the classification model for depression. Used the TF-IDF vectorizer on posts about anxiety and posts about random thoughts to be able to train and test different models such as XGBoost, Random Forest, and Support Vector Classifier. This was an important part of creating a chatbot to help users understand their feelings.
        """
    )

    st.subheader("[Justin Louise Neypes](https://www.linkedin.com/in/jlrnrph/)")
    st.markdown(
        """
        * Developed and deployed the chatbot using Rasa. This includes defining the bot's behavior by crafting dialogue flows and designing relevant intents, entities, and actions. Performed training and fine-tuning of the model’s Natural Language Understanding, which involved creating training data, analyzing model performance, and iterating on improvements.
        * Implemented custom actions and rules that allowed the bot (1) to empathize with users experiencing anxiety and depression, offering tailored self-care strategies and coping techniques; (2) to handle specific user requests, such as finding the nearest mental health facilities, and (3) to flag high-risk messages such as suicidal thoughts.
        * Spearheaded the design and deployment of the capstone project on Streamlit, showcasing the findings to others.
        """
    )

    st.subheader("Mentor: Aaron Sta. Clara")

# Define the main menu
list_of_pages = [
    "Project Overview",
    "Exploratory Data Analysis",
    "Chatbot: BESHY",
    "Recommendations",
    "The Team"
]

st.sidebar.title(':scroll: Main Menu')
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "Project Overview":
    introduction()

elif selection == "Exploratory Data Analysis":
    viz_eda()

elif selection == "Chatbot: BESHY":
    chatbot()

elif selection == "Recommendations":
    conclusion()

elif selection == "The Team":
    the_team()
